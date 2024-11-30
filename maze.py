import random
import collections
from geometry import Cell
from time import sleep

REFRESH_RATE = 0.01


class Maze:
    def __init__(self,
                 x1: int,
                 y1: int,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: int,
                 cell_size_y: int,
                 win=None,
                 seed: int = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.goal_coords = (num_cols - 1, num_rows - 1)
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
        self._reset_cells_visited()

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

    def _animate(self, refresh_rate: float = REFRESH_RATE) -> None:
        if self._win is None:
            return
        self._win.redraw()
        sleep(refresh_rate)

    def _break_entrance_and_exit(self) -> None:
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        if self._win is not None:
            self._draw_cell(0, 0)
        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        if self._win is not None:
            self._draw_cell(-1, -1)

    def _break_walls_r(self, i: int, j: int) -> None:
        current = self._cells[i][j]
        current.visited = True
        while True:
            directions = [(i + 1, j),
                          (i - 1, j),
                          (i, j + 1),
                          (i, j - 1)]
            possible_moves = []

            for col, row in directions:
                if 0 <= col < len(self._cells):
                    if 0 <= row < len(self._cells[col]):
                        if not self._cells[col][row].visited:
                            possible_moves.append((col, row))

            if len(possible_moves) == 0:
                self._draw_cell(i, j)
                return

            next_cell = random.choice(possible_moves)
            if next_cell == (i + 1, j):
                current.has_right_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_left_wall = False
            elif next_cell == (i - 1, j):
                current.has_left_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_right_wall = False
            elif next_cell == (i, j + 1):
                current.has_bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_top_wall = False
            else:
                current.has_top_wall = False
                self._cells[next_cell[0]][next_cell[1]].has_bottom_wall = False

            self._draw_cell(i, j)
            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self) -> None:
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self, method: str = "r") -> bool:
        if method == "DFS":
            return self._solve_r()
        if method == "BFS":
            return self._solve_l()

    def _is_goal(self, col: int, row: int) -> bool:
        if (col, row) == self.goal_coords:
            return True
        return False

    def _solve_r(self, i: int = 0, j: int = 0) -> bool:
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if (i, j) == self.goal_coords:
            return True

        directions = [(i + 1, j),
                      (i - 1, j),
                      (i, j + 1),
                      (i, j - 1)]

        for col, row in directions:
            if 0 <= col < len(self._cells):
                if 0 <= row < len(self._cells[col]):
                    if (
                            ((col, row) == (i + 1, j)) and
                            (not current.has_right_wall) and
                            (not self._cells[col][row].visited)
                    ):
                        current.draw_move(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        current.draw_move(self._cells[col][row], undo=True)
                    if (
                            ((col, row) == (i - 1, j)) and
                            (not current.has_left_wall) and
                            (not self._cells[col][row].visited)
                    ):
                        current.draw_move(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        current.draw_move(self._cells[col][row], undo=True)
                    if (
                            ((col, row) == (i, j + 1)) and
                            (not current.has_bottom_wall) and
                            (not self._cells[col][row].visited)
                    ):
                        current.draw_move(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        current.draw_move(self._cells[col][row], undo=True)
                    if (
                            ((col, row) == (i, j - 1)) and
                            (not current.has_top_wall) and
                            (not self._cells[col][row].visited)
                    ):
                        current.draw_move(self._cells[col][row])
                        if self._solve_r(col, row):
                            return True
                        current.draw_move(self._cells[col][row], undo=True)
        return False

    def _solve_l(self, i: int = 0, j: int = 0) -> bool:
        self._cells[i][j].visited = True
        to_visit = collections.deque([(i, j),])

        while to_visit:
            current = to_visit.popleft()
            self._cells[current[0]][current[1]].visited = True
            directions = [(current[0] + 1, current[1]),
                          (current[0] - 1, current[1]),
                          (current[0], current[1] + 1),
                          (current[0], current[1] - 1)]

            for col, row in directions:
                if 0 <= col < len(self._cells):  # Within the maze columns
                    if 0 <= row < len(self._cells[col]):  # Within the maze rows
                        if not self._cells[col][row].visited and (col, row) not in to_visit:
                            if col == current[0] + 1:
                                if not self._cells[current[0]][current[1]].has_right_wall:
                                    self._cells[current[0]][current[1]].draw_move(self._cells[col][row])
                                    if self._is_goal(col, row):
                                        self._animate()
                                        return True
                                    to_visit.append((col, row))

                            elif col == current[0] - 1:
                                if not self._cells[current[0]][current[1]].has_left_wall:
                                    self._cells[current[0]][current[1]].draw_move(self._cells[col][row])
                                    if self._is_goal(col, row):
                                        self._animate()
                                        return True
                                    to_visit.append((col, row))

                            elif row == current[1] + 1:
                                if not self._cells[current[0]][current[1]].has_bottom_wall:
                                    self._cells[current[0]][current[1]].draw_move(self._cells[col][row])
                                    if self._is_goal(col, row):
                                        self._animate()
                                        return True
                                    to_visit.append((col, row))

                            elif row == current[1] - 1:
                                if not self._cells[current[0]][current[1]].has_top_wall:
                                    self._cells[current[0]][current[1]].draw_move(self._cells[col][row])
                                    if self._is_goal(col, row):
                                        self._animate()
                                        return True
                                    to_visit.append((col, row))
                            self._animate(0.03)

        return False  # All paths exhausted
