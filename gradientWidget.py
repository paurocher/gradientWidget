from PyQt5 import QtGui, QtWidgets, QtCore, Qt
import LabelGradient, buttonBar

class GradientWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GradientWidget, self).__init__()

        self.setGeometry(2500, 500, 250, 100)

        self.gradient = LabelGradient.LabelGradient()
        self.button_bar = buttonBar.ButtonBar(self.gradient)
        self.gradientLayout = QtWidgets.QVBoxLayout()
        self.gradientLayout.setSpacing(0)
        self.gradientLayout.addWidget(self.gradient)
        self.gradientLayout.addWidget(self.button_bar)


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.gradientLayout)
        self.setLayout(self.layout)

        self.gradient.setGeometry(self.layout.contentsMargins().right(), 0,
                             self.width()-self.layout.contentsMargins().right()*2, 75)
        self.gradient.update_gradient()



        self.color_picker_dialog = QtWidgets.QColorDialog()
        self.color_picker_dialog.currentColorChanged.connect(self.on_color_change)

        self.color_layout = QtWidgets.QHBoxLayout()
        self.choose_color = QtWidgets.QPushButton('color')
        self.choose_color.released.connect(self.color_picker_dialog_show)
        self.color_layout.addWidget(self.choose_color)
        self.color_display = QtWidgets.QLabel()

        self.color_layout.addWidget(self.color_display)
        self.layout.addLayout(self.color_layout)

    def color_picker_dialog_show(self):
        self.color_picker_dialog.open()


    def on_color_change(self, c):
        self.color_display.setStyleSheet(
            "QLabel {{background-color : rgb({},{},{})}}".format(
                c.red(), c.green(), c.blue()))

    def resizeEvent(self, e):
        self.gradient.update()













