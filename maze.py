import random

from geometry import Cell
from time import sleep


class Maze:
    def __init__(self, 
                 x1:int, 
                 y1:int, 
                 num_rows:int, 
                 num_cols:int, 
                 cell_size_x:int, 
                 cell_size_y:int, 
                 win=None,
                 seed:int=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        if self.num_rows < 1 or self.num_cols < 1:
            raise Exception("Number of rows/columns cannot be zero(0) or negative.")
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        self._seed = seed
        if self._seed is not None:
            random.seed(self._seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _draw_cell(self, col, row) -> None:
            if self._win is None:
                return
            self._cells[col][row].draw()
            self._animate()

    def _create_cells(self) -> None:
        for column in range(self.num_cols):
            cols = []
            for row in range(self.num_rows):
                cols.append(Cell(self.x1 + column * self._cell_size_x,
                                 self.x1 + column * self._cell_size_x + self._cell_size_x,
                                 self.y1 + row * self._cell_size_y,
                                 self.y1 + row * self._cell_size_y + self._cell_size_y,
                                 self._win
                                    )
                                )
            self._cells.append(cols)

        for column in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(column, row)

    def _animate(self) -> None:
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        if self._win is not None:
            self._draw_cell(0, 0)
        salida = self._cells[-1][-1]
        salida.has_bottom_wall = False
        if self._win is not None:
            self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            directions = [(i + 1, j), 
                        (i - 1, j), 
                        (i, j + 1), 
                        (i, j - 1)]
            possible_moves = []
            # TODO Make this more readable ------_____-------
            for col, row in directions:
                print(col, row)
                if 0 <= col < len(self._cells):
                    if 0 <= row < len(self._cells[col]):
                        if not self._cells[col][row].visited:
                            possible_moves.append((col, row))
            print(possible_moves)
            if len(possible_moves) == 0:
                current.draw()
                return
            # TODO Figure out how to break down the walls between the random cell and this one
            next_cell = random.choice(possible_moves)
            current.draw_move(self._cells[next_cell[0]][next_cell[1]])
            self._break_walls_r(*next_cell)




            

