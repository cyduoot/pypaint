# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\code\pypaint\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cydPaintBoard(object):
    def setupUi(self, cydPaintBoard):
        cydPaintBoard.setObjectName("cydPaintBoard")
        cydPaintBoard.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(cydPaintBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 341, 321))
        self.graphicsView.setObjectName("graphicsView")
        cydPaintBoard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(cydPaintBoard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        _translate = QtCore.QCoreApplication.translate
        cydPaintBoard.setWindowTitle(_translate("cydPaintBoard", "MainWindow"))
        self.menuFile.setTitle(_translate("cydPaintBoard", "File"))
        self.actionOpen.setText(_translate("cydPaintBoard", "Open"))
        self.actionSave.setText(_translate("cydPaintBoard", "Save"))
