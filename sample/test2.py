# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jul  8 10:31:32 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.action1 = QtGui.QPushButton(self.centralwidget)
        self.action1.setGeometry(QtCore.QRect(30, 350, 90, 27))
        self.action1.setObjectName(_fromUtf8("action1"))
        self.action2 = QtGui.QPushButton(self.centralwidget)
        self.action2.setGeometry(QtCore.QRect(140, 350, 90, 27))
        self.action2.setObjectName(_fromUtf8("action2"))
        self.action4 = QtGui.QPushButton(self.centralwidget)
        self.action4.setGeometry(QtCore.QRect(360, 350, 90, 27))
        self.action4.setObjectName(_fromUtf8("action4"))
        self.action3 = QtGui.QPushButton(self.centralwidget)
        self.action3.setGeometry(QtCore.QRect(250, 350, 90, 27))
        self.action3.setObjectName(_fromUtf8("action3"))
        self.webView = QtWebKit.QWebView()
        self.webView.settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://www.google.com")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.webView.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.webView.page().currentFrame().setScrollBarPolicy(QtCore.Qt.Horizontal^QtCore.Qt.Vertical, QtCore.Qt.ScrollBarAlwaysOff)
        self.inspect = QtWebKit.QWebInspector()
        self.graphicsScene= QtGui.QGraphicsScene()
        self.graphicsScene.addWidget(self.webView,QtCore.Qt.WindowFlags(0))
        self.graphicsView = QtGui.QGraphicsView(self.graphicsScene, self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 20, 731, 511))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.action1.setText(QtGui.QApplication.translate("MainWindow", "Action1", None, QtGui.QApplication.UnicodeUTF8))
        self.action2.setText(QtGui.QApplication.translate("MainWindow", "Action2", None, QtGui.QApplication.UnicodeUTF8))
        self.action4.setText(QtGui.QApplication.translate("MainWindow", "Action4", None, QtGui.QApplication.UnicodeUTF8))
        self.action3.setText(QtGui.QApplication.translate("MainWindow", "Action3", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
