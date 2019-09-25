import numpy as np
from PIL import Image
import cv2
from PySide2.QtGui import QImage, QPixmap, QCursor


def imread(fileName):
    pimg = Image.open(fileName)
    img = np.asarray(pimg)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


def imwrite(fileName, img):
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image.save(fileName)


def showImage(ui):
    image_height, image_width, image_channel = ui.img.shape
    qimg = QImage()
    timg = cv2.cvtColor(ui.img, cv2.COLOR_BGR2RGB)
    qimg = QImage(timg.data, image_width, image_height, image_width*image_channel, QImage.Format_RGB888)
    pix = QPixmap.fromImage(qimg)
    ui.board.resize(pix.size())
    ui.board.setPixmap(pix)
    ui.scrollAreaWidgetContents.resize(pix.size())


def changeCursor(ui, icon, hotX, hotY):
    myPix = QPixmap(icon)
    myCur = QCursor(myPix, hotX, hotY)
    ui.board.setCursor(myCur)


def penPress(ui, pos):
    cv2.circle(ui.img, pos, ui.thickness//2, ui.curColor, -1)
    ui.lastPos = pos
    showImage(ui)


def penMove(ui, pos):
    cv2.line(ui.img, ui.lastPos, pos, ui.curColor, ui.thickness)
    ui.lastPos = pos
    showImage(ui)


if __name__ == "__main__":
    i = imread("C:/Users/陈杨栋/Pictures/0b538deef01f3a29b0a3ae359525bc315d607ced.jpg")
    cv2.imshow("a", i)
    cv2.waitKey()

import paint_rc
