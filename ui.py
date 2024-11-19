from tkinter import Tk, BOTH, Canvas
from geometry import Line


TITLE = "Maze Solver"
BG_COLOR = "white"
CLOSING_MSG = "Closing window..."


class Window:
    def __init__(self, width:int, height:int) -> None:
        self._window = Tk()
        self._window.title(TITLE)
        self._window.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._window, width=width, height=height, bg=BG_COLOR)
        self._canvas.pack()
        self._window_open = False

    def redraw(self) -> None:
        self._window.update_idletasks()
        self._window.update()

    def wait_for_close(self) -> None:
        self._window_open = True
        while self._window_open:
            self.redraw()
        print(CLOSING_MSG)

    def close(self) -> None:
        self._window_open = False

    def draw_line(self, line:Line, fill_color: str) -> None:
        line.draw(self._canvas, fill_color)