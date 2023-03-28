from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

class DragReorderButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(DragReorderButton, self).__init__(*args, **kwargs)
        self.configure_size()
        
    def configure_size(self):
        self.setFixedSize(QSize(15, 15))

class DragButton(DragReorderButton):
    def __init__(self, *args, **kwargs):
        super(DragButton, self).__init__(*args, **kwargs)

class RemoveButton(DragReorderButton):
    def __init__(self, *args, **kwargs):
        super(RemoveButton, self).__init__(*args, **kwargs)

