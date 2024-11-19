from tkinter import Tk, BOTH, Canvas
from line import Line


title = "Maze Solver"
bg_color = "white"
closing_msg = "Closing window..."


class Window:
    def __init__(self, width:int, height:int) -> None:
        self.__window = Tk()
        self.__window.title(title)
        self.__window.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__window, width=width, height=height, bg=bg_color)
        self.__canvas.pack()
        self.__window_open = False

    def redraw(self) -> None:
        self.__window.update_idletasks()
        self.__window.update()

    def wait_for_close(self) -> None:
        self.__window_open = True
        while self.__window_open:
            self.redraw()
        print(closing_msg)

    def close(self) -> None:
        self.__window_open = False

    def draw_line(self, line:Line, fill_color) -> None:
        line.draw(self.__canvas, fill_color)