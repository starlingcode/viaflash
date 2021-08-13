import sys
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QFile
from ui_sync3_scales import Ui_Sync3ScaleEdit

class Sync3ScaleWindow(QDialog):
    def __init__(self):
        super(Sync3ScaleWindow, self).__init__()
        self.ui = Ui_Sync3ScaleEdit()
        self.ui.setupUi(self)
        for i in range(0, 8):
            self.ui.comboBox.insertItem(i, str(i))
        
        
