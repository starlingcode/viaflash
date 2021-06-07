import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('viaflash.icns'))
    window = MainWindow()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())

