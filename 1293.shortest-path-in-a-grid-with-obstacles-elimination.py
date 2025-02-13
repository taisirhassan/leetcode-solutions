#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
#
# algorithms
# Hard (45.41%)
# Likes:    4628
# Dislikes: 86
# Total Accepted:    230.4K
# Total Submissions: 506.7K
# Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
#
# You are given an m x n integer matrix grid where each cell is either 0
# (empty) or 1 (obstacle). You can move up, down, left, or right from and to an
# empty cell in one step.
#
# Return the minimum number of steps to walk from the upper left corner (0, 0)
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most
# k obstacles. If it is not possible to find such walk return -1.
#
#
# Example 1:
#
#
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation:
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such
# path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a
# walk.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
#
#
#


# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Approach 1: BFS with a queue of (x, y, k, steps) tuples
        # Time: O(m*n*k)
        # Space: O(m*n*k)
        # m, n = len(grid), len(grid[0])

        # # Early optimization: if k is large enough to cover any obstacles on a Manhattan path.
        # if k >= m + n - 2:
        #     return m + n - 2

        # # 3D visited array: visited[x][y][rem] indicates if cell (x,y) has been visited with rem eliminations left.
        # visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

        # # Queue for BFS: each state is (x, y, remaining eliminations, steps)
        # dq = deque()
        # dq.append((0, 0, k, 0))
        # visited[0][0][k] = True

        # # Four possible directions: down, up, right, left.
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # # BFS loop.
        # while dq:
        #     x, y, rem, steps = dq.popleft()

        #     # If we've reached the destination, return the steps.
        #     if x == m - 1 and y == n - 1:
        #         return steps

        #     # Explore neighbors.
        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
        #         # Check bounds.
        #         if 0 <= nx < m and 0 <= ny < n:
        #             new_rem = rem
        #             # If next cell is an obstacle.
        #             if grid[nx][ny] == 1:
        #                 if new_rem > 0:
        #                     new_rem -= 1
        #                 else:
        #                     continue  # Can't proceed if no eliminations remain.

        #             # Visit this new state if not visited.
        #             if not visited[nx][ny][new_rem]:
        #                 visited[nx][ny][new_rem] = True
        #                 dq.append((nx, ny, new_rem, steps + 1))

        # # Destination unreachable.
        # return -1
        # Approach 2: A* Search with a priority queue
        # Time: O(m*n*k log(m*n*k))
        # Space: O(m*n*k)
        # m, n = len(grid), len(grid[0])

        # # Early optimization.
        # if k >= m + n - 2:
        #     return m + n - 2

        # # 3D visited array.
        # visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

        # # Heuristic function: Manhattan distance from (x, y) to destination.
        # def heuristic(x: int, y: int) -> int:
        #     return (m - 1 - x) + (n - 1 - y)

        # # Priority queue: elements are (f, steps, x, y, remaining eliminations)
        # pq = []
        # heapq.heappush(pq, (heuristic(0, 0), 0, 0, 0, k))
        # visited[0][0][k] = True

        # # Four possible directions.
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # while pq:
        #     f, steps, x, y, rem = heapq.heappop(pq)

        #     # Destination reached.
        #     if x == m - 1 and y == n - 1:
        #         return steps

        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < m and 0 <= ny < n:
        #             new_rem = rem
        #             if grid[nx][ny] == 1:
        #                 if new_rem > 0:
        #                     new_rem -= 1
        #                 else:
        #                     continue
        #             if not visited[nx][ny][new_rem]:
        #                 visited[nx][ny][new_rem] = True
        #                 new_steps = steps + 1
        #                 new_f = new_steps + heuristic(nx, ny)
        #                 heapq.heappush(pq, (new_f, new_steps, nx, ny, new_rem))

        # return -1
        


# @lc code=end
