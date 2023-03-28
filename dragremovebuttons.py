from PySide6.QtWidgets import QPushButton, QMessageBox
from PySide6.QtCore import QSize, QMimeData
from PySide6.QtGui import QDrag

class DragReorderButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(DragReorderButton, self).__init__(*args, **kwargs)
        self.configure_size()
        
    def configure_size(self):
        self.setFixedSize(QSize(15, 15))

class DragButton(DragReorderButton):
    def __init__(self, *args, **kwargs):
        super(DragButton, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.parent_window = args[0] # parent_window
        self.idx = 0

    def set_idx(self, idx):
        self.idx = idx

    def mouseMoveEvent(self, e):
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        self.parent_window.dragged_idx = self.idx

        dropAction = drag.exec()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        if not self.parent_window.sorted_flag:
            self.parent_window.handle_drop(self.idx)
        else:
            msgBox = QMessageBox()
            msgBox.setText("Reordering not supported in sorted mode")
            msgBox.exec()

class RemoveButton(DragReorderButton):
    def __init__(self, *args, **kwargs):
        super(RemoveButton, self).__init__(*args, **kwargs)

