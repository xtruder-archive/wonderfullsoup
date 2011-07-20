# -*- coding: utf-8 -*-
import sys
import random

from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import QWebElement
from PyQt4.QtCore import QEvent, QRectF, QRect, QSize
from PyQt4.QtGui import QWidget, QPen, QBrush, QColor
from test2 import Ui_MainWindow

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.webView.installEventFilter(self)
        QtCore.QObject.connect(self.ui.graphicsScene, QtCore.SIGNAL("sceneRectChanged(const QRectF&)"), self.webResize)
        QtCore.QObject.connect(self.ui.webView, QtCore.SIGNAL("loadFinished(bool)"), self.loadFinished)
        self.rect= None
        self.parents=[]
        self.forceResize= False

    def eventFilter(self, target, event):
        if event.type() == QtCore.QEvent.MouseMove:
           #self.ui.webView.resize(self.ui.graphicsScene.width(),self.ui.graphicsScene.height())
           pos= event.pos()
           res= self.ui.webView.page().mainFrame().hitTestContent(pos)
           el= res.element()
           widthProperty = el.styleProperty("width",2);
           heightProperty = el.styleProperty("height",2);
           for parent in self.parents:
               self.ui.graphicsScene.removeItem(parent)
           self.parents=[]
           if(el.geometry().center().x()==0 or el.geometry().center().y()==0):
               el= res.linkElement()
           else:
               t_el= el
               counter= 10
               counter2=3
               while(t_el.parent() and t_el.geometry().center().x()<>0):
                   self.parents.append(self.ui.graphicsScene.addRect(QRectF(t_el.geometry()), QPen(QBrush(QColor(20,20,counter,255)), counter2, QtCore.Qt.DashDotLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin), QBrush(QColor(0,0,0,0))))
                   t_el= t_el.parent()
                   counter+=20
                   counter2-=1
                   if not counter2:
                       counter2= 1
           print "x: " + str(el.geometry().center().x()) + "y: " + str(el.geometry().center().y())
           print "x: " + str(res.boundingRect().center().x()) + "y: " + str(res.boundingRect().center().y()) 
           if self.rect:
               self.ui.graphicsScene.removeItem(self.rect)
           self.rect= self.ui.graphicsScene.addRect(QRectF(res.boundingRect()), QPen(), QBrush(QColor(20,20,20,50)))
           print("mousemove")
           self.ui.inspect.setPage(self.ui.webView.page())
           self.ui.inspect.show()
           self.ui.inspect.update()

        return False

    def webResize(self, e):
	if self.forceResize:
            print "resize"
            self.forceResize= False
            self.ui.webView.resize(self.ui.graphicsScene.width(), self.ui.graphicsScene.height())
            self.ui.webView.page().setViewportSize(QSize(self.ui.graphicsScene.width()-20, self.ui.graphicsScene.height()-20))

    def loadFinished(self, e):
        self.forceResize= True
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

