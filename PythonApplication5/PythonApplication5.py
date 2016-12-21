# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""


import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import time
from PyQt5.QtCore import QTime

class SubAddressAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        result = []
        for item in values:
            if (int(item) >= 0) and (int(item) < 32):
                result.append('{:}{:d}'.format('SA', int(item)))
        return result

class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        result = []
        for item in values:
            result.append('{:}{:d}'.format('SA', int(item)))
        return result

    def tickStrings(self, values, scale, spacing):
        return [QTime().addMSecs(value).toString('mm:ss') for value in values]

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

xAxis.setTickSpacing(major=1, minor=1)
yAxis.setTickSpacing(major=1, minor=1)

vb = CustomViewBox()

pw = pg.PlotWidget(axisItems={'bottom': xAxis, 'left': yAxis}, enableMenu=False, title="MIL-STD-1553B Log Trace: LogFile.txt [2016-05-27 13:27:53.39]")
pw.setRange(xRange=[0,31], padding=0)

#pw = pg.PlotWidget(viewBox=vb, enableMenu=False, title="MIL-STD-1553B Log Trace: LogFile.txt [2016-05-27 13:27:53.39]")
dates = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
#yvals = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
yvals = [0,0,0,1,1,1,2,2,2,3,3,3,3,3,3,3,4,4,4,5,5,6,6,6,6,6,6,6,6,6,6,6]

f = open('LogFile.txt', 'r')

for line in f:
    print(line,)

#pw.plot(x=dates, y=yvals, symbol='o')
pw.plot(x=[0,1,7,11], y=[0,0,0,0], symbol='o')
"""
pw.plot(x=[20,24,30,41], y=[0,0,0,0], symbol='o')
"""
pw.plot(x=[2,4,5,10], y=[1,1,1,1], symbol='o')
pw.plot(x=[12,14,15], y=[2,2,2], symbol='o')
pw.plot(x=[13,17,27], y=[3,3,3], symbol='o')
pw.plot(x=[16,19,28], y=[4,4,4], symbol='o')
pw.plot(x=[21,24,25], y=[5,5,5], symbol='o')
"""
pw.plot(x=[12,14,15], y=[6,6,6], symbol='o')
pw.plot(x=[12,14,15], y=[7,7,7], symbol='o')
pw.plot(x=[12,14,15], y=[8,8,8], symbol='o')
pw.plot(x=[12,14,15], y=[9,9,9], symbol='o')
pw.plot(x=[0,1,3,7], y=[10,10,10,10], symbol='o')
pw.plot(x=[2,4,5,10], y=[11,11,11,11], symbol='o')
pw.plot(x=[12,14,15], y=[12,12,12], symbol='o')
pw.plot(x=[12,14,15], y=[13,13,13], symbol='o')
pw.plot(x=[12,14,15], y=[14,14,14], symbol='o')
pw.plot(x=[12,14,15], y=[15,15,15], symbol='o')
pw.plot(x=[12,14,15], y=[16,16,16], symbol='o')
pw.plot(x=[12,14,15], y=[17,17,17], symbol='o')
pw.plot(x=[12,14,15], y=[18,18,18], symbol='o')
pw.plot(x=[12,14,15], y=[19,19,19], symbol='o')
pw.plot(x=[0,1,3,7], y=[20,20,20,20], symbol='o')
pw.plot(x=[2,4,5,10], y=[21,21,21,21], symbol='o')
pw.plot(x=[12,14,15], y=[22,22,22], symbol='o')
pw.plot(x=[12,14,15], y=[23,23,23], symbol='o')
pw.plot(x=[12,14,15], y=[24,24,24], symbol='o')
pw.plot(x=[12,14,15], y=[25,25,25], symbol='o')
pw.plot(x=[12,14,15], y=[26,26,26], symbol='o')
pw.plot(x=[12,14,15], y=[27,27,27], symbol='o')
pw.plot(x=[12,14,15], y=[28,28,28], symbol='o')
pw.plot(x=[12,14,15], y=[29,29,29], symbol='o')
pw.plot(x=[0,1,3,7], y=[30,30,30,30], symbol='o')
pw.plot(x=[2,4,5,10], y=[31,31,31,31], symbol='o')
"""
pw.show()
pw.setWindowTitle('pyqtgraph example: customPlot')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
