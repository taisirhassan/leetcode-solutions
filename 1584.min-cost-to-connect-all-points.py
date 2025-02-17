#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
#
# algorithms
# Medium (67.98%)
# Likes:    5239
# Dislikes: 136
# Total Accepted:    351.4K
# Total Submissions: 514.7K
# Testcase Example:  '[[0,0],[2,2],[3,10],[5,2],[7,0]]'
#
# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
# distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
# absolute value of val.
#
# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.
#
#
# Example 1:
#
#
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
#
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
#
#
# Example 2:
#
#
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.
#
#
#


# @lc code=start
class DSU:
    def __init__(self, n: int):
        # Parent array for union-find
        self.parent = list(range(n))
        # Rank array for union by rank
        self.rank = [0] * n

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # Union by rank; returns True if union was successful (i.e., x and y were in different sets)
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False

        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Approach 1: Prim's Algorithm
        # Time: O(n^2 log n)
        # Space: O(n)
        # number of points
        # n = len(points)
        # # if there is only one point, return 0
        # if n <= 1:
        #     return 0

        # def manhattan(i: int, j: int) -> int:
        #     return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # # array to keep track of whether a point is in the minimum spanning tree
        # in_mst = [False] * n

        # # heap stores tuples of (cost, point_index)
        # min_heap = [(0, 0)]

        # total_cost = 0

        # count = 0  # number of points in the minimum spanning tree
        # while count < n:
        #     # get smallest cost edge from heap
        #     cost, i = heapq.heappop(min_heap)
        #     # if point is already in the mst, skip
        #     if in_mst[i]:
        #         continue
        #     # mark point as in the mst and add cost to total cost
        #     in_mst[i] = True
        #     total_cost += cost
        #     count += 1
        #     # for each point not in the mst, add the manhattan distance to the heap
        #     for j in range(n):
        #         if not in_mst[j]:
        #             heapq.heappush(min_heap, (manhattan(i, j), j))
        # return total_cost

        # Approach 2: Kruskal's Algorithm
        # Time: O(n^2 log n)
        # Space: O(n)
        n = len(points)
        if n <= 1:
            return 0
        # Build a list of all edges with their Manhattan distances
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the Manhattan distance between points i and j
                cost = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                edges.append((cost, i, j))

        # Sort the edges by cost
        edges.sort(key=lambda x: x[0])

        dsu = DSU(n)
        total_cost = 0
        edges_used = 0

        # process edges in increasing order
        for cost, u, v in edges:
            # If u and v are not connected, add the edge to the MST
            if dsu.union(u, v):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost


# @lc code=end
