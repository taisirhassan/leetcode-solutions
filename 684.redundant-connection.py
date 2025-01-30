#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (63.79%)
# Likes:    6746
# Dislikes: 426
# Total Accepted:    505.7K
# Total Submissions: 767.3K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#
#
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
#
# Constraints:
#
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
#
#
#


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Approach 1: DFS (Depth First Search)
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)
        # Build the graph incrementally and check for cycles at each step
        # graph = defaultdict(list)  # Adjacency list representation of the graph

        # def dfs(current, target, visited):
        #     # DFS to check if a path exists between current and target
        #     if current == target:
        #         return True
        #     # Mark the current node as visited
        #     visited.add(current)
        #     # Visit all neighbors that have not been visited
        #     for neighbor in graph[current]:
        #         # If the neighbor has not been visited, recursively visit it
        #         if neighbor not in visited:
        #             # If a path is found between the neighbor and the target, return True
        #             if dfs(neighbor, target, visited):
        #                 return True
        #     # If no path is found between the current node and the target, return False
        #     return False

        # # Build the graph incrementally and check for cycles at each step
        # for u, v in edges:
        #     visited = set()
        #     # Check if u and v are already connected before adding the edge
        #     if dfs(u, v, visited):  # This edge forms a cycle
        #         return [u, v]
        #     # Add the edge to the graph if no cycle is detected
        #     graph[u].append(v)
        #     graph[v].append(u)

        # return []  # No redundant edge found in the graph

        n = len(edges)
        parent = list(
            range(n + 1)
        )  # Initialize the parent of each node as the node itself
        rank = [1] * (n + 1)  # Track the depth of each tree for union by rank

        def find(x: int) -> int:
            # Find the root of the tree
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression for faster lookup
            return parent[x]

        def union(x: int, y: int) -> bool:
            # Union by rank
            root_x, root_y = find(x), find(y)  # Find the root of each tree
            if root_x == root_y:  # If the nodes are already connected by the same root
                return False
            if (
                rank[root_x] > rank[root_y]
            ):  # Attach the smaller tree to the larger tree
                parent[root_y] = root_x
            else:
                parent[root_x] = (
                    root_y  # If the trees are of the same size, attach the second tree to the first tree
                )
                rank[root_y] += rank[root_x]  # Increase the rank of the second tree
            return True

        for u, v in edges:
            if not union(u, v):  # If the nodes are already connected by the same root
                return [u, v]


# @lc code=end
