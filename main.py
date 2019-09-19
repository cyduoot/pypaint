import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_cydPaintBoard


class paintBoard(QMainWindow, Ui_cydPaintBoard):
    def __init__(self):
        super(paintBoard, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)

    def fileOpen(self):
        self.statusbar.showMessage("open", 5000)

    def fileSave(self):
        self.statusbar.showMessage("Save", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = paintBoard()
    w.show()
    sys.exit(app.exec_())
