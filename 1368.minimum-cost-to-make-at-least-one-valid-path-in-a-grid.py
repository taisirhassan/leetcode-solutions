#
# @lc app=leetcode id=1368 lang=python3
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/
#
# algorithms
# Hard (62.60%)
# Likes:    1887
# Dislikes: 21
# Total Accepted:    59.9K
# Total Submissions: 93.6K
# Testcase Example:  '[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]'
#
# Given an m x n grid. Each cell of the grid has a sign pointing to the next
# cell you should visit if you are currently in this cell. The sign of
# grid[i][j] can be:
#
#
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to
# grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to
# grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i +
# 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i -
# 1][j])
#
#
# Notice that there could be some signs on the cells of the grid that point
# outside the grid.
#
# You will initially start at the upper left cell (0, 0). A valid path in the
# grid is a path that starts from the upper left cell (0, 0) and ends at the
# bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
# path does not have to be the shortest.
#
# You can modify the sign on a cell with cost = 1. You can modify the sign on a
# cell one time only.
#
# Return the minimum cost to make the grid have at least one valid path.
#
#
# Example 1:
#
#
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
# change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) -->
# (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2,
# 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
#
#
# Example 2:
#
#
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
#
#
# Example 3:
#
#
# Input: grid = [[1,2],[4,3]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# 1 <= grid[i][j] <= 4
#
#
#


# @lc code=start
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Approach 1: Dijkstra's Algorithm
        # Time Complexity: O(m*n*log(m*n))
        # Space Complexity: O(m*n)
        m, n = len(grid), len(grid[0])  # m = rows, n = columns

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

        cost = [
            [float("inf")] * n for _ in range(m)
        ]  # cost to reach (i, j) is stored in cost[i][j]
        cost[0][0] = 0  # cost to reach (0, 0) is 0

        # # Priority Queue to store the cells to be visited in the order of cost (current_cost, i, j)
        # pq = [(0, 0, 0)]

        # while pq:
        #     current_cost, i, j = heapq.heappop(
        #         pq
        #     )  # pop the cell with minimum cost from the priority queue

        #     # If we have already found a better way, skip.
        #     if current_cost > cost[i][j]:
        #         continue

        #     for direction, (di, dj) in enumerate(
        #         moves
        #     ):  # explore all the possible directions from the current cell (i, j)
        #         ni, nj = i + di, j + dj
        #         if (
        #             0 <= ni < m and 0 <= nj < n
        #         ):  # check if the next cell (ni, nj) is within the grid
        #             extra_cost = (
        #                 0 if grid[i][j] == direction + 1 else 1
        #             )  # calculate the extra cost to change the direction
        #             new_cost = current_cost + extra_cost
        #             if new_cost < cost[ni][nj]:
        #                 cost[ni][nj] = new_cost
        #                 heapq.heappush(pq, (new_cost, ni, nj))

        # return cost[m - 1][
        #     n - 1
        # ]  # return the cost to reach the bottom-right cell (m-1, n-1)

        # Approach 2: 0-1 BFS
        # Initialize deque for 0-1 BFS.
        dq = deque()  # deque is used to pop the front element in O(1) time complexity
        dq.append((0, 0))  # start from the top-left cell (0, 0) with cost 0

        while dq:
            i, j = dq.popleft()  # pop the front element from the deque

            for direction, (di, dj) in enumerate(
                moves, start=1
            ):  # explore all the possible directions from the current cell (i, j)
                ni, nj = i + di, j + dj

                # check if the next cell (ni, nj) is within the grid
                if 0 <= ni < m and 0 <= nj < n:
                    extra_cost = 0 if grid[i][j] == direction else 1
                    new_cost = cost[i][j] + extra_cost

                    # If we can reach the neighbor with a lower cost then update and add to deque.
                    if new_cost < cost[ni][nj]:
                        cost[ni][nj] = new_cost
                        if extra_cost == 0:
                            # If no cost, add the neighbor to the front.
                            dq.appendleft((ni, nj))
                        else:
                            # If cost, add the neighbor to the back.
                            dq.append((ni, nj))

        return cost[m - 1][
            n - 1
        ]  # return the cost to reach the bottom-right cell (m-1, n-1)


# @lc code=end
