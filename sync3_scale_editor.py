import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from PySide6.QtWidgets import QDialog, QPushButton, QSpacerItem, QSizePolicy, QMessageBox, QLabel, QFileDialog, QWidget, QGridLayout
from PySide6.QtCore import Slot, QRect, Qt

from ui_sync3_scale_editor import Ui_sync3ScaleEditor
from ui_sync3_ratio import Ui_sync3Ratio
from viatools.sync3_scales import Sync3ScaleSet
from via_resource_editor import ViaResourceEditor


class Sync3RatioXY(FigureCanvasQTAgg):
    def __init__(self, numerator, denominator):
        fig = Figure(figsize=(1,1), facecolor='black')
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        domain = np.linspace(0, 2 * np.pi * denominator, 256)
        self.axes.plot(np.sin(domain), np.cos(domain * (numerator/denominator)), color='white')
        super(Sync3RatioXY, self).__init__(fig)
    
    def update_plot(self, numerator, denominator):
        self.axes.cla()
        self.axes.set_facecolor('black')
        domain = np.linspace(0, 2 * np.pi * denominator, 256)
        self.axes.plot(np.sin(domain), np.cos(domain * (numerator/denominator)), color='white')
        self.draw()

class Sync3Ratio(QDialog, Ui_sync3Ratio):
    def __init__(self, numerator, denominator):
        super().__init__()
        self.setupUi(self)
        self.decimalData.setText('%.4f' % (numerator/denominator))
        self.semitonesData.setText('%.4f' % (np.log2(numerator/denominator) * 12))
        self.xyLayout.addWidget(Sync3RatioXY(numerator,denominator))

class Sync3ScaleEditor(ViaResourceEditor, Ui_sync3ScaleEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text=''):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)
        self.style_text = style_text

        #TODO pass through to resources through constructors
        self.scale_size = 32

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = Sync3ScaleSet(resource_dir, slug)

        self.update_resource_sets()
        self.update_resources()

        self.active_ratio_idx = 0
        self.create_seed_ratio_grid()

        self.preview_idx = 16
        self.init_preview_display()

        for slot_num in range(0, 8):
            eval('self.slot%d' % (slot_num+1)).clicked.connect(lambda state=True, x=slot_num: self.switch_slot(x))
        self.selectResource.activated.connect(self.handle_select_resource)
        self.saveResource.clicked.connect(lambda state=True: self.handle_save_resource())

        self.slot1.setChecked(True)
        self.switch_slot(0)

        self.update_resource_ui()

# Edit scale recipe

    @Slot()
    def on_addSeedRatio_clicked(self):
        ratio = [int(self.numerator.value()), int(self.denominator.value())]
        print(ratio)
        self.add_seed_ratio(ratio)

    @Slot()
    def on_addFromScala_clicked(self):
        scala_path = QFileDialog.getOpenFileName(self, 'Import Scala File')[0]
        with open(scala_path) as scala_file:
            scala_ratios = []
            for line in scala_file.readlines():
                fixed_line = line.replace('\n', '')
                fixed_line = fixed_line.replace(' ', '')
                parse_try = fixed_line.split('/')
                print(parse_try)
                if len(parse_try) == 2:
                    if parse_try[0].isnumeric() and parse_try[1].isnumeric():
                        scala_ratios.append([int(parse_try[0]), int(parse_try[1])])
        for ratio in scala_ratios:
            self.add_seed_ratio(ratio)
                

    @Slot()
    def on_clearSeedRatios_clicked(self):
        if QMessageBox.question(self, 'Clear Ratios', 'Clear all ratios?') == QMessageBox.Yes: 
            self.set.resources[self.active_idx].data['seed_ratios'] = []
            self.update_resource_ui()

# Tiling method selection

    @Slot()
    def on_fillExpand_clicked(self):
        self.update_fill_method('expand')

    @Slot()
    def on_fillOctave_clicked(self):
        self.update_fill_method('octave')

    @Slot()
    def on_fillTritave_clicked(self):
        self.update_fill_method('tritave')

# Preview section slots

    @Slot()
    def on_cvSlider_valueChanged(self):
        self.preview_idx = self.cvSlider.value() + self.knob.value()    
        self.update_preview()

    @Slot()
    def on_knob_valueChanged(self):
        self.preview_idx = self.cvSlider.value() + self.knob.value()
        self.update_preview()

    @Slot()
    def on_previewSelect_activated(self):
        self.change_preview_display(self.previewSelect.currentText())
        self.update_preview()

# Seed ratio dispaly helpers

    def add_seed_ratio(self, ratio): 
        if self.check_data(ratio):
            self.set.resources[self.active_idx].add_data(self.reduce_ratio(ratio))
            self.update_resource_ui()
            self.unsaved_scale_changes = True
            print('Added')
        else:
            reduced = self.reduce_ratio(ratio)
            print('Ratio %d/%d exists in set as %d/%d' % (ratio[0], ratio[1], reduced[0], reduced[1]))
    
    def check_data(self, ratio):
        reduced_ratio = self.reduce_ratio(ratio)
        if reduced_ratio in self.set.resources[self.active_idx].data['seed_ratios']:
            #TODO prompt to override
            return False
        else:
            return True

    def reduce_ratio(self, ratio):
        gcd = np.gcd(ratio[0], ratio[1])
        reduced_ratio = [1, 1]
        reduced_ratio[0] = int(ratio[0]/gcd)
        reduced_ratio[1] = int(ratio[1]/gcd)
        return reduced_ratio

    def seed_button_pushed(self, idx):
        ratio = self.set.resources[self.active_idx].data['seed_ratios'][idx]
        self.ratio_dialog = Sync3Ratio(ratio[0], ratio[1])
        self.ratio_dialog.removeRatio.clicked.connect(self.remove_ratio)
        self.ratio_dialog.close.clicked.connect(self.close_ratio_dialog)
        self.ratio_dialog.setWindowTitle('%d/%d' % (ratio[0], ratio[1]))
        self.ratio_dialog.setStyleSheet(self.style_text)
        self.active_ratio_idx = idx
        self.ratio_dialog.exec()

    def close_ratio_dialog(self):
        self.ratio_dialog.accept()

    def remove_ratio(self):
        self.set.resources[self.active_idx].remove_data(self.active_ratio_idx)
        self.update_resource_ui()
        self.unsaved_scale_changes = True
        self.ratio_dialog.accept()

    def create_seed_ratio_grid(self):
        self.scroll_widget = QWidget()
        self.scroll_widget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.seedRatioGrid = QGridLayout()
        self.seed_ratio_buttons = []
        self.num_columns = 4
        self.num_rows = 8
        for row in range(0, self.num_rows):
            for column in range(0, self.num_columns):
                idx = row * self.num_columns + column
                new_button = QPushButton()
                new_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                new_button.setFixedSize(80, 20)
                sp = new_button.sizePolicy()
                sp.setRetainSizeWhenHidden(True)
                new_button.setSizePolicy(sp)
                new_button.clicked.connect(lambda state=True, x=idx: self.seed_button_pushed(x))
                self.seed_ratio_buttons.append(new_button)
                self.seedRatioGrid.addWidget(new_button, row, column)
        self.scroll_widget.setLayout(self.seedRatioGrid)
        self.seedRatios.setWidget(self.scroll_widget)      


    def update_resource_ui(self):
        seed_ratios = self.set.resources[self.active_idx].data['seed_ratios']
        idx = -1
        for idx, ratio in enumerate(seed_ratios):
            self.seed_ratio_buttons[idx].show()
            self.seed_ratio_buttons[idx].setText('%s/%s' % (ratio[0], ratio[1]))
        for i in range(idx+1, 32):
            self.seed_ratio_buttons[i].hide()
        self.update_fill_method(self.set.resources[self.active_idx].data['fill_method'])

# Fill method helpers

    def update_fill_method(self, fill_method):
        seed_ratios = self.set.resources[self.active_idx].data['seed_ratios']
        #TODO make this into a function somewhere
        lt_1 = []
        gt_1 = []
        for ratio in seed_ratios:
            if ratio[0]/ratio[1] < 1:
                lt_1.append(ratio)
            elif ratio[0]/ratio[1] > 1:
                gt_1.append(ratio)
        if len(lt_1) > self.scale_size/4 or len(gt_1) > self.scale_size/4:
            tile_ok = False
        else:
            tile_ok = True
            
        if self.set.resources[self.active_idx].data['fill_method'] != fill_method:
            self.unsaved_scale_changes = True

        if not tile_ok:
            fill_method = 'expand'
            print('Forcing expand because too many ratios')

        if fill_method == 'octave':
            self.fillOctave.setChecked(True)
            self.set.resources[self.active_idx].data['fill_method'] = fill_method
        elif fill_method == 'tritave': 
            self.fillTritave.setChecked(True)
            self.set.resources[self.active_idx].data['fill_method'] = fill_method
        elif fill_method == 'expand':       
            self.fillExpand.setChecked(True)
            self.set.resources[self.active_idx].data['fill_method'] = fill_method
        self.set.bake()
        self.update_preview()

# Preview helpers

    def init_preview_display(self):
        self.decimalPreview = QLabel()
        self.decimalPreview.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.decimalPreview.setText('Value')
        self.semitonePreview = QLabel()
        self.semitonePreview.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.semitonePreview.setText('Value')
        self.ratioPreview = QLabel()
        self.ratioPreview.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ratioPreview.setText('Value')
        self.xyPreview = Sync3RatioXY(1, 1)
        self.previewContainer.addWidget(self.ratioPreview)
        self.previewContainer.addWidget(self.decimalPreview)
        self.previewContainer.addWidget(self.semitonePreview)
        self.previewContainer.addWidget(self.xyPreview) 
        self.decimalPreview.hide()
        self.semitonePreview.hide()
        self.xyPreview.hide()
        self.previewSelect.addItem('Ratio')
        self.previewSelect.addItem('Decimal')
        self.previewSelect.addItem('Semitone')
        self.previewSelect.addItem('XY')
        self.previewSelect.setCurrentIndex(0)

    def change_preview_display(self, display_type):
        if display_type == 'Decimal':
            self.ratioPreview.hide()
            self.decimalPreview.show() 
            self.semitonePreview.hide() 
            self.xyPreview.hide()      
        if display_type == 'Semitone':
            self.ratioPreview.hide()
            self.decimalPreview.hide() 
            self.semitonePreview.show() 
            self.xyPreview.hide()      
        if display_type == 'XY':
            self.ratioPreview.hide()
            self.decimalPreview.hide() 
            self.semitonePreview.hide() 
            self.xyPreview.show()      
        if display_type == 'Ratio':
            self.ratioPreview.show()
            self.decimalPreview.hide() 
            self.semitonePreview.hide() 
            self.xyPreview.hide()      

    def update_preview(self):
        self.set.bake()
        numerator = self.set.resources[self.active_idx].baked['numerators'][self.preview_idx]
        denominator = self.set.resources[self.active_idx].baked['denominators'][self.preview_idx]
        self.decimalPreview.setText('%.4f' % (numerator/denominator))
        self.semitonePreview.setText('%.4f' % (np.log2(numerator/denominator) * 12))
        self.ratioPreview.setText('%d/%d' % (numerator, denominator)) 
        self.xyPreview.update_plot(numerator, denominator)       

