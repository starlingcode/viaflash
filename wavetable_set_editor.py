from PySide6.QtWidgets import QInputDialog, QMessageBox, QDialog
from PySide6.QtCore import Slot

import numpy as np
import matplotlib, mpld3
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

from ui_wavetable_set_editor import Ui_wavetableSetEditor
from ui_wavetable_browser import Ui_wavetableBrowser
from viatools.wavetables import Wavetable, WavetableSet
from via_resource_editor import ViaResourceEditor

import json


class Wavetable3D(FigureCanvasQTAgg):

    def __init__(self, wavetable=None, method=None):
        self.methods = {'contour': self.render_contour, 'wireframe': self.render_wireframe, 'surface': self.render_surface}
        fig = Figure(figsize=(6,6), facecolor='black')
        self.axes = fig.add_subplot(111, projection='3d')
        self.axes.set_axis_off()
        self.axes.set_facecolor('black')
        #self.axes.view_init(elev=85, azim=-50)
        self.render_plot(wavetable.expand(), method)
        super(Wavetable3D, self).__init__(fig)
    
    def update_plot(self, wavetable, method):
        self.axes.cla()
        self.axes.set_facecolor('black')
        self.render_plot(wavetable.expand(), method)
        self.draw()

    def render_plot(self, data, method):
        self.methods[method](data)

    def render_contour(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, 512, 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.set_axis_off()
        self.axes.contour(X, Y + 1, Z, zdir="y")

    def render_wireframe(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, 512, 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.set_axis_off()
        self.axes.plot_wireframe(X, Y, Z, rcount=morph_size, ccount=256, alpha=0.4, color=(240/256, 200/256, 50/256))

    def render_surface(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, 512, 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.set_axis_off()
        self.axes.plot_surface(X, Y, Z, rcount=morph_size, ccount=256, alpha=0.8, cmap=cm.coolwarm)


class Wavetable2D(FigureCanvasQTAgg):

    def __init__(self, wavetable, method, table_index):
        self.methods = {'waveform': self.render_waveform, 'fft': self.render_fft}
        fig = Figure(figsize=(6,6), facecolor='black')
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        self.render_plot(wavetable.expand(), method, table_index)
        super(Wavetable2D, self).__init__(fig)
    
    def update_plot(self, wavetable, method, table_index):
        self.axes.cla()
        self.axes.set_facecolor('black')
        self.render_plot(wavetable.expand(), method, table_index)
        self.draw()

    def render_plot(self, data, method, table_index):
        self.methods[method](data, table_index)

    def render_waveform(self, tables, table_index):
        self.axes.plot(tables[table_index], color=(240/256, 200/256, 50/256), linewidth=2)

    def render_fft(self, tables, table_index):
        fft_reading = np.abs(np.fft.rfft(np.array(tables[table_index]) - 16384).real)
        fft_reading = np.log(fft_reading[1:65])
        self.axes.bar(np.arange(64), fft_reading, 1)
        self.axes.set_ylim(0, 16)


class WavetableViz():

    @Slot()
    def on_displayType_activated(self):
        self.update_resource_ui()

    @Slot()
    def on_tableIndex_valueChanged(self):
        self.d2viz.update_plot(self.table, self.displayType.currentText(), self.tableIndex.value())
    
    def init_viz(self, table):
        self.table = table
        self.viz_methods = {'surface': '3d', 'contour': '3d', 'wireframe': '3d', 'waveform': '2d', 'fft': '2d'}    
        self.d2viz = None
        self.d3viz = None
        if len(table.expand()) <= 1:
            self.viz_methods = {'waveform': '2d', 'fft': '2d'}    
        for item in self.viz_methods:
            self.displayType.insertItem(-1, item)
        self.update_resource_ui()

    def update_resource_ui(self):
        method = self.displayType.currentText()
        if self.viz_methods[method] == '2d':
            self.deinitd3()
            self.initd2(method)
        else:
            self.deinitd2()
            self.initd3(method)

    def initd2(self, method):
        self.tableIndex.setMaximum(len(self.table.expand()) - 1)
        table_idx = self.tableIndex.value()
        if self.d2viz:
            self.d2viz.update_plot(self.table, method, table_idx)
            self.d2viz.show()
        else:
            self.d2viz = Wavetable2D(self.table, method, table_idx)
            self.tableViz.addWidget(self.d2viz)
        self.tableIndex.show()

    def initd3(self, method):
        if self.d3viz:
            self.d3viz.update_plot(self.table, method)
            self.d3viz.show()
        else:
            self.d3viz = Wavetable3D(self.table, method)
            self.tableViz.addWidget(self.d3viz)
        self.tableIndex.hide()

    def deinitd2(self):
        if self.d2viz:
            self.d2viz.hide()

    def deinitd3(self):
        if self.d3viz:
            self.d3viz.hide()

    def switch_table(self): 
        self.viz_methods = {'surface': '3d', 'contour': '3d', 'wireframe': '3d', 'waveform': '2d', 'fft': '2d'}    
        if len(self.table.expand()) <= 1:
            self.viz_methods = {'waveform': '2d', 'fft': '2d'}    
        self.displayType.clear()
        for item in self.viz_methods:
            self.displayType.insertItem(-1, item)
        self.update_resource_ui()



class WavetableBrowser(QDialog, Ui_wavetableBrowser, WavetableViz):
    def __init__(self, table_file, slope_file, slug, max_table_size):
        super().__init__()
        self.setupUi(self)
        self.init_table_dict(table_file, slope_file)
        self.table_file = table_file
        self.slope_file = slope_file
        self.max_table_size = max_table_size
        if self.table_dict[slug]['type'] == 'slope_pair':
            self.slopePair.setChecked(True)
            self.type = 'slope_pair'
        else:
            self.cycle.setChecked(True)
            self.type = 'cycle'
        self.update_type()
        self.table_size = self.table_dict[slug]['size']
        self.update_size()
        self.tableSize.setCurrentIndex(self.tableSize.findText(str(self.table_size)))
        self.selectTable.setCurrentIndex(self.selectTable.findText(slug))
        self.tableSizeWarning.setText('(the first %d will be used)' % max_table_size) 
        self.init_viz(Wavetable(self.table_file, slug, self.slope_file, max_table_size)
)

    @Slot() 
    def on_slopePair_clicked(self):
        self.type = 'slope_pair'
        self.update_type()

    @Slot() 
    def on_cycle_clicked(self):
        self.type = 'cycle'
        self.update_type()

    @Slot() 
    def on_tableSize_activated(self):
        try: 
            self.table_size = int(self.tableSize.currentText())
            self.update_size()
        except:
            pass

    @Slot()
    def on_selectTable_activated(self):
        self.table = Wavetable(self.table_file, self.selectTable.currentText(), self.slope_file, self.max_table_size)
        self.switch_table()

    def init_table_dict(self, table_file, slope_file):
        self.table_dict = {}
        with open(slope_file) as infile:
            raw_slopes = json.load(infile)
        with open(table_file) as infile:
            raw_tables = json.load(infile)
            for table in raw_tables:
                self.table_dict[table] = {}
                attack_samples = raw_slopes[raw_tables[table][0]]
                self.table_dict[table]['size'] = len(attack_samples)
                if attack_samples[0][0] == 0 and attack_samples[0][-1] == 32767:
                    self.table_dict[table]['type'] = 'slope_pair'
                else:
                    self.table_dict[table]['type'] = 'cycle'
                
    def update_type(self):
        self.selectTable.clear()
        self.tableSize.clear()
        valid_sizes = set()
        valid_tables = []
        for table, properties in self.table_dict.items():
            if properties['type'] == self.type:
                valid_sizes.add(properties['size'])
                valid_tables.append(table)
        valid_size_list = sorted(valid_sizes)
        for size in valid_size_list:
            self.tableSize.insertItem(-1, str(size))
            self.table_size = size
        for table in valid_tables:
            self.selectTable.insertItem(-1, table)
            
    def update_size(self):
        self.selectTable.clear()
        valid_tables = []
        for table, properties in self.table_dict.items():
            if properties['type'] == self.type and properties['size'] == self.table_size:
                valid_tables.append(table)
        for table in valid_tables:
            self.selectTable.insertItem(-1, table)


class WavetableEditor(ViaResourceEditor, WavetableViz):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)
        self.style_text = style_text

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug
        self.size_limit_data = {'table_size': 9}
        self.set = WavetableSet(resource_dir, slug, table_file, slope_file)
        self.set_slug = slug
        self.slope_file = slope_file
        self.table_file = table_file

        self.update_resource_sets()
        self.tableViz.removeItem(self.vizSpacer)
        self.init_viz(self.set.resources[0])
        self.update_resources()

        for slot_num, label in enumerate(self.slot_labels):
            eval('self.slot%d' % (slot_num+1)).setText(label)
            eval('self.slot%d' % (slot_num+1)).clicked.connect(lambda state=True, x=slot_num: self.switch_slot(x))
        
        for slot_num in range(len(self.slot_labels), 25):
            eval('self.slot%d' % (slot_num+1)).hide()

        self.slot1.setChecked(True)
        self.switch_slot(0)

# Edit wavetable recipe

    @Slot()
    def on_openBrowser_clicked(self):
        self.launch_browser()
        

# Override set editor base class methods

    def launch_browser(self):
        self.browser = WavetableBrowser(self.table_file, self.slope_file, self.set.resources[self.active_idx].slug, self.size_limit_data['table_size'])
        self.browser.swapTable.clicked.connect(self.swap_table)
        self.browser.close.clicked.connect(self.close_browser)
        self.browser.setStyleSheet(self.style_text)
        self.browser.exec()

    def swap_table(self):
        slug = self.browser.selectTable.currentText()
        self.set.replace_resource(slug, self.active_idx)
        self.switch_slot(self.active_idx)
        self.browser.accept()
    
    def close_browser(self):
        self.browser.accept()

 
    def update_resource_selection(self, slug):
        self.tableName.setText(slug)
        self.table = Wavetable(self.table_file, slug, self.slope_file, self.size_limit_data['table_size']) 
        self.switch_table()
        
    def update_resources(self):
        return


class ScannerWavetableEditor(WavetableEditor, Ui_wavetableSetEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        x_slot_labels = []
        y_slot_labels = []
        for mode in range(1, 9):
            x_slot_labels.append('X-%d' % mode)
            y_slot_labels.append('Y-%d' % mode)
        self.slot_labels = x_slot_labels + y_slot_labels 
        self.size_limit_data = {'table_size': 5, 'memory_footprint': 160000}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 

class MetaWavetableEditor(WavetableEditor, Ui_wavetableSetEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        a_slot_labels = []
        e_slot_labels = []
        s_slot_labels = []
        for mode in range(1, 9):
            a_slot_labels.append('A-%d' % mode)
            e_slot_labels.append('E-%d' % mode)
            s_slot_labels.append('S-%d' % mode)
        self.slot_labels = a_slot_labels + e_slot_labels + e_slot_labels
        self.slot_labels.append('Drum')
        self.size_limit_data = {'table_size': 9, 'memory_footprint': 160000}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 


class SyncWavetableEditor(WavetableEditor, Ui_wavetableSetEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        I_slot_labels = []
        II_slot_labels = []
        III_slot_labels = []
        IV_slot_labels = []
        G_slot_labels = []
        for mode in range(1, 5):
            I_slot_labels.append('I-%d' % mode)
            II_slot_labels.append('II-%d' % mode)
            III_slot_labels.append('III-%d' % mode)
            IV_slot_labels.append('IV-%d' % mode)
            G_slot_labels.append('G-%d' % mode)
        self.slot_labels = I_slot_labels + II_slot_labels + III_slot_labels + IV_slot_labels + G_slot_labels
        self.size_limit_data = {'table_size': 9, 'memory_footprint': 116000}
        super().__init__(resource_dir, remote_resources, slug, style_text, table_file, slope_file) 


