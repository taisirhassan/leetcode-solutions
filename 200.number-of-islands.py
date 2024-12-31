#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (61.05%)
# Likes:    23323
# Dislikes: 545
# Total Accepted:    3.1M
# Total Submissions: 5.1M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Edge case: empty grid
        if not grid or not grid[0]:
            return 0

        # Initialize the number of islands
        num_islands = 0
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Approach 1: Depth-First Search (DFS)

        # # Define the DFS function
        # def dfs(i, j):
        #     # Base case: if the current cell is out of bounds or is water, return
        #     if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
        #         return
        #     # Mark current cell as visited by setting it to '0'
        #     grid[i][j] = "0"
        #     # Recursively call DFS on the neighboring cells (up, down, left, right)
        #     dfs(i + 1, j)
        #     dfs(i - 1, j)
        #     dfs(i, j + 1)
        #     dfs(i, j - 1)

        # # Iterate through each cell in the grid
        # for i in range(m):
        #     for j in range(n):
        #         # If the current cell is land, perform DFS to explore the island
        #         if grid[i][j] == "1":
        #             num_islands += 1
        #             dfs(i, j)  # Mark all connected land cells as visited

        # return num_islands

        # Approach 2: Breadth-First Search (BFS)
        # Time complexity: O(m * n) where m is the number of rows and n is the number of columns
        # Space complexity: O(min(m, n)) as the queue can contain at most min(m, n) elements

        # Define directions for adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If the cell is land, perform BFS
                if grid[i][j] == "1":
                    num_islands += 1  # Found a new island
                    grid[i][j] = "0"  # Mark as visited
                    queue = deque([(i, j)])  # Initialize BFS queue

                    while queue:
                        x, y = queue.popleft()
                        # Check all adjacent cells
                        for dx, dy in directions:
                            new_x, new_y = x + dx, y + dy
                            # If adjacent cell is land, mark it and add to queue
                            if (
                                0 <= new_x < m
                                and 0 <= new_y < n
                                and grid[new_x][new_y] == "1"
                            ):
                                grid[new_x][new_y] = "0"
                                queue.append((new_x, new_y))

        return num_islands


# @lc code=end
