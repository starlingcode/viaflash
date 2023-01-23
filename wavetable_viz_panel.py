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
        self.methods = {'contour': self.render_contour, 'wireframe': self.render_wireframe, '3dfft': self.render_3dfft}
        self.method = method
        fig = Figure(figsize=(6,6), facecolor='black')
        self.axes = fig.add_subplot(111, projection='3d')
        self.axes.set_axis_off()
        self.axes.set_facecolor('black')
        #self.axes.view_init(elev=85, azim=-50)
        self.render_plot(wavetable, method)
        super(Wavetable3D, self).__init__(fig)
    
    def update_plot(self, wavetable):
        self.axes.cla()
        self.axes.set_facecolor('black')
        self.render_plot(wavetable, self.method)
        self.draw()

    def render_plot(self, data, method):
        data = data.expand()
        self.methods[method](data)

    def render_contour(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, len(tables[0]), 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.set_axis_off()
        self.axes.contour(X, Y + 1, Z, zdir="y")

    def render_wireframe(self, tables):
        morph_size = len(tables)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, len(tables[0]), 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(tables)
        self.axes.set_axis_off()
        self.axes.plot_wireframe(X, Y, Z, rcount=morph_size, ccount=32, alpha=0.2, color=(240/256, 200/256, 50/256))

    def render_3dfft(self, tables):
        fft_table = []
        for table in tables:
            dcblock = np.asarray(table) - 16383
            fft_table.append(np.abs(np.fft.rfft(dcblock).real)[1:65])
        morph_size = len(fft_table)
        yrange = np.arange(0, morph_size, 1)
        xrange = np.arange(0, len(fft_table[0]), 1)
        X, Y = np.meshgrid(xrange, yrange)
        Z = np.array(fft_table)
        self.axes.set_axis_off()
        self.axes.contour(X, Y + 1, Z, zdir="y")
        # self.axes.plot_wireframe(X, Y, Z, rcount=morph_size, ccount=32, alpha=0.4, color=(240/256, 200/256, 50/256))


class Wavetable2D(FigureCanvasQTAgg):

    def __init__(self, wavetable, method, table_index):
        self.methods = {'waveform': self.render_waveform, 'fft': self.render_fft}
        self.method = method
        fig = Figure(figsize=(6,6), facecolor='black')
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        self.render_plot(wavetable, method, table_index)
        super(Wavetable2D, self).__init__(fig)
    
    def update_plot(self, wavetable, table_index):
        self.axes.cla()
        self.axes.set_facecolor('black')
        self.render_plot(wavetable, self.method, table_index)
        self.draw()

    def render_plot(self, data, method, table_index):
        data = data.expand()
        self.methods[method](data, table_index)

    def render_waveform(self, tables, table_index):
        self.axes.plot(tables[table_index], color=(240/256, 200/256, 50/256), linewidth=2)

    def render_fft(self, tables, table_index):
        dcblock = np.asarray(tables[table_index]) - 16383
        fft_reading = np.abs(np.fft.rfft(dcblock).real)[1:65]
        self.axes.bar(np.arange(len(fft_reading)), fft_reading, 1)
        

class WavetableVizPanel(QWidget):

    def __init__(self, parent):
        super(WavetableVizPanel, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.viz_methods = {'3dfft': '3d', 'contour': '3d', 'wireframe': '3d', 'waveform': '2d', 'fft': '2d'}
        self.is2d = False    
    
    def init_viz(self, method, table):
        self.d2viz = None
        self.d3viz = None
        self.method = method
        self.table = table
        self.create_viz()

    def update_plot(self, table, table_idx=0):
        self.table = table
        self.table_idx = table_idx
        if self.is2d:
            self.d2viz.update_plot(self.table, self.table_idx)
        else:
            self.d3viz.update_plot(self.table)

    def create_viz(self):
        if self.viz_methods[self.method] == '2d':
            self.is2d = True
            self.initd2()
        else:
            self.is2d = False
            self.initd3()

    def initd2(self):
        if self.d2viz:
            self.d2viz = Wavetable2D(self.table, self.method, 0)
            self.d2viz.show()
        else:
            self.d2viz = Wavetable2D(self.table, self.method, 0)
            self.layout.addWidget(self.d2viz)
            self.d2viz.show()

        if self.d3viz:
            self.d3viz.hide()

    def initd3(self):
        if self.d3viz:
            self.d3viz.Wavetable3D(self.table, self.method)
            self.d3viz.show()
        else:
            self.d3viz = Wavetable3D(self.table, self.method)
            self.layout.addWidget(self.d3viz)
            self.d3viz.show()

        if self.d2viz:
            self.d2viz.hide()

