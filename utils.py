import numpy as np
from PySide2 import QtGui


def QImageToCvMat(self, incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''

    incomingImage = incomingImage.convertToFormat(QtGui.QImage.Format.Format_RGB888)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.constBits()
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
    return arr
