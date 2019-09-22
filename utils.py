import numpy as np
from PIL import Image
from PySide2 import QtGui


def imread(fileName):
    img = np.array(Image.open(fileName))
    if len(np.shape(img)) == 3:
        return img[:,:,::-1]
    else:
        return img