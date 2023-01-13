from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

class SlotButton(QPushButton):
	def __init__(self, *args, **kwargs):
		super(SlotButton, self).__init__(*args, **kwargs)
		#self.setFixedSize(QSize(30, 30))

class Slot1Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot1Button, self).__init__(*args, **kwargs)

class Slot2Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot2Button, self).__init__(*args, **kwargs)

class Slot3Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot3Button, self).__init__(*args, **kwargs)

class Slot4Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot4Button, self).__init__(*args, **kwargs)

class Slot5Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot5Button, self).__init__(*args, **kwargs)

class Slot6Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot6Button, self).__init__(*args, **kwargs)

class Slot7Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot7Button, self).__init__(*args, **kwargs)

class Slot8Button(SlotButton):
	def __init__(self, *args, **kwargs):
		super(Slot8Button, self).__init__(*args, **kwargs)
