from PySide6.QtWidgets import QVBoxLayout, QSpinBox, QWidget
from PySide6.QtCore import Slot

import numpy as np
import matplotlib, mpld3
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


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


class WavetableVizPanel(QWidget):

    def __init__(self, parent):
        super(WavetableVizPanel, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tableIndex = QSpinBox(self)
        self.tableIndex.valueChanged.connect(self.tableIndex_valueChanged)
        self.layout.addWidget(self.tableIndex)

        self.viz_methods = {'surface': '3d', 'contour': '3d', 'wireframe': '3d', 'waveform': '2d', 'fft': '2d'}    

    # doesnt seem to automagically connect with on_tableIndex_valueChanged
    @Slot()
    def tableIndex_valueChanged(self):
        self.d2viz.update_plot(self.table, self.method, self.tableIndex.value())
    
    def init_viz(self, method, table):
        self.table = table
        self.d2viz = None
        self.d3viz = None
        self.method = method
        self.update_resource_ui(method, table)

    def update_resource_ui(self, method, table):
        self.table = table
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
            self.layout.addWidget(self.d2viz)
        self.tableIndex.show()

    def initd3(self, method):
        if self.d3viz:
            self.d3viz.update_plot(self.table, method)
            self.d3viz.show()
        else:
            self.d3viz = Wavetable3D(self.table, method)
            self.layout.addWidget(self.d3viz)
        self.tableIndex.hide()

    def deinitd2(self):
        if self.d2viz:
            self.d2viz.hide()

    def deinitd3(self):
        if self.d3viz:
            self.d3viz.hide()

