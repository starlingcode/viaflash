from PySide6.QtWidgets import QPushButton, QLabel, QSpinBox, QWidget, QHBoxLayout, QSizePolicy, QFrame
from PySide6.QtCore import QSize, Qt, QMimeData
from PySide6.QtGui import QDrag

from dragremovebuttons import DragButton, RemoveButton

class GateseqStepButton(QPushButton):

    def __init__(self):
        super().__init__()
        button_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button_size = QSize(10, 10)
        self.setSizePolicy(button_policy)
        self.setMinimumSize(button_size)
        self.setMaximumSize(button_size)
        self.setCheckable(True)

class GateseqSequenceEdit(QWidget):

    def __init__(self, parent, ruler_size=4):

        super().__init__(parent)

        self.parent_window = parent

        self.drag_button = DragButton(parent)
        self.label = QLabel()
        self.label.setText("PLZ SHOW UP")
        self.label.setAlignment(Qt.AlignCenter)
        self.length_entry = QSpinBox()
        self.remove = RemoveButton()
        self.layout = QHBoxLayout()

        self.layout.addWidget(self.drag_button)

        self.layout.addWidget(self.label)

        self.step_buttons = []
        self.step_dividers = []

        for i in range(0, 64):
            line = QFrame()
            line.setObjectName(u"line")
            line.setFrameShape(QFrame.VLine)
            line.setFrameShadow(QFrame.Sunken)
            self.step_dividers.append(line)
            self.layout.addWidget(line)

            new_button = GateseqStepButton()
            self.step_buttons.append(new_button)
            self.layout.addWidget(self.step_buttons[i])

        self.layout.insertSpacing(-1, 10)
        self.layout.addWidget(self.length_entry)
        self.layout.insertSpacing(-1, 10)
        self.layout.addWidget(self.remove)

        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        self.setLayout(self.layout)

        sp_retain = self.sizePolicy();
        sp_retain.setRetainSizeWhenHidden(True);
        self.setSizePolicy(sp_retain)
        self.reset_ruler(ruler_size)

        self.idx = 0
        self.unsorted_idx = 0

    def reset_ruler(self, size):
        for divider in self.step_dividers:
            divider.hide()
        for i in range(1, 64):
            if i % size == 0:
                self.step_dividers[i].show()

    def set_idx(self, idx):
        self.idx = idx
        self.drag_button.set_idx(idx)

