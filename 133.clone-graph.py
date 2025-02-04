#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (60.31%)
# Likes:    9764
# Dislikes: 3963
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
# 
# Return a deep copy (clone) of the graph.
# 
# Each node in the graph contains a value (int) and a list (List[Node]) of its
# neighbors.
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
# 
# 
# 
# 
# Test case format:
# 
# For simplicity, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val == 1, the second node with
# val == 2, and so on. The graph is represented in the test case using an
# adjacency list.
# 
# An adjacency list is a collection of unordered lists used to represent a
# finite graph. Each list describes the set of neighbors of a node in the
# graph.
# 
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
# 
# 
# Example 1:
# 
# 
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
# 
# 
# Example 2:
# 
# 
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
# 
# 
# Example 3:
# 
# 
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Approach 1: Using DFS recursively to clone the graph
        # Time complexity: O(N + E) where N is the number of nodes and E is the number of edges
        # Space complexity: O(N) where N is the number of nodes
        
        # A dictionary to store the cloned nodes: key is the original node and value is the cloned node
        cloned_nodes = {}
        
        # def dfs(node):
        #     if not node:
        #         return None
            
        #     # If the node is already cloned, return the cloned node
        #     if node in cloned_nodes:
        #         return cloned_nodes[node]
            
        #     # Create a new node with the value of the original node
        #     cloned_node = Node(node.val)
            
        #     # Store the cloned node in the dictionary
        #     cloned_nodes[node] = cloned_node
            
        #     # For each neighbor of the original node, clone it and add it to the cloned node's neighbors recursively
        #     for neighbor in node.neighbors:
        #         cloned_neighbor = dfs(neighbor)
        #         cloned_node.neighbors.append(cloned_neighbor)
            
        #     return cloned_node
        
        # return dfs(node) # Return the cloned node of the input node
        
        # Approach 2: Using DFS iteratively to clone the graph
        # Time complexity: O(N + E) where N is the number of nodes and E is the number of edges
        # Space complexity: O(N) where N is the number of nodes
        
        # if not node:
        #     return None
        
        # # Initialize the stacck with the starting node
        # stack = [node]
        # # Clone the root node
        # cloned_nodes[node] = Node(node.val)
        
        # while stack:
        #     current = stack.pop()
        #     for neighbor in current.neighbors:
        #         if neighbor not in cloned_nodes:
        #             # Clone and add to stack for further processing
        #             cloned_nodes[neighbor] = Node(neighbor.val)
        #             stack.append(neighbor)
        #             # Add the cloned neighbor to the current node's clone's neighbors
        #         cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])
                
        # return cloned_nodes[node] # Return the cloned node of the input node
        
        # Approach 3: Using BFS to clone the graph
        # Time complexity: O(N + E) where N is the number of nodes and E is the number of edges
        # Space complexity: O(N) where N is the number of nodes
        if not node: 
            return None
        
        # Initialize the queue with the starting node
        queue = deque([node])
        # Clone the root node
        cloned_nodes[node] = Node(node.val)
        
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in cloned_nodes:
                    # Clone and add to queue for further processing
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Add the cloned neighbor to the current node's clone's neighbors
                cloned_nodes[current].neighbors.append(cloned_nodes[neighbor])
                
        return cloned_nodes[node] # Return the cloned node of the input node
        
        
        
# @lc code=end

