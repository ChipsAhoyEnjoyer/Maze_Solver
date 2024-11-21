import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols,)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_zero_rows_columns(self):
        num_cols = 0
        num_rows = 10
        with self.assertRaises(Exception):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        num_cols = 12
        num_rows = 0
        with self.assertRaises(Exception):
            m2 = Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

        


if __name__ == "__main__":
    unittest.main()
