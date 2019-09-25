import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainwindow import Ui_cydPaintBoard
from utils import imread, imwrite, showImage, changeCursor
from utils import penPress, penMove
from PySide2.QtCore import Qt


class paintBoard(QMainWindow, Ui_cydPaintBoard):
    def __init__(self):
        super(paintBoard, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.toolPen.clicked.connect(self.changePen)
        self.scrollArea.setWidgetResizable(False)
        self.thickness = 1
        self.curColor = (0, 0, 0)  # BGR
        self.lastPos = (0, 0)

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
        if self.toolPen.isChecked():
            print('pen')
            changeCursor(self, ":/cursors/penCur", 0, 16)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        globalPos = self.mapToGlobal(event.pos())
        labelPos = self.board.mapFromGlobal(globalPos)
        pos = (labelPos.x(), labelPos.y())
        print(labelPos)
        toolList = [self.toolPen.isChecked()]
        funcList = [penPress]
        if True in toolList:
            idx = toolList.index(True)
            funcList[idx](self, pos)

    def mouseMoveEvent(self, event):
        globalPos = self.mapToGlobal(event.pos())
        labelPos = self.board.mapFromGlobal(globalPos)
        pos = (labelPos.x(), labelPos.y())
        toolList = [self.toolPen.isChecked()]
        funcList = [penMove]
        if True in toolList:
            idx = toolList.index(True)
            funcList[idx](self, pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = paintBoard()
    w.show()
    sys.exit(app.exec_())
