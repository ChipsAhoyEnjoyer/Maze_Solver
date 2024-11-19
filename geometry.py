LINE_WIDTH = 2
DEFAULT_LINE_COLOR = "black"
RED = "red"
GRAY = "gray"


class Point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a:Point, point_b:Point) -> None:
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color:str) -> None:
        canvas.create_line(
            self.point_a.x, 
            self.point_a.y, 
            self.point_b.x, 
            self.point_b.y, 
            fill=fill_color, 
            width=LINE_WIDTH, 
)       

class Cell:
    def __init__(self, x1:int, x2:int, y1:int, y2:int, window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

    def draw(self) -> None:
        if self.has_left_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y1), 
                     Point(self._x1, self._y2)), 
                     DEFAULT_LINE_COLOR)
        if self.has_right_wall:
            self._window.draw_line(
                Line(Point(self._x2, self._y1), 
                     Point(self._x2, self._y2)), 
                     DEFAULT_LINE_COLOR)
        if self.has_top_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y1), 
                     Point(self._x2, self._y1)), 
                     DEFAULT_LINE_COLOR)
        if self.has_bottom_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y2), 
                     Point(self._x2, self._y2)), 
                     DEFAULT_LINE_COLOR)

    def draw_move(self, to_cell, undo = False) -> None:
        line_color = GRAY
        if undo:
            line_color = RED
        
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2

        self._window.draw_line(
            Line(Point(x1, y1), (Point(x2, y2))),
            line_color
        )

