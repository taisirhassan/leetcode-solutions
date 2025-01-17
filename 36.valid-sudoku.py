#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (61.15%)
# Likes:    11172
# Dislikes: 1176
# Total Accepted:    1.8M
# Total Submissions: 3M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach 1: Using Three Lists of Sets (Brute force)
        # Initialize list of sets for rows, columns, and 3x3 boxes.
        # Check each row.
        # Loop over each row in the board.
        for row in board:
            seen = set()  # Create a new set to track digits seen in the current row.
            for char in row:  # Iterate over each character in the row.
                if char != ".":  # Skip empty cells (denoted by ".").
                    if (
                        char in seen
                    ):  # If the digit is already in 'seen', the row has duplicates.
                        return False  # Return False indicating the board is not valid.
                    seen.add(char)  # Add the current digit to the 'seen' set.

        # Check each column.
        # Loop over the range 0 to 8 for each column index.
        for col in range(9):
            seen = set()  # Create a new set to track digits seen in the current column.
            # For each column, iterate over every row.
            for row in range(9):
                char = board[row][
                    col
                ]  # Get the character located at the current row and column.
                if char != ".":  # Skip empty cells.
                    if (
                        char in seen
                    ):  # If the digit is already in 'seen', the column has duplicates.
                        return False  # Return False indicating the board is not valid.
                    seen.add(char)  # Add the current digit to the 'seen' set.

        # Check each of the 3 x 3 sub-boxes.
        # The board is divided into nine 3x3 sub-boxes.
        # We use two nested loops to iterate over each sub-box.
        for box_row in range(3):  # Loop for each box row group (3 total groups).
            for box_col in range(3):  # Loop for each box column group (3 total groups).
                seen = (
                    set()
                )  # Create a new set to track digits seen in the current 3x3 sub-box.
                # Calculate the starting row and column indices for the current sub-box.
                start_row, start_col = box_row * 3, box_col * 3
                # Loop over the 3 rows within the current sub-box.
                for i in range(3):
                    # Loop over the 3 columns within the current sub-box.
                    for j in range(3):
                        # Get the character from the current cell in the sub-box.
                        char = board[start_row + i][start_col + j]
                        if char != ".":  # Skip empty cells.
                            if (
                                char in seen
                            ):  # If the digit is already in 'seen', there is a duplicate in the sub-box.
                                return False  # Return False indicating the board is not valid.
                            seen.add(
                                char
                            )  # Add the current digit to the 'seen' set for the sub-box.

        # If all rows, columns, and sub-boxes are valid (no duplicates found), return True.
        return True


# @lc code=end
