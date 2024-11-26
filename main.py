from ui import Window
from maze import Maze

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main() -> None:
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    num_rows = 5
    num_cols = 5
    margin = 50
    screen_x = SCREEN_WIDTH
    screen_y = SCREEN_HEIGHT
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows
    print("Creating maze.")
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 0)
    print("Solving!")
    solve = maze.solve_l()
    print("Done...")
    if solve:
        print("Maze solved!")
    else:
        print("Maze can not be solved...")

    win.wait_for_close()


if __name__ == "__main__":
    main()
