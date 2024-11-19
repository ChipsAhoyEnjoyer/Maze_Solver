from ui import Window
from geometry import Line, Point, Cell


LINE_COLOR = "black"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


coords = [(x, y) for x in range(0, 801, 20) for y in range(0, 801, 20)]


def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    for coord in coords:
        cell = Cell(window=win, x1=coord[0], y1=coord[0],x2=coord[1],y2=coord[1])
        cell.draw(LINE_COLOR)

    win.wait_for_close()

if __name__ == "__main__":
    main()

