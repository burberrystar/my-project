import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class Cell(QPushButton):
    def __init__(self, x, y, parent):
        super().__init__()
        self.x = x
        self.y = y
        self.parent = parent
        self.is_mine = False
        self.revealed = False
        self.setFixedSize(100,100)
        self.clicked.connect(self.reveal)