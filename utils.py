import numpy as np
from PIL import Image
import cv2


def imread(fileName):
    pimg = Image.open(fileName)
    img = np.asarray(pimg)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


def imwrite(fileName, img):
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image.save(fileName)


if __name__ == "__main__":
    i = imread("C:/Users/陈杨栋/Pictures/0b538deef01f3a29b0a3ae359525bc315d607ced.jpg")
    cv2.imshow("a", i)
    cv2.waitKey()
