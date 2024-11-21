from geometry import Cell
from time import sleep


class Maze:
    def __init__(self, x1:int, y1:int, num_rows:int, num_cols:int, cell_size_x:int, cell_size_y:int, win=None,) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        if self.num_rows < 1 or self.num_cols < 1:
            raise Exception("Number of rows/columns cannot be zero(0) or negative.")
        self._create_cells()
        self._break_entrance_and_exit()

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

    def _animate(self):
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

