#
# @lc app=leetcode id=2661 lang=python3
#
# [2661] First Completely Painted Row or Column
#
# https://leetcode.com/problems/first-completely-painted-row-or-column/description/
#
# algorithms
# Medium (49.96%)
# Likes:    444
# Dislikes: 10
# Total Accepted:    27.2K
# Total Submissions: 54.2K
# Testcase Example:  '[1,3,4,2]\n[[1,4],[2,3]]'
#
# You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
# arr and mat both contain all the integers in the range [1, m * n].
#
# Go through each index i in arr starting from index 0 and paint the cell in
# mat containing the integer arr[i].
#
# Return the smallest index i at which either a row or a column will be
# completely painted in mat.
#
#
# Example 1:
#
#
# Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
# Output: 2
# Explanation: The moves are shown in order, and both the first row and second
# column of the matrix become fully painted at arr[2].
#
#
# Example 2:
#
#
# Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
# Output: 3
# Explanation: The second column becomes fully painted at arr[3].
#
#
#
# Constraints:
#
#
# m == mat.length
# n = mat[i].length
# arr.length == m * n
# 1 <= m, n <= 10^5
# 1 <= m * n <= 10^5
# 1 <= arr[i], mat[r][c] <= m * n
# All the integers of arr are unique.
# All the integers of mat are unique.
#
#
#


# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Approach 1: Brute Force
        # Time: O(m*n * (m * n)) where m is the number of rows and n is the number of columns
        # Space: O(m*n) to store the number of painted cells in each row and column
        m, n = len(mat), len(mat[0])

        # painted = [[False] * n for _ in range(m)]

        # pos = (
        #     {}
        # )  # Store the position of each number in arr in the matrix mat (row, col )

        # for i in range(m):
        #     for j in range(n):
        #         pos[mat[i][j]] = (
        #             i,
        #             j,
        #         )  # This is a dictionary of the form {number: (row, col)}

        # # Process the array arr
        # for i, num in enumerate(arr):
        #     r, c = pos[num]
        #     painted[r][c] = True

        #     # Check if the row is completely painted
        #     if all(painted[r][col] for col in range(n)):
        #         return i

        #     # Check if the column is completely painted
        #     if all(painted[row][c] for row in range(m)):
        #         return i

        # return -1  # If no row or column is completely painted

        # Approach 2: Optimized Approach of Brute Force
        # Time: O(m*n) where m is the number of rows and n is the number of columns
        # Space: O(m*n) to store the number of painted cells in each row and column
        # for r in range(m):
        #     for c in range(n):
        #         pos[mat[r][c]] = (r, c)

        # row_painted = [0] * m
        # col_painted = [0] * n

        # for i, num in enumerate(arr):
        #     r, c = pos[num]
        #     row_painted[r] += 1
        #     col_painted[c] += 1

        #     if row_painted[r] == n or col_painted[c] == m:
        #         return i  # If either row or column is completely painted

        # return -1  # If no row or column is completely painted

        # Approach 3: Reverse Mapping
        # Precompute the turn at which each number is painted
        # Time: O(m*n) where m is the number of rows and n is the number of columns
        # Space: O(m*n) to store the turn at which each number is painted
        turn = {}
        for i, num in enumerate(arr):
            turn[num] = i

        # For each row, compute the turn when the row is fully painted.
        min_row_turn = float("inf")
        for r in range(m):
            # The row will be complete only after the last cell is painted.
            row_turn = max(turn[mat[r][c]] for c in range(n))
            min_row_turn = min(min_row_turn, row_turn)

        # For each column, compute the turn when the column is fully painted.
        min_col_turn = float("inf")
        for c in range(n):
            col_turn = max(turn[mat[r][c]] for r in range(m))
            min_col_turn = min(min_col_turn, col_turn)

        # The overall answer is the earliest (smallest index) when a row or column is complete.
        return min(min_row_turn, min_col_turn)


# @lc code=end
