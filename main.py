from ui import Window
from geometry import Line, Point, Cell


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600




def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    cell = Cell(300, 350, 300, 350, win)
    cell2 = Cell(350, 400, 300, 350, win)

    cell.draw_move(cell2, undo=True)
    cell.draw()
    cell2.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()

