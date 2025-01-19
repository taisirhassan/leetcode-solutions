#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (48.62%)
# Likes:    4349
# Dislikes: 132
# Total Accepted:    161.3K
# Total Submissions: 279K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n integer matrix heightMap representing the height of each unit
# cell in a 2D elevation map, return the volume of water it can trap after
# raining.
#
#
# Example 1:
#
#
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small ponds 1 and 3 units trapped.
# The total volume of water trapped is 4.
#
#
# Example 2:
#
#
# Input: heightMap =
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
#
#
#
# Constraints:
#
#
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4
#
#
#


# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Approach BFS + Priority Queue (Heap)
        # Time Complexity: O(m*n*log(m*n))
        # Space Complexity: O(m*n)
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])  # m: row, n: col
        visited = [[False] * n for _ in range(m)]  # Mark the visited cells
        heap = []  # (height, i, j) tuple to store the height and position

        for i in range(m):
            for j in range(n):
                if (
                    i == 0 or i == m - 1 or j == 0 or j == n - 1
                ):  # Border cells are useless for trapping water
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        total_water = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

        while heap:
            height, i, j = heapq.heappop(
                heap
            )  # Get the cell with the lowest height from the heap
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < m and 0 <= nj < n and not visited[ni][nj]
                ):  # Check if the neighbor is valid and not visited
                    visited[ni][nj] = True  # Mark the neighbor as visited
                    neighbor_height = heightMap[ni][nj]
                    # If the current cell's height is taller than the neighbor, water is trapped.
                    trapped = max(0, height - neighbor_height)
                    total_water += trapped
                    # The new effective height is the maximum of neighbor's height and the current water level.
                    new_height = max(height, neighbor_height)
                    # Push the new cell to the heap with the new effective height.
                    heapq.heappush(heap, (new_height, ni, nj))

        return total_water


# @lc code=end
