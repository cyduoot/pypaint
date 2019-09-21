# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\code\pypaint\mainwindow.ui',
# licensing of 'd:\code\pypaint\mainwindow.ui' applies.
#
# Created: Fri Sep 20 17:20:09 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_cydPaintBoard(object):
    def setupUi(self, cydPaintBoard):
        cydPaintBoard.setObjectName("cydPaintBoard")
        cydPaintBoard.resize(130, 138)
        self.centralwidget = QtWidgets.QWidget(cydPaintBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 110, 73))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.board = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.board.setGeometry(QtCore.QRect(0, 0, 54, 12))
        self.board.setText("")
        self.board.setObjectName("board")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        cydPaintBoard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cydPaintBoard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 130, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        cydPaintBoard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(cydPaintBoard)
        self.statusbar.setObjectName("statusbar")
        cydPaintBoard.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(cydPaintBoard)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(cydPaintBoard)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(cydPaintBoard)
        QtCore.QMetaObject.connectSlotsByName(cydPaintBoard)

    def retranslateUi(self, cydPaintBoard):
        cydPaintBoard.setWindowTitle(QtWidgets.QApplication.translate("cydPaintBoard", "MainWindow", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("cydPaintBoard", "File", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("cydPaintBoard", "Open", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("cydPaintBoard", "Save", None, -1))

