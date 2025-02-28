import sys
import random
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.DrawButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            self.draw_ellipse(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_ellipse(self, qp):
        for i in range(random.randint(1, 100)):
            wh = random.randint(1, 100)
            qp.drawEllipse(random.randint(1, 1125), random.randint(1, 905), wh, wh)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestWidget()
    ex.show()
    sys.exit(app.exec())
