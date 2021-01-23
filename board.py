import Cell

class board:
    def __init__(self,rows=None,cols=None) -> None:
        if row==None or cols==None:
            self._col=input("Enter no of col")
            self._row=input("Enter no of row")
        else:
            self._col=cols
            self._row=rows
        
        self.grid = [[Cell() for column_cells in range(self._col)] for row_cells in range(self._row)]
        
        self._generate_board()
        