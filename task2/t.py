from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6.QtGui import QBrush, QColor, QPainter
from PyQt6.QtCore import Qt

from random import randint
from sys import argv


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)
        self.paint = False
        self.brush = QBrush()
        self.brush.setColor(QColor('yellow'))
        self.brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.setFixedSize(600, 600)
        self.initUI()

    def paintEvent(self, e):
        if self.paint:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(self.brush)
            for _ in range(10):
                x = randint(0, 600)
                y = randint(0, 600)
                size = randint(10, 300)
                painter.drawEllipse(x, y, size, size)
            painter.end()
            self.paint = False

    def initUI(self):
        self.button = QPushButton(self)
        self.button.clicked.connect(self.draw)
        self.button.move(300, 300)

    def draw(self):
        self.paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(argv)
    window = Window()
    window.show()
    app.exec()
