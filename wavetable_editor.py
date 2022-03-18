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

    def __init__(self, wavetable, method):
        self.methods = {'contour': self.render_contour, 'wireframe': self.render_wireframe, 'surface': self.render_surface}
        fig = Figure(figsize=(1,1), facecolor='black')
        self.axes = fig.add_subplot(111, projection='3d')
        self.axes.axis('off')
        self.axes.view_init(elev=85, azim=-50)
        self.render_plot(wavetable.expand(), method)
        super(WavetableSurface, self).__init__(fig)
    
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
        self.axes.contour(X, Y + 1, Z, zdir="y")

    def render_wireframe(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, 512, 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.plot_wireframe(X, Y, Z, rcount=morph_size, ccount=256, alpha=0.4, color=(240/256, 200/256, 50/256))

    def render_surface(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, 512, 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.plot_surface(X, Y, Z, rcount=morph_size, ccount=256, alpha=0.8, cmap=cm.coolwarm)

class Wavetable2D(FigureCanvasQTAgg):


    def __init__(self, wavetable, method, table_index):
        self.methods = {'contour': self.render_waveform, 'wireframe': self.render_fft}
        fig = Figure(figsize=(1,1), facecolor='black')
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        self.axes.view_init(elev=85, azim=-50)
        self.render_plot(wavetable.expand(), method, table_index)
        super(Wavetable2D, self).__init__(fig)
    
    def update_plot(self, wavetable, method, table_index):
        self.axes.cla()
        self.axes.set_facecolor('black')
        self.render_plot(wavetable.expand(), method, table_index)
        self.draw()

    def render_plot(self, data, method, table_index):
        self.methods[method](data, index)

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
        method = self.displayType.getCurrentText()
        if method in self.d2_methods:
            self.deinitd3()
            self.initd2(self.set[active_idx], self.method, table_idx)
        elif method in self.d3_methods:
            self.deinitd2()
            self.initd3(self.method)

    @Slot()
    def on_indexSelector_activated(self):
        return

# Override set editor base class methods
 
    def update_resource_selection(self, name):
        self.tableName.setText(name)
        
    def update_resources(self):
        return

    def update_resource_ui(self):

        return

# Visualization window

    def initd2(self, index):
        #self.tableIndex.setMaximum(
        table_idx = self.tableIndex.value()
        self.initd2(self.set[active_idx], self.method, table_idx)
        return

    def initd3(self, wavetable, name):
        return

    def deinitd2(self):
        return

    def deinitd3(self):
        return



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
        self.update_resources()

        self.slot1.setChecked(True)
        self.switch_slot(0)


