import unittest

from sudoku_solver import SudokuSolver, read_sudoku_from_file


class TestSudokuSolver(unittest.TestCase):
    def test_is_valid_valid_placement(self):
        puzzle = [[0] * 9 for _ in range(9)]
        solver = SudokuSolver(puzzle)
        self.assertTrue(solver.is_valid(0, 0, 1))

    def test_is_valid_invalid_placement_row(self):
        puzzle = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        solver = SudokuSolver(puzzle)
        self.assertFalse(solver.is_valid(0, 1, 1))

    def test_is_valid_invalid_placement_column(self):
        puzzle = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        solver = SudokuSolver(puzzle)
        self.assertFalse(solver.is_valid(1, 0, 1))

    def test_is_valid_invalid_placement_subgrid(self):
        puzzle = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        solver = SudokuSolver(puzzle)
        self.assertFalse(solver.is_valid(1, 1, 1))

    def test_solve_solvable_puzzle(self):
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        solver = SudokuSolver(puzzle)
        self.assertTrue(solver.solve())

    def test_read_sudoku_from_file_valid_file(self):
        test_file_path = "test_sudoku_valid.txt"
        with open(test_file_path, "w") as test_file:
            test_file.write("5 3 0 0 7 0 0 0 0\n")
            test_file.write("6 0 0 1 9 5 0 0 0\n")
            test_file.write("0 9 8 0 0 0 0 6 0\n")
            test_file.write("8 0 0 0 6 0 0 0 3\n")
            test_file.write("4 0 0 8 0 3 0 0 1\n")
            test_file.write("7 0 0 0 2 0 0 0 6\n")
            test_file.write("0 6 0 0 0 0 2 8 0\n")
            test_file.write("0 0 0 4 1 9 0 0 5\n")
            test_file.write("0 0 0 0 8 0 0 7 9\n")
        puzzle = read_sudoku_from_file(test_file_path)
        self.assertIsNotNone(puzzle)

    def test_read_sudoku_from_file_invalid_content(self):
        test_file_path = "test_sudoku_invalid.txt"
        with open(test_file_path, "w") as test_file:
            test_file.write("5 3 0 0 7 0 0 0 INVALID\n")
            test_file.write("6 0 0 1 9 5 0 0 0\n")
            test_file.write("0 9 8 0 0 0 0 6 0\n")
            test_file.write("8 0 0 0 6 0 0 0 3\n")
            test_file.write("4 0 0 8 0 3 0 0 1\n")
            test_file.write("7 0 0 0 2 0 0 0 6\n")
            test_file.write("0 6 0 0 0 0 2 8 0\n")
            test_file.write("0 0 0 4 1 9 0 0 5\n")
            test_file.write("0 0 0 0 8 0 0 7 9\n")
        with self.assertRaises(ValueError):
            read_sudoku_from_file(test_file_path)

    def test_read_sudoku_from_file_missing_values(self):
        test_file_path = "test_sudoku_missing_values.txt"
        with open(test_file_path, "w") as test_file:
            test_file.write("5 3 0 0 7 0 0 0\n")
            test_file.write("6 0 0 1 9 5 0 0 0\n")
            test_file.write("0 9 8 0 0 0 0 6 0\n")
            test_file.write("8 0 0 0 6 0 0 0 3\n")
            test_file.write("4 0 0 8 0 3 0 0 1\n")
            test_file.write("7 0 0 0 2 0 0 0 6\n")
            test_file.write("0 6 0 0 0 0 2 8 0\n")
            test_file.write("0 0 0 4 1 9 0 0 5\n")
            test_file.write("0 0 0 0 8 0 0 7 9\n")
        with self.assertRaises(ValueError):
            read_sudoku_from_file(test_file_path)

    def test_read_sudoku_from_file_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_sudoku_from_file("non_existent_file.txt")

    def test_solve_and_match_solution(self):
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        expected_solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

        solver = SudokuSolver(puzzle)
        self.assertTrue(solver.solve())

        # Check if the solved puzzle matches the expected solution
        self.assertListEqual(solver.solution, expected_solution)


if __name__ == "__main__":
    unittest.main()
