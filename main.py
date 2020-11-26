import sys
from random import randint

from PyQt5.QtGui import QColor, QPainter, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.repaint()

    def generate(self, qp):
        qp.setBrush(QBrush(QColor(randint(0, 255), randint(0, 255),
                                  randint(0, 255))))
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
