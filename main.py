import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtGui import QImage, QPixmap
from mainwindow import Ui_cydPaintBoard
import cv2
from utils import imread, imwrite


class paintBoard(QMainWindow, Ui_cydPaintBoard):
    def __init__(self):
        super(paintBoard, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.scrollArea.setWidgetResizable(False)

    def fileOpen(self):
        self.statusbar.showMessage("open", 5000)
        fileName = QFileDialog.getOpenFileName(self, "Open an image file", "./", "Image files(*.bmp *.jpg *.png)")
        print(fileName)
        self.img = imread(fileName[0])
        image_height, image_width, image_channel = self.img.shape
        qimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        qimg = QImage(qimg.data, image_width, image_height,
                      QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)
        self.board.resize(pix.size())
        self.board.setPixmap(pix)
        self.scrollAreaWidgetContents.resize(pix.size())

    def fileSave(self):
        self.statusbar.showMessage("Save", 5000)
        fileName = QFileDialog.getSaveFileName(self, "Save an imagefile", "./", "Images (*.png *.bmp *.jpg)")
        print(fileName)
        imwrite(fileName[0], self.img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = paintBoard()
    w.show()
    sys.exit(app.exec_())
