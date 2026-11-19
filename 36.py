
# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid.

# Only the filled cells need to be validated according to the following rules:
# - Each row must contain the digits 1-9 without repetition.
# - Each column must contain the digits 1-9 without repetition.
# - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.

# noinspection DuplicatedCode
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Horizontally
        for y in range(9):
            seen = {}
            for x in range(9):
                if board[y][x] == ".":
                    continue

                if board[y][x] in seen:
                    return False
                seen[board[y][x]] = True

        # Vertically
        for x in range(9):
            seen = {}
            for y in range(9):
                if board[y][x] == ".":
                    continue

                if board[y][x] in seen:
                    return False
                seen[board[y][x]] = True

        # inner squares
        for xs in range(3):
            x_offset = xs * 3
            for ys in range(3):
                seen = {}
                y_offset = ys * 3

                for x in range(3):
                    for y in range(3):
                        if board[y + y_offset][x + x_offset] == ".":
                            continue

                        if board[y + y_offset][x + x_offset] in seen:
                            return False
                        seen[board[y + y_offset][x + x_offset]] = True

        return True



