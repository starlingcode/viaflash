from PySide6.QtWidgets import QPushButton, QLabel, QSpinBox, QWidget, QHBoxLayout, QSizePolicy
from PySide6.QtCore import QSize

# QLabel -> 64 Buttons -> Seq Lenngth Selector

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

		for i in range(0, 40):
			new_button = QPushButton()
			new_button.setSizePolicy(button_policy)
			new_button.setMinimumSize(button_size)
			new_button.setMaximumSize(button_size)
			self.step_buttons.append(new_button)
			self.layout.addWidget(self.step_buttons[i])

		self.layout.addWidget(self.length_entry)

		self.layout.setContentsMargins(0,0,0,0)

		self.setLayout(self.layout)



