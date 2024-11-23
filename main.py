from ui import Window
from maze import Maze


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600




def main() -> None:
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    num_rows = 20
    num_cols = 20
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=0)


    win.wait_for_close()

if __name__ == "__main__":
    main()

