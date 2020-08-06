import sys
from PyQt5 import QtWidgets
import gradientWidget


app = QtWidgets.QApplication(sys.argv)
GW = gradientWidget.GradientWidget()
GW.show()
app.exec_()