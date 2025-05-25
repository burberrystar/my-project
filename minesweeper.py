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

    def reveal(self):
        if self.revealed:
            return
        self.revealed = True
        if self.is_mine:
            self.setText("💣")
            self.setStyleSheet("background-color: red")
            self.parent.game_over(False)
        else:
            count = self.parent.count_mines(self.x, self.y)
            if count:
                self.setText(str(count))
            else:
                self.setStyleSheet("background-color: #ddd")
                self.parent.reveal_neighbours(self.x, self.y)
        self.setEnabled(False)

class Minesweeper(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сапер")
        self.size = 5 
        self.mines = 3
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.init_board()

    def init_board(self):
        self.cells = [[Cell(x, y, self) for y in range(self.size)] for x in range(self.size)] # двумерный список клеток
        for x in range(self.size):
            for y in range(self.size):
                self.grid.addWidget(self.cells[x][y], x, y)
        self.place_mines()
    
    def place_mines(self):
        position = random.sample(range(self.size * self.size), self.mines)
        for pos in position:
            x = pos // self.size
            y = pos % self.size
            self.cells[x][y].is_mine = True
    
    