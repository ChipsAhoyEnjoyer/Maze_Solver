line_width = 2


class Point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a:Point, point_b:Point) -> None:
        self.__point_a = Point(point_a.x, point_a.y)
        self.__point_b = Point(point_b.x, point_b.y)

    def draw(self, canvas, fill_color:str) -> None:
        line = canvas.create_line(
            self.__point_a.x, 
            self.__point_a.y, 
            self.__point_b.x, 
            self.__point_b.y, 
            fill=fill_color, 
            width=line_width, 
)       

class Cell:
    pass