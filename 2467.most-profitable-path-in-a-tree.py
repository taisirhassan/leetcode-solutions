#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#
# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
#
# algorithms
# Medium (49.57%)
# Likes:    757
# Dislikes: 80
# Total Accepted:    15.8K
# Total Submissions: 31.5K
# Testcase Example:  '[[0,1],[1,2],[1,3],[3,4]]\n3\n[-2,4,2,-4,6]'
#
# There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at
# node 0. You are given a 2D integer array edges of length n - 1 where edges[i]
# = [ai, bi] indicates that there is an edge between nodes ai and bi in the
# tree.
# 
# At every node i, there is a gate. You are also given an array of even
# integers amount, where amount[i] represents:
# 
# 
# the price needed to open the gate at node i, if amount[i] is negative,
# or,
# the cash reward obtained on opening the gate at node i, otherwise.
# 
# 
# The game goes on as follows:
# 
# 
# Initially, Alice is at node 0 and Bob is at node bob.
# At every second, Alice and Bob each move to an adjacent node. Alice moves
# towards some leaf node, while Bob moves towards node 0.
# For every node along their path, Alice and Bob either spend money to open the
# gate at that node, or accept the reward. Note that:
# 
# If the gate is already open, no price will be required, nor will there be any
# cash reward.
# If Alice and Bob reach the node simultaneously, they share the price/reward
# for opening the gate there. In other words, if the price to open the gate is
# c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the
# gate is c, both of them receive c / 2 each.
# 
# 
# If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches
# node 0, he stops moving. Note that these events are independent of each
# other.
# 
# 
# Return the maximum net income Alice can have if she travels towards the
# optimal leaf node.
# 
# 
# Example 1:
# 
# 
# Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
# Output: 6
# Explanation: 
# The above diagram represents the given tree. The game goes as follows:
# - Alice is initially on node 0, Bob on node 3. They open the gates of their
# respective nodes.
# ⁠ Alice's net income is now -2.
# - Both Alice and Bob move to node 1. 
# Since they reach here simultaneously, they open the gate together and share
# the reward.
# Alice's net income becomes -2 + (4 / 2) = 0.
# - Alice moves on to node 3. Since Bob already opened its gate, Alice's income
# remains unchanged.
# Bob moves on to node 0, and stops moving.
# - Alice moves on to node 4 and opens the gate there. Her net income becomes 0
# + 6 = 6.
# Now, neither Alice nor Bob can make any further moves, and the game ends.
# It is not possible for Alice to get a higher net income.
# 
# 
# Example 2:
# 
# 
# Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
# Output: -7280
# Explanation: 
# Alice follows the path 0->1 whereas Bob follows the path 1->0.
# Thus, Alice opens the gate at node 0 only. Hence, her net income is
# -7280. 
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.
# 1 <= bob < n
# amount.length == n
# amount[i] is an even integer in the range [-10^4, 10^4].
# 
# 
#

# @lc code=start
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Approach 1: DFS with memoization
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        # n = len(amount)
        # graph = [[] for _ in range(n)]
        
        # for u,v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)  
            
        # # array to rcord the parent of each node from dfs starting at root
        # parent = [-1]*n
        
        # def dfs(u:int, par: int):
        #     parent[u] = par
        #     for v in graph[u]:
        #         if v== par:
        #             continue
        #         dfs(v,u)
                
        # dfs(0,-1)
        
        # # bob's timeline: for each node, the time it takes for bob to reach the node
        # # for nodes bob never reaches, time is inf
        
        # bob_time = [float('inf')]*n
        # t = 0 
        # node = bob
        # while node != -1:
        #     bob_time[node] = t
        #     node = parent[node]
        #     t+=1
            
        # # dfs for alice: simulate her journey from root to every leaf
        # best_profit = -float('inf')
        
        # def dfs_alice(u:int, time_alice: int, current_profit: int, par: int):
        #     nonlocal best_profit
        #     # decide how much profit to add at node u based on arrival times of alice and bob
        #     if time_alice < bob_time[u]:
        #         current_profit += amount[u] # alice reaches before bob
        #     elif time_alice == bob_time[u]:
        #         current_profit += amount[u]//2 # alice and bob reach together, they share the profit
        #     # else: bob reaches before alice, no profit to add
        #     # if u is a leaf, update the best profit
        #     if u != 0 and len(graph[u]) == 1:
        #         best_profit = max(best_profit, current_profit)
                
        #     # recurse to children
        #     for v in graph[u]:
        #         if v == par:
        #             continue
        #         dfs_alice(v, time_alice+1, current_profit, u)

        # dfs_alice(0, 0, 0, -1)
        
        # return best_profit
        
        # Approach 2: BFS + DFS
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        n = len(amount)
        
        adj = [[] for _ in range(n)] # adjacency list
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # step 2: bfs to compute distances and parents
        dist = [-1] * n 
        parent = [-1] * n
        queue = deque([0])
        dist[0] = 0 
        
        while queue:
            node = queue.popleft()
            for neighbour in adj[node]:
                if dist[neighbour] == -1: # unvisited
                    dist[neighbour] = dist[node] + 1
                    parent[neighbour] = node
                    queue.append(neighbour)
        # step 3: trace bob's path from bob to 0
        P = []
        current = bob 
        while current != -1:
            P.append(current)
            current = parent[current] # P is the path from bob to 0
            
        # step 4: modify amounts based on alice and bob's timings
        modified_amount = amount.copy() 
        for i in range(len(P)):
            v = P[i] 
            if dist[v] > i: # bob reaches before alice
                modified_amount[v] = 0
            elif dist[v] == i: # alice and bob reach together
                modified_amount[v] //= 2      
                
        # step 5: dfs to compute the best profit to a leaf node
        def dfs(node, parent):
            # get sums for all children except parent 
            children_sum = [dfs(child,node) for child in adj[node] if child != parent]
            if not children_sum: # leaf node
                return modified_amount[node]
            return modified_amount[node] + max(children_sum) # best profit to a leaf node
        return dfs(0,-1) # start dfs from root node
        
# @lc code=end

