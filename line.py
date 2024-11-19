line_width = 2


class Point:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a:tuple, point_b:tuple) -> None:
        if len(point_a) != 2 or len(point_b) != 2:
            raise Exception("Points should be a tuple that contains 2 integers")
        self.__point_a = Point(point_a[0], point_a[1])
        self.__point_b = Point(point_b[0], point_b[1])

    def draw(self, canvas, fill_color:str) -> None:
        line = canvas.create_line(
            self.__point_a.x, 
            self.__point_a.y, 
            self.__point_b.x, 
            self.__point_b.y, 
            fill=fill_color, 
            width=line_width, 
)       
