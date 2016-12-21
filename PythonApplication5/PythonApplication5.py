# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import time

class SubAddressAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = ['SA0', 'SA1', 'SA2', 'SA3', 'SA4', 'SA5', 'SA6', 'SA7', 'SA8', 'SA9', 'SA10', 'SA11', 'SA12', 'SA13', 'SA14', 'SA15', 'SA16', 'SA17', 'SA18', 'SA19', 'SA20', 'SA21', 'SA22', 'SA23', 'SA24', 'SA25', 'SA26', 'SA27', 'SA28', 'SA29', 'SA30', 'SA31', 'SA32' ]
        result = []
        for item in values:
            result.append(strns[int(item)])
        return result

class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = ['SA0', 'SA1', 'SA2', 'SA3', 'SA4', 'SA5', 'SA6', 'SA7', 'SA8', 'SA9', 'SA10', 'SA11', 'SA12', 'SA13', 'SA14', 'SA15', 'SA16', 'SA17', 'SA18', 'SA19', 'SA20', 'SA21', 'SA22', 'SA23', 'SA24', 'SA25', 'SA26', 'SA27', 'SA28', 'SA29', 'SA30', 'SA31' ]
        return strns[0:len(values)]

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)


app = pg.mkQApp()

xAxis = DateAxis(orientation='bottom')
yAxis = SubAddressAxis(orientation='left')

vb = CustomViewBox()

pw = pg.PlotWidget(viewBox=vb, axisItems={'bottom': xAxis, 'left': yAxis}, enableMenu=False, title="PlotItem with custom axis and ViewBox<br>Menu disabled, mouse behavior changed: left-drag to zoom, right-click to reset zoom")
dates = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
pw.plot(x=dates, y=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], symbol='o')
pw.show()
pw.setWindowTitle('pyqtgraph example: customPlot')

r = pg.PolyLineROI([(0,0), (10, 10)])
pw.addItem(r)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
