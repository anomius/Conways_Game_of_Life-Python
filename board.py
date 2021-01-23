import Cell
import os
from random import randint


class board:
    def __init__(self,rows=None,cols=None) -> None:
        if row==None or cols==None:
            self._col=input("Enter no of col")
            self._row=input("Enter no of row")
        else:
            self._col=cols
            self._row=rows
        
        self.grid = [[Cell() for column_cells in range(self._col)] for row_cells in range(self._row)]
        
        self.generate_board()

    def draw_board(self):
       print('\n'*10)
       for row in self.grid:
           for column in row:
               print(column,end="")
        
    def generate_board():
        for row in self._grid:
            for column in row:
                ran = randint(0,2)
                if ran==1:
                    column.set_liv