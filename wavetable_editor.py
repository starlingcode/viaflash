from PySide6.QtWidgets import QInputDialog, QMessageBox 
from PySide6.QtCore import Slot

import numpy as np
import matplotlib, mpld3
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

from ui_meta_wavetable_editor import Ui_metaWavetableEditor
from ui_scanner_wavetable_editor import Ui_scannerWavetableEditor
from ui_sync_wavetable_editor import Ui_syncWavetableEditor
from viatools.wavetables import Wavetable, WavetableSet
from via_resource_editor import ViaResourceEditor


class Wavetable3D(FigureCanvasQTAgg):

    def __init__(self, wavetable=None, method=None):
        self.methods = {'contour': self.render_contour, 'wireframe': self.render_wireframe, 'surface': self.render_surface}
        fig = Figure(figsize=(1,1), facecolor='black')
        self.axes = fig.add_subplot(111, projection='3d')
        self.axes.set_axis_off()
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
        fig = Figure(figsize=(1,1), facecolor='black')
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
        fft_reading = np.abs(np.fft.rfft(tables[table_index]))
        fft_reading = np.log(fft_reading[:128])
        self.axes.plot(fft_reading)

class WavetableEditor(ViaResourceEditor):
    def __init__(self):
        super().__init__() 

# Edit wavetable recipe

    @Slot()
    def on_openBrowser_clicked(self):
        return

    @Slot()
    def on_displayType_activated(self):
        self.update_resource_ui()

    @Slot()
    def on_tableIndex_valueChanged(self):
        self.d2viz.update_plot(self.set.resources[self.active_idx], self.displayType.currentText(), self.tableIndex.value())

# Override set editor base class methods

    def init_viz(self):
        self.viz_methods = {'surface': '3d', 'contour': '3d', 'wireframe': '3d', 'waveform': '2d', 'fft': '2d'}    
        self.d2viz = None
        self.d3viz = None
        for item in self.viz_methods:
            self.displayType.insertItem(-1, item)
        self.update_resource_ui()
 
    def update_resource_selection(self, name):
        self.tableName.setText(name)
        
    def update_resources(self):
        return

    def update_resource_ui(self):
        method = self.displayType.currentText()
        if self.viz_methods[method] == '2d':
            self.deinitd3()
            self.initd2(method)
        else:
            self.deinitd2()
            self.initd3(method)
        

# Visualization window

    def initd2(self, method):
        self.tableIndex.setMaximum(len(self.set.resources[self.active_idx].expand()) - 1)
        table_idx = self.tableIndex.value()
        if self.d2viz:
            self.d2viz.update_plot(self.set.resources[self.active_idx], method, table_idx)
            self.d2viz.show()
        else:
            self.d2viz = Wavetable2D(self.set.resources[self.active_idx], method, table_idx)
            self.tableViz.addWidget(self.d2viz)
        self.tableIndex.show()

    def initd3(self, method):
        if self.d3viz:
            self.d3viz.update_plot(self.set.resources[self.active_idx], method)
            self.d3viz.show()
        else:
            self.d3viz = Wavetable3D(self.set.resources[self.active_idx], method)
            self.tableViz.addWidget(self.d3viz)
        self.tableIndex.hide()

    def deinitd2(self):
        if self.d2viz:
            self.d2viz.hide()

    def deinitd3(self):
        if self.d3viz:
            self.d3viz.hide()


class ScannerWavetableEditor(WavetableEditor, Ui_scannerWavetableEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug
        size_limit_data = {'table_size': 5}
        self.set = WavetableSet(resource_dir, slug, table_file, slope_file, size_limit_data)

        self.update_resource_sets()

        self.init_viz()

        self.update_resources()

        self.slot1.setChecked(True)
        self.switch_slot(0)

class MetaWavetableEditor(WavetableEditor, Ui_metaWavetableEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = WavetableSet(resource_dir, slug, table_file, slope_file)

        self.update_resource_sets()
        self.init_viz()
        self.update_resources()

        self.slot1.setChecked(True)
        self.switch_slot(0)


class SyncWavetableEditor(WavetableEditor, Ui_syncWavetableEditor):
    def __init__(self, resource_dir='./', remote_resources = {}, slug='original', style_text="", table_file='./tables.json', slope_file='./slopes.json'):
        super().__init__() 
        self.setupUi(self)
        self.setStyleSheet(style_text)

        self.remote_resources = remote_resources
        # TODO check if new remote resource or set collides with existing local slug

        self.set = WavetableSet(resource_dir, slug, table_file, slope_file)

        self.update_resource_sets()
        self.init_viz()
        self.update_resources()

        self.slot1.setChecked(True)
        self.switch_slot(0)


