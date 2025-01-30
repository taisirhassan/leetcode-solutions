#
# @lc app=leetcode id=2493 lang=python3
#
# [2493] Divide Nodes Into the Maximum Number of Groups
#
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/description/
#
# algorithms
# Hard (40.38%)
# Likes:    507
# Dislikes: 33
# Total Accepted:    16.5K
# Total Submissions: 33.8K
# Testcase Example:  '6\n[[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]'
#
# You are given a positive integer n representing the number of nodes in an
# undirected graph. The nodes are labeled from 1 to n.
#
# You are also given a 2D integer array edges, where edges[i] = [ai, bi]
# indicates that there is a bidirectional edge between nodes ai and bi. Notice
# that the given graph may be disconnected.
#
# Divide the nodes of the graph into m groups (1-indexed) such that:
#
#
# Each node in the graph belongs to exactly one group.
# For every pair of nodes in the graph that are connected by an edge [ai, bi],
# if ai belongs to the group with index x, and bi belongs to the group with
# index y, then |y - x| = 1.
#
#
# Return the maximum number of groups (i.e., maximum m) into which you can
# divide the nodes. Return -1 if it is impossible to group the nodes with the
# given conditions.
#
#
# Example 1:
#
#
# Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
# Output: 4
# Explanation: As shown in the image we:
# - Add node 5 to the first group.
# - Add node 1 to the second group.
# - Add nodes 2 and 4 to the third group.
# - Add nodes 3 and 6 to the fourth group.
# We can see that every edge is satisfied.
# It can be shown that that if we create a fifth group and move any node from
# the third or fourth group to it, at least on of the edges will not be
# satisfied.
#
#
# Example 2:
#
#
# Input: n = 3, edges = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: If we add node 1 to the first group, node 2 to the second group,
# and node 3 to the third group to satisfy the first two edges, we can see that
# the third edge will not be satisfied.
# It can be shown that no grouping is possible.
#
#
#
# Constraints:
#
#
# 1 <= n <= 500
# 1 <= edges.length <= 10^4
# edges[i].length == 2
# 1 <= ai, bi <= n
# ai != bi
# There is at most one edge between any pair of vertices.
#
#
#


# @lc code=start
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]  # Using 1-based indexing
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n + 1)  # Track visited nodes
        total_groups = 0  # Accumulate the total number of groups

        # Process each node to find connected components
        for node in range(1, n + 1):
            if not visited[node]:
                # Collect all nodes in the current connected component using BFS
                component = []
                queue = deque([node])
                visited[node] = True
                while queue:
                    u = queue.popleft()
                    component.append(u)
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            queue.append(v)

                # Check if the component is bipartite using BFS again
                is_bipartite = True
                color = [-1] * (n + 1)  # -1 indicates coloured, 0/1 are colours
                start = component[0]  # Start BFS from the first node in the component
                color[start] = 0
                q = deque([start])
                while q and is_bipartite:
                    u = q.popleft()
                    for v in adj[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]  # Assign alternate colour
                            q.append(v)
                        elif color[v] == color[u]:
                            # Adjacent nodes have the same colour: component is not bipartite
                            is_bipartite = False
                            break  # No need to check further
                # If any component is not bipartite, return -1 immediately
                if not is_bipartite:
                    return -1

                # Compute the diameter of the component
                max_diameter = 0  # Track the max diameter found in the component
                # Perform BFS from node u to find the maximum distance to any other node
                for u in component:
                    # BFS to find the maximum distance from u
                    distance = [-1] * (n + 1)  # Distance from u to each node
                    q = deque([u])
                    distance[u] = 0
                    max_dist = 0  # Maximum distance from u in this BFS
                    while q:
                        current = q.popleft()
                        for neighbor in adj[current]:
                            if distance[neighbor] == -1:
                                distance[neighbor] = distance[current] + 1
                                max_dist = max(max_dist, distance[neighbor])
                                q.append(neighbor)
                    # Updat the component's diameter with the maximum distance found
                    max_diameter = max(max_diameter, max_dist)
                # The number of groups for this component is diameter + 1
                total_groups += max_diameter + 1

        return total_groups


# @lc code=end
