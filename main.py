from sys import argv

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtCore import Qt, QPoint

from random import randint


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flag = False
        self.initUI()
        self.brush = QBrush()
        self.brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.brush.setColor(QColor('yellow'))
        self.setFixedSize(600, 600)

    def initUI(self):
        self.button = QPushButton(self)
        self.button.clicked.connect(self.click)
        self.button.move(300, 300)

    def click(self):
        self.flag = True
        self.update()
        
    def paintEvent(self, e):
        print(self.flag)
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(self.brush)
            for i in range(10):
                coords = (randint(0, 600), randint(0, 600))
                size = randint(5, 200)

                painter.drawEllipse(*coords, size, size)

            painter.end()
            # self.flag = False
            self.update()


if __name__ == '__main__':
    app = QApplication(argv)
    window = Window()
    window.show()
    app.exec()
