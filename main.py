import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsPixmapItem, QGraphicsScene
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtCore import Qt
from mainwindow import Ui_cydPaintBoard
import cv2


class paintBoard(QMainWindow, Ui_cydPaintBoard):
    def __init__(self):
        super(paintBoard, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)

    def fileOpen(self):
        self.statusbar.showMessage("open", 5000)
        fileName = QFileDialog.getOpenFileName(self, "open an image file", "./", "Image files(*.bmp *.jpg *.png)")
        print(fileName)
        img = cv2.imread(fileName[0])
        image_height, image_width, image_channel = img.shape
        qimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qimg = QImage(qimg.data, image_width, image_height,
                      QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)
        self.item = QGraphicsPixmapItem(pix)
        self.item.setFlag(QGraphicsPixmapItem.ItemIgnoresTransformations)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
#        self.qrect = QRectF()
#        self.qrect = self.scene.itemsBoundingRect()
#        self.scene.setSceneRect(self.qrect)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.resize(image_width, image_height)

    def fileSave(self):
        self.statusbar.showMessage("Save", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = paintBoard()
    w.show()
    sys.exit(app.exec_())
