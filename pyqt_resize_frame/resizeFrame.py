from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget


class ResizeFrame(QWidget):
    deactivated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

        self.__resize_frame_max_width = self.maximumWidth()
        self.__resize_frame_max_height = self.maximumHeight()

        self.setMouseTracking(True)

    def paintEvent(self, e):
        painter = QPainter(self)
        pen = QPen(QColor(Qt.blue), 5)
        painter.setPen(pen)
        painter.drawRect(self.rect())
        return super().paintEvent(e)

    def adjustResizeFrame(self, pos, cur_shape):
        x = pos.x()
        y = pos.y()
        self.resize(QSize(x, y))

        resize_frame_min_width = 30
        resize_frame_min_height = 30

        self.setMaximumSize(self.__resize_frame_max_width, self.__resize_frame_max_height)
        if cur_shape == Qt.SizeHorCursor:
            height = self.height()
            self.setMaximumHeight(height)
            if x < resize_frame_min_width:
                pass
            else:
                resize_frame_min_height = height
                self.setMinimumSize(resize_frame_min_width, resize_frame_min_height)
        elif cur_shape == Qt.SizeVerCursor:
            width = self.width()
            self.setMaximumWidth(width)
            if y < resize_frame_min_height:
                pass
            else:
                resize_frame_min_width = width
                self.setMinimumSize(resize_frame_min_width, resize_frame_min_height)
        else:
            self.setMinimumSize(resize_frame_min_width, resize_frame_min_height)

    def event(self, e):
        if e.type() == 25:
            self.deactivated.emit()
        return super().event(e)
