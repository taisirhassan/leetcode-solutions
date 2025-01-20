#
# @lc app=leetcode id=1730 lang=python3
#
# [1730] Shortest Path to Get Food
#
# https://leetcode.com/problems/shortest-path-to-get-food/description/
#
# algorithms
# Medium (55.41%)
# Likes:    703
# Dislikes: 41
# Total Accepted:    74.4K
# Total Submissions: 132.5K
# Testcase Example:  '[["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]'
#
# You are starving and you want to eat food as quickly as possible. You want to
# find the shortest path to arrive at any food cell.
#
# You are given an m x n character matrix, grid, of these different types of
# cells:
#
#
# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
#
#
# You can travel to any adjacent cell north, east, south, or west of your
# current location if there is not an obstacle.
#
# Return the length of the shortest path for you to reach any food cell. If
# there is no path for you to reach food, return -1.
#
#
# Example 1:
#
#
# Input: grid =
# [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
#
#
# Example 2:
#
#
# Input: grid =
# [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
#
#
# Example 3:
#
#
# Input: grid =
# [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach
# the bottom food.
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[row][col] is '*', 'X', 'O', or '#'.
# The grid contains exactly one '*'.
#
#
#


# @lc code=start
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Approach 1: BFS
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        # m, n = len(grid), len(grid[0])  # m: row, n: col
        # start = None  # Start position of the player '*'

        # # Find the start position of the player '*'
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "*":
        #             start = (i, j)
        #             break
        #     if start:  # Found the start position of the player '*'
        #         break

        # if not start:
        #     return -1  # No start position found

        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        # visited = [[False] * n for _ in range(m)]
        # queue = deque()

        # si, sj = start
        # queue.append((si, sj, 0))  # (i, j, steps) tuple to store the position and steps
        # visited[si][sj] = True

        # while queue:
        #     i, j, steps = queue.popleft()  # Dequeue the front cell from the queue

        #     # Check if the current cell is a food cell '#'
        #     if grid[i][j] == "#":
        #         return steps

        #     # Visit all adjacent cells of the current cell
        #     for di, dj in directions:
        #         ni, nj = i + di, j + dj
        #         if (
        #             0 <= ni < m
        #             and 0 <= nj < n
        #             and not visited[ni][nj]
        #             and grid[ni][nj] != "X"
        #         ):
        #             visited[ni][nj] = True
        #             queue.append((ni, nj, steps + 1))

        # return -1  # No path found to reach the food cell

        # Approach 2: A* Search Algorithm (Heuristic Search)
        m, n = len(grid), len(grid[0])
        start = None
        foods = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    start = (i, j)
                elif grid[i][j] == "#":
                    foods.append((i, j))

        if not start or not foods:
            return -1  # No start position or food position found

        # Helper function to calculate the Manhattan distance between two points (i1, j1) and (i2, j2)
        def heuristic(i, j):
            return min(
                abs(i - fi) + abs(j - fi) for fi, fj in foods
            )  # Manhattan distance between the current cell and the nearest food cell

        # The priority queue stores tuples: (f, steps, i, j)
        # where f = steps + heuristic(i, j)

        # The priority queue is used to store the cells to visit in the order of the total cost f = steps + heuristic(i, j)
        # where steps is the number of steps taken so far and heuristic(i, j) is the estimated number of steps to reach the nearest food cell from the current cell (i, j).
        heap = []
        si, sj = start
        initial_h = heuristic(
            si, sj
        )  # Initial heuristic value for the start position of the player '*'
        heapq.heappush(
            heap, (initial_h, 0, si, sj)
        )  # (f, steps, i, j) tuple to store the total cost, steps, and position
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        while heap:
            f, steps, i, j = heapq.heappop(
                heap
            )  # Dequeue the cell with the minimum total cost f from the priority queue
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < m
                    and 0 <= nj < n
                    and (ni, nj) not in visited
                    and grid[ni][nj] != "X"
                ):
                    # If food is found, return the total steps taken
                    if grid[ni][nj] == "#":
                        return steps + 1

                    visited.add((ni, nj))
                    new_steps = steps + 1
                    new_f = new_steps + heuristic(ni, nj)
                    heapq.heappush(heap, (new_f, new_steps, ni, nj))

        return -1  # No path found to reach the food cell


# @lc code=end
