LINE_WIDTH = 2


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
    def __init__(self, x1, x2, y1, y2, window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

    def draw(self, fill_color:str) -> None:
        if self.has_left_wall:
            self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color)
        if self.has_right_wall:
            self._window.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color)
        if self.has_top_wall:
            self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color)
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color)

