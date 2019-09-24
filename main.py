import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainwindow import Ui_cydPaintBoard
import cv2
from utils import imread, imwrite, showImage, changeCursor
from PySide2.QtCore import Qt


class paintBoard(QMainWindow, Ui_cydPaintBoard):
    def __init__(self):
        super(paintBoard, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.toolPen.clicked.connect(self.changePen)
        self.scrollArea.setWidgetResizable(False)

    def fileOpen(self):
        self.statusbar.showMessage("open", 5000)
        fileName = QFileDialog.getOpenFileName(self, "Open an image file", "./", "Image files(*.bmp *.jpg *.png)")
        print(fileName)
        self.img = imread(fileName[0])
        showImage(self)

    def fileSave(self):
        self.statusbar.showMessage("Save", 5000)
        fileName = QFileDialog.getSaveFileName(self, "Save an imagefile", "./", "Images (*.png *.bmp *.jpg)")
        print(fileName)
        imwrite(fileName[0], self.img)

    def changePen(self):
        if self.toolPen.isChecked:
            print('pen')
            changeCursor(self, ":/cursors/penCur", 0, 16)
            self.toolPen.isChecked = False
        else:
            self.board.setCursor(Qt.ArrowCursor)
            self.toolPen.isChecked = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = paintBoard()
    w.show()
    sys.exit(app.exec_())
