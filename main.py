import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog
from mainwindow import Ui_cydPaintBoard
from utils import imread, imwrite, showImage, changeCursor, changeRubberCursor
from utils import penPress, penMove
from utils import rubberPress, rubberMove
from PySide2.QtCore import Qt
from inputdialog import InputDialog
import numpy as np


class paintBoard(QMainWindow, Ui_cydPaintBoard):
    def __init__(self):
        super(paintBoard, self).__init__()
        self.setupUi(self)
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionChange_Board_Size.triggered.connect(self.changeSize)
        self.toolPen.clicked.connect(self.changePen)
        self.toolRubber.clicked.connect(self.changeRubber)
        self.toolBucket.clicked.connect(self.changeBucket)
        self.toolLine.clicked.connect(self.changeLine)
        self.toolRec.clicked.connect(self.changeRec)
        self.toolCircle.clicked.connect(self.changeCircle)
        self.lineEdit.textChanged.connect(self.changeThickness)
        self.lColor.clicked.connect(self.changeLeftColor)
        self.rColor.clicked.connect(self.changeRightColor)
        self.scrollArea.setWidgetResizable(False)
        self.thickness = 1
        self.curColor = (0, 0, 0)  # BGR
        self.leftColor = (0, 0, 0)
        self.rightColor = (255, 255, 255)
        self.lastPos = (0, 0)

    def refreshTools(self):
        self.toolPen.setChecked(False)
        self.toolCircle.setChecked(False)
        self.toolBucket.setChecked(False)
        self.toolRubber.setChecked(False)
        self.toolRec.setChecked(False)
        self.toolLine.setChecked(False)

    def newFile(self):
        dialog = InputDialog(parent=self)
        width, height = (100, 100)
        if dialog.exec():
            width, height = dialog.getInputs()
        if width.isdigit():
            width = int(width)
        if height.isdigit():
            height = int(height)
        self.img = np.ones((height, width, 3), np.uint8) * 255
        showImage(self)

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

    def changeSize(self):
        dialog = InputDialog(parent=self)
        image_height, image_width, image_channel = self.img.shape
        width, height = (image_width, image_height)
        if dialog.exec():
            width, height = dialog.getInputs()
        width = int(width)
        height = int(height)
        tmpimg = self.img
        image_height, image_width, image_channel = tmpimg.shape
        self.img = np.ones((height, width, 3), np.uint8) * 255
        for i in range(height):
            for j in range(width):
                for k in range(3):
                    if (i < image_height) and (j < image_width):
                        self.img[i, j, k] = tmpimg[i, j, k]
        showImage(self)

    def changePen(self):
        if self.toolPen.isChecked():
            self.refreshTools()
            self.toolPen.setChecked(True)
            print('pen')
            changeCursor(self, ":/cursors/penCur", 0, 16)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def changeRubber(self):
        if self.toolRubber.isChecked():
            self.refreshTools()
            self.toolRubber.setChecked(True)
            print('rubber')
            changeRubberCursor(self)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def changeBucket(self):
        if self.toolBucket.isChecked():
            self.refreshTools()
            self.toolBucket.setChecked(True)
            print('bucket')
            changeCursor(self, ":/cursors/bucketCur", 0, 16)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def changeLine(self):
        if self.toolLine.isChecked():
            self.refreshTools()
            self.toolLine.setChecked(True)
            print('line')
            self.board.setCursor(Qt.CrossCursor)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def changeRec(self):
        if self.toolRec.isChecked():
            self.refreshTools()
            self.toolRec.setChecked(True)
            print('rec')
            self.board.setCursor(Qt.CrossCursor)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def changeCircle(self):
        if self.toolCircle.isChecked():
            self.refreshTools()
            self.toolCircle.setChecked(True)
            print('circle')
            self.board.setCursor(Qt.CrossCursor)
        else:
            self.board.setCursor(Qt.ArrowCursor)

    def changeThickness(self):
        text = self.lineEdit.text()
        if text.isdigit():
            t = int(text)
            if t <= 50:
                self.thickness = t

    def changeLeftColor(self):
        cl = QColorDialog.getColor()
        h = cl.name()
        self.lColor.setStyleSheet("background-color:%s" % h)
        self.leftColor = (int(h[5:7], 16), int(h[3:5], 16), int(h[1:3], 16))

    def changeRightColor(self):
        cl = QColorDialog.getColor()
        h = cl.name()
        self.rColor.setStyleSheet("background-color:%s" % h)
        self.rightColor = (int(h[5:7], 16), int(h[3:5], 16), int(h[1:3], 16))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.curColor = self.leftColor
        elif event.button() == Qt.RightButton:
            self.curColor = self.rightColor
        globalPos = self.mapToGlobal(event.pos())
        labelPos = self.board.mapFromGlobal(globalPos)
        pos = (labelPos.x(), labelPos.y())
        print(labelPos)
        toolList = [self.toolPen.isChecked(), self.toolRubber.isChecked()]
        funcList = [penPress, rubberPress]
        if True in toolList:
            idx = toolList.index(True)
            funcList[idx](self, pos)

    def mouseMoveEvent(self, event):
        globalPos = self.mapToGlobal(event.pos())
        labelPos = self.board.mapFromGlobal(globalPos)
        pos = (labelPos.x(), labelPos.y())
        toolList = [self.toolPen.isChecked(), self.toolRubber.isChecked()]
        funcList = [penMove, rubberMove]
        if True in toolList:
            idx = toolList.index(True)
            funcList[idx](self, pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = paintBoard()
    w.show()
    sys.exit(app.exec_())
