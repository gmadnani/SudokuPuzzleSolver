"""
Girish Madnani
Class: CS 521 - Fall 23
Date: 15th November 2023
Final Project: Sudoku Solver
Description of Problem: program that takes an input file which is an unsolved sudoku puzzle and returns a solve puzzle
using backtracking algorithm.
"""

import copy
import sys


class SudokuSolver:
    def __init__(self, puzzle):
        """
        Validate puzzle format upon initialization
        """
        if not isinstance(puzzle, list) or len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
            raise ValueError("Invalid puzzle format. Please provide a 9x9 list of lists.")
        self.puzzle = puzzle
        self.solution = None

    def is_valid(self, row, col, num):
        """
        Returns the numbers are valid in the grid
        """
        # Check if 'num' is a valid choice for the given cell
        for i in range(9):
            if self.puzzle[row][i] == num or self.puzzle[i][col] == num:
                return False

        # Check within the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.puzzle[start_row + i][start_col + j] == num:
                    return False

        return True

    # Function to solve the Sudoku puzzle using backtracking
    def solve(self):
        """
        Returns true when the puzzle is solved and save the solution in the solution attribute
        """
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.puzzle[row][col] = num
                            if self.solve():
                                return True
                            self.puzzle[row][col] = 0
                    return False
        self.solution = [row[:] for row in self.puzzle]
        return True

    def __repr__(self):
        """
        Representation method to display the solved Sudoku grid
        """
        result = ""
        result += "\nSolved Sudoku Puzzle:\n"
        if self.solution:
            for i, row in enumerate(self.solution):
                result += " ".join(map(str, row[:3])) + " | " + " ".join(map(str, row[3:6])) + " | " + " ".join(
                    map(str, row[6:])) + "\n"
                if i == 2 or i == 5:
                    result += "------+-------+------\n"
        else:
            result += "No solution found."
        return result


def read_sudoku_from_file(file_path):
    """
    Reads form the input file and returns the puzzle without the grid lines
    """
    puzzle = []
    # Read Sudoku puzzle from a file
    with open(file_path, 'r') as file:
        for line in file:
            # Extract digits from the line using a regular expression, replace '.' with 0
            digits = [int(char) if char.isdigit() else char for char in line.replace('.', '0') if char.isdigit()]
            if digits:
                puzzle.append(digits)

    # Check if there are exactly 9 rows
    if len(puzzle) != 9:
        raise ValueError(f"Invalid puzzle. It must have exactly 9 rows.")

    return puzzle


def main():
    """
    Main function to read Sudoku puzzles from files and solve them
    """
    input_files = sys.argv[1:]
    if not input_files:
        print("Please provide input file paths as command line arguments.")
        return

    for input_file in input_files:
        try:
            puzzle = read_sudoku_from_file(input_file)
            initial_puzzle = copy.deepcopy(puzzle)
            sudoku_solver = SudokuSolver(puzzle)
            sudoku_solver.solve()
            print(f"\nInitial Sudoku Puzzle for {input_file}:\n")
            for i, row in enumerate(initial_puzzle):
                print(" ".join(map(str, row[:3])) + " | " + " ".join(map(str, row[3:6])) + " | " + " ".join(
                    map(str, row[6:])))
                if i == 2 or i == 5:
                    print("------+-------+------")
            print(sudoku_solver)
        except FileNotFoundError:
            print(f"File not found: {input_file}")
        except ValueError as e:
            print(f"Error processing {input_file}: {e}")


if __name__ == "__main__":
    main()
