import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.paintEvent(self.repaint())

    def generate(self, qp):
        qp.setBrush(QBrush(QColor(255, 255, 0)))
        size = randint(0, 600)
        qp.drawEllipse(randint(0, 600), randint(0, 600), size, size)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.generate(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
