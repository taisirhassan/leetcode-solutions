#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (54.58%)
# Likes:    9144
# Dislikes: 140
# Total Accepted:    601.9K
# Total Submissions: 1.1M
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
#
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
#
#
# Example 1:
#
#
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
#
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
#
#
# Example 3:
#
#
# Input: matrix = [[1]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Approach 1: DFS With Memoization
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        # edge case: if the matrix is empty
        # if not matrix or not matrix[0]:
        #     return 0
        # m, n = len(matrix), len(matrix[0])
        # # dp[i][j] will store the longest path starting from cell (i,j)
        # dp = [[0] * n for _ in range(m)]

        # # directions: right, left, down, up
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def dfs(i: int, j: int) -> int:
        #     # if the result is already calculated, return it
        #     if dp[i][j] != 0:
        #         return dp[i][j]
        #     max_path = 1  # the cell itself counts as length 1
        #     # explore neighbours
        #     for dx, dy in directions:
        #         ni, nj = i + dx, j + dy
        #         # check bounds and if neighbour is greater than current cell
        #         if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
        #             max_path = max(max_path, 1 + dfs(ni, nj))
        #     # store the result in dp
        #     dp[i][j] = max_path
        #     return dp[i][j]

        # # compute the maximum path from any cell
        # result = 0
        # for i in range(m):
        #     for j in range(n):
        #         result = max(result, dfs(i, j))
        # return result

        # Approach 2: Topological Sort (Peeling Onion)
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # outdegree[i][j] represents the number of valid moves from cell (i,j)
        outdegree = [[0] * n for _ in range(m)]

        # directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # compute outdegrees for each cell
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        outdegree[i][j] += 1
        # initialize queue with cells with outdegree 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if outdegree[i][j] == 0:
                    queue.append((i, j))

        # Layer-by-layer peeling (BFS)
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # explore neighbours that could reach (i,j)
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                        outdegree[ni][nj] -= 1
                        # if no more valid moves from neighbour add it to the queue
                        if outdegree[ni][nj] == 0:
                            queue.append((ni, nj))

        # The number of levels is the length of the longest increasing path
        return level


# @lc code=end
