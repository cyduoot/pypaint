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


def changeRubberCursor(ui):
    img = np.ones((ui.thickness, ui.thickness, 4), np.uint8) * 255
    for i in range(ui.thickness):
        for j in range(ui.thickness):
            img[i, j, 3] = 0
    cv2.circle(img, (ui.thickness//2, ui.thickness//2), ui.thickness//2, (255, 255, 255, 255), -1)
    cv2.circle(img, (ui.thickness//2, ui.thickness//2), ui.thickness//2, (0, 0, 0, 255), 1)
    image_height, image_width, image_channel = img.shape
    qimg = QImage()
    timg = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    qimg = QImage(timg.data, image_width, image_height, image_width*image_channel, QImage.Format_RGBA8888)
    myPix = QPixmap.fromImage(qimg)
    myCur = QCursor(myPix, -1, -1)
    ui.board.setCursor(myCur)


def penPress(ui, pos):
    cv2.circle(ui.img, pos, ui.thickness//2, ui.curColor, -1)
    ui.lastPos = pos
    showImage(ui)


def penMove(ui, pos):
    cv2.line(ui.img, ui.lastPos, pos, ui.curColor, ui.thickness)
    ui.lastPos = pos
    showImage(ui)


def rubberPress(ui, pos):
    cv2.circle(ui.img, pos, ui.thickness//2, ui.rightColor, -1)
    ui.lastPos = pos
    showImage(ui)


def rubberMove(ui, pos):
    cv2.line(ui.img, ui.lastPos, pos, ui.rightColor, ui.thickness)
    ui.lastPos = pos
    showImage(ui)


def linePress(ui, pos):
    ui.lastPos = pos
    print(pos)


def lineMove(ui, pos):
    timg = ui.img.copy()
    cv2.line(ui.img, ui.lastPos, pos, ui.curColor, ui.thickness)
    showImage(ui)
    ui.img = timg.copy()


def lineRelease(ui, pos):
    cv2.line(ui.img, ui.lastPos, pos, ui.curColor, ui.thickness)
    showImage(ui)


def recPress(ui, pos):
    ui.lastPos = pos
    print(pos)


def recMove(ui, pos):
    timg = ui.img.copy()
    cv2.rectangle(ui.img, ui.lastPos, pos, ui.curColor, ui.thickness)
    showImage(ui)
    ui.img = timg.copy()


def recRelease(ui, pos):
    cv2.rectangle(ui.img, ui.lastPos, pos, ui.curColor, ui.thickness)
    showImage(ui)


def circlePress(ui, pos):
    ui.lastPos = pos
    print(pos)


def calc(p1, p2):
    center = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    radius = (abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
    return center, radius


def circleMove(ui, pos):
    timg = ui.img.copy()
    center, radius = calc(ui.lastPos, pos)
    cv2.ellipse(ui.img, center, radius, 0, 0, 360, ui.curColor, ui.thickness)
    showImage(ui)
    ui.img = timg.copy()


def circleRelease(ui, pos):
    center, radius = calc(ui.lastPos, pos)
    cv2.ellipse(ui.img, center, radius, 0, 0, 360, ui.curColor, ui.thickness)
    showImage(ui)


def bucket(ui, pos):
    h, w = ui.img.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv2.floodFill(ui.img, mask, pos, ui.curColor, (0, 0, 0), (0, 0, 0), cv2.FLOODFILL_FIXED_RANGE)
    showImage(ui)


if __name__ == "__main__":
    i = imread("C:/Users/陈杨栋/Pictures/0b538deef01f3a29b0a3ae359525bc315d607ced.jpg")
    cv2.imshow("a", i)
    cv2.waitKey()

import paint_rc
