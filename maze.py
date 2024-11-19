from geometry import Cell
from time import sleep


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        self._create_cells()

    def _draw_cell(self) -> None:
            for columns in self._cells:
                for cell in columns:
                    cell.draw()
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
        self._draw_cell()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)
