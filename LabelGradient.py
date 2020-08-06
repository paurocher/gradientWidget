from PyQt5 import QtWidgets, QtCore, QtGui

class LabelGradient (QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(LabelGradient, self).__init__()
        #self.parent = parent


        self.setText('fefefefef')
        self.style = "QLabel { border : 1px solid black;" \
                     "border-radius: 5px;" \
                     "background: rgb(80,80,80) }"
        self.setStyleSheet(self.style)
        self.setMinimumSize(QtCore.QSize(100, 50))
        self.setMaximumSize(QtCore.QSize(10000, 75))

        self.grad = self.new_gradient()


    def new_gradient(self):
        grad = QtGui.QLinearGradient(
            QtCore.QPoint(0, 0), QtCore.QPoint(0, 0))
        grad.setSpread(QtGui.QGradient.PadSpread)
        grad.setColorAt(0, QtCore.Qt.black)
        grad.setColorAt(1, QtCore.Qt.white)
        return grad

    def update_gradient(self):
        self.grad.setFinalStop(self.width(), 0)

    def gradient_add_color(self, x, color):
        self.grad.setColorAt(x, QtGui.QColor(*color))
        self.update()

    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.fillRect(0, 0, self.width(), 75, self.grad)
        self.update_gradient()

    def mousePressEvent(self, e):
        self.gradient_add_color (e.x()/self.width(), (255,0,0))

    def set_stops(self, stops):
        # self.grad.setStops([(pos, QtGui.QColor(*color))])
        print (stops)
        print (self.grad.stops())
        self.grad.setStops(stops)
        self.update()


"""
class Gradient(QtGui.QLinearGradient):
    def __init__(self, parent=None):
        super().__init__()

    def new_gradient(self):
        grad = QtGui.QLinearGradient(
            QtCore.QPoint(0, 0), QtCore.QPoint(self.width(), 0))
        grad.setSpread(QtGui.QGradient.PadSpread)
        grad.setColorAt(0, QtCore.Qt.black)
        grad.setColorAt(1, QtCore.Qt.white)
        return grad
"""