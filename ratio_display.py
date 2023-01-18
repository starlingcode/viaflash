from PySide6.QtWidgets import QWidget

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from ui_ratio_display import Ui_ratioDisplay

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

class RatioDisplay(QWidget, Ui_ratioDisplay):
    
    def __init__(self, parent):
        super(RatioDisplay, self).__init__(parent)
        self.lissa_plot = Sync3RatioXY(1,1)
        self.xyLayout.addWidget(self.lissa_plot)
        self.update(numerator, denominator)

    def update(self):
        self.decimalData.setText('%.4f' % (numerator/denominator))
        self.semitonesData.setText('%.4f' % (np.log2(numerator/denominator) * 12))
        self.lissa_plot.update_plot(numerator, denominator)
