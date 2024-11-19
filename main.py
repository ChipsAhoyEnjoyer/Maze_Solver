from ui import Window
from line import Line, Point


line_color = "black"
line = Line(Point(0,0), Point(50, 50))
line2 = Line(Point(48, 72), Point(50, 50))
line3 = Line(Point(0,0), Point(48,72))


def main():
    win = Window(800, 600)

    win.draw_line(line, line_color)
    win.draw_line(line2, line_color)
    win.draw_line(line3, line_color)

    win.wait_for_close()

if __name__ == "__main__":
    main()

