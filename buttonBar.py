from PyQt5 import QtCore, QtWidgets, QtGui

class ButtonBar(QtWidgets.QWidget):
    def __init__(self, gradient):
        super(ButtonBar, self).__init__()

        self.setMinimumHeight(10)
        self.setMaximumHeight(10)
        self.gradient = gradient
        self.start = Button(0, (0,0,0), '', self.gradient)
        self.start.setParent(self)
        self.final = Button(100, (255,255,255), '', self.gradient)
        self.final.setParent(self)

        self.stop_points = [self.start, self.final]

    def paintEvent(self, e):
        p = QtGui.QPainter(self)
        p.fillRect(0, 0, self.width(), self.height(), QtGui.QColor(180,180,180))

    def update_gradient(self):
        stops = []
        for i in self.stop_points:
            stops.append((i.pos_normalized, QtGui.QColor(*i.color)))

        self.gradient.set_stops(stops)


class Button(QtWidgets.QPushButton):
    def __init__(self, pos, color, stop, gradient):
        super(Button, self).__init__()

        self.color = color
        self.gradient = gradient

        self.setGeometry(0, 0, 10, 10)
        self.setStyleSheet("QPushButton {"
                           "background-color: rgba(20,20,20,50);"
                           "border: flat;}")
        self.setText('X')

        self.move(pos, 0)
        self.pos_normalized = 0.0

        self.button_move_offset = None

        self.pressed.connect(self.button_pressed)
        self.clicked.connect(self.button_released)

    def select(self):
        pass
        '''this will draw a frame around the button when selected'''

    def button_pressed(self):
        print ('pressed')

    def button_released(self):
        print ('released')

    def mouseMoveEvent(self, ee):
        self.mouse_new_posx = ee.globalPos().x()-self.window().pos().x()- \
                              20 - self.button_move_offset
        if self.mouse_new_posx <= 0:
            self.mouse_new_posx = 0
        elif self.mouse_new_posx >= self.window().width()-50:
            self.mouse_new_posx = self.window().width()-50

        self.move(self.mouse_new_posx, 0)
        self.pos_normalized = self.mouse_new_posx / (self.window().width()-50)
        self.parent().update_gradient()


    def mousePressEvent(self, e):
        # if e.buttons() == QtCore.Qt.RightButton:

        self.button_move_offset = e.x()


    def mouseReleaseEvent(self, e):
        pass
