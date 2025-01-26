#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#
# https://leetcode.com/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (60.92%)
# Likes:    1833
# Dislikes: 103
# Total Accepted:    180.5K
# Total Submissions: 246.1K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given a map of a server center, represented as a m * n integer matrix
# grid, where 1 means that on that cell there is a server and 0 means that it
# is no server. Two servers are said to communicate if they are on the same row
# or on the same column.
#
# Return the number of servers that communicate with any other server.
#
#
# Example 1:
#
#
#
#
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
#
# Example 2:
#
#
#
#
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other
# server.
#
#
# Example 3:
#
#
#
#
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each
# other. The two servers in the third column can communicate with each other.
# The server at right bottom corner can't communicate with any other
# server.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
#
#
#


# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(m*n * (m+n))
        # Space Complexity: O(1)

        m, n = len(grid), len(grid[0])
        # communicating_servers = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             can_communicate = False
        #             # Check Row
        #             for k in range(n):
        #                 if grid[i][k] == 1 and k != j:
        #                     can_communicate = True
        #                     break
        #                 # If not found in row, check the column
        #             if not can_communicate:
        #                 for k in range(m):
        #                     if grid[k][j] == 1 and k != i:
        #                         can_communicate = True
        #                         break
        #             if can_communicate:
        #                 communicating_servers += 1
        # return communicating_servers

        # Approach 2: Optimized Counting Using Row and Column Count Array
        # Time Complexity: O(m*n)
        # Space Complexity: O(m+n)
        row_count = [0] * m  # Count of servers in each row
        col_count = [0] * n  # Count of servers in each column

        # First Pass: Count the number of servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        communicating_servers = 0

        # Second Pass: Count the number of servers that can communicate with other servers in the same row or column
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        communicating_servers += 1
        return communicating_servers


# @lc code=end
