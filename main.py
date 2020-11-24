from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5 import uic
import sys
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.QPushButton.clicked.connect(self.run)

    def run(self):
            self.paint()
            self.paintEvent()

    def generate(self, qp):
        qp.setBrush(QBrush(QColor(255, 255, 0)))
        while True:
            qp.drawEllipse(randint(0, 600), randint(0, 600), randint(0, 600), randint(0, 600))

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.generate(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = QMainWindow()
    wnd.show()
    sys.exit(app.exec())