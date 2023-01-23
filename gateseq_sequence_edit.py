from PySide6.QtWidgets import QPushButton, QLabel, QSpinBox, QWidget, QHBoxLayout, QSizePolicy, QFrame
from PySide6.QtCore import QSize

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

	def __init__(self):

		super().__init__()

		self.label = QLabel()
		self.label.setText("PLZ SHOW UP")
		self.length_entry = QSpinBox()
		self.layout = QHBoxLayout()

		self.layout.addWidget(self.label)

		button_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		button_size = QSize(10, 10)

		self.step_buttons = []

		for i in range(0, 64):
			if i % 4 == 0:
				line = QFrame()
				line.setObjectName(u"line")
				line.setFrameShape(QFrame.VLine)
				line.setFrameShadow(QFrame.Sunken)
				self.layout.addWidget(line)

			new_button = GateseqStepButton()
			self.step_buttons.append(new_button)
			self.layout.addWidget(self.step_buttons[i])

		self.layout.addWidget(self.length_entry)

		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)

		self.setLayout(self.layout)



