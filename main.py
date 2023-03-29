import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('/ui_resources/viaflash.icns'))
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

