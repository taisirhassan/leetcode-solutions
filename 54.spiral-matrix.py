#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (52.19%)
# Likes:    15736
# Dislikes: 1405
# Total Accepted:    1.8M
# Total Submissions: 3.4M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#
#
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Approach 1: Brute Force Simulation DFS
        # Time complexity: O(m*n)
        # Space complexity: O(m*n)
        # if not matrix or not matrix[0]:
        #     return []
        # m, n = len(matrix), len(matrix[0])
        # result = []
        # # create a visited matrix
        # visited = [[False] * n for _ in range(m)]
        # # directions
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # # initial direction
        # d = 0  # start with moving right
        # i = j = 0

        # for _ in range(m * n):
        #     result.append(matrix[i][j])
        #     visited[i][j] = True

        #     # calculate the next position based on the current direction
        #     ni, nj = i + directions[d][0], j + directions[d][1]
        #     # check if the next position is within the boundary or visited, if it is change the direction
        #     if not (0 <= ni < m and 0 <= nj < n and not visited[ni][nj]):
        #         d = (d + 1) % 4  # rotate the direction
        #         ni, nj = i + directions[d][0], j + directions[d][1]

        #     i, j = ni, nj  # update the position

        # return result

        # Appproach 2: Layer-by-Layer
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # loop untill all boundaries have been processed
        while left <= right and top <= bottom:
            # top row
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            # right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            # bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            # left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


# @lc code=end
