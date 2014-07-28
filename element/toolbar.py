# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
class Toolbar(QtGui.QToolBar):
    def __init__(self,parent):
        #利用parent(QMainWindow)工具栏
        toolbar = parent.addToolBar("open")
        
        self.openfileAction=QtGui.QAction(QtGui.QIcon("image/open.png"),parent.tr("open"),parent)
        self.openfileAction.setShortcut("Ctrl+F")                
        toolbar.addAction(self.openfileAction)
        
        self.transAction=QtGui.QAction(QtGui.QIcon("image/trans.png"),parent.tr("trans"),parent)
        self.transAction.setShortcut("Ctrl+T")        
        toolbar.addAction(self.transAction)

        self.saveAction=QtGui.QAction(QtGui.QIcon("image/save.png"),parent.tr("save"),parent)
        self.saveAction.setShortcut("Ctrl+S")
        toolbar.addAction(self.saveAction)

if __name__ == '__main__':
    pass
