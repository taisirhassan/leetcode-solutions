#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (75.20%)
# Likes:    2180
# Dislikes: 65
# Total Accepted:    144.2K
# Total Submissions: 173.5K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# We run a preorder depth-first search (DFS) on the root of a binary tree.
# 
# At each node in this traversal, we output D dashes (where D is the depth of
# this node), then we output the value of this node.  If the depth of a node is
# D, the depth of its immediate child is D + 1.  The depth of the root node is
# 0.
# 
# If a node has only one child, that child is guaranteed to be the left child.
# 
# Given the output traversal of this traversal, recover the tree and return its
# root.
# 
# 
# Example 1:
# 
# 
# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# 
# 
# Example 2:
# 
# 
# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# 
# 
# Example 3:
# 
# 
# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 10^9
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Approach 1: Using Stack
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        # stack = [] # stack to store the (node, depth) tuple
        # i = 0
        # n = len(traversal) 
        
        # while i < n:
        #     depth = 0
        #     # count the number of dashes to get the depth
        #     while i < n and traversal[i] == '-':
        #         depth += 1
        #         i += 1
            
        #     # parse the numeric value of the node
        #     value = 0
        #     while i < n and traversal[i].isdigit():
        #         # parse the numeric value of the node 
        #         value = value * 10 + int(traversal[i])
        #         i += 1
                
        #     # create a new node with the parsed value 
        #     node = TreeNode(value)
            
        #     # if the stack's size is larger than the current depth, then pop the stack until the stack's size is equal to the current depth
        #     while len(stack) > depth:
        #         stack.pop()
            
        #     # if the stack isn't empty, attach current node as a child 
        #     if stack:
        #         parent = stack[-1] 
        #         # if left child is not set, set the left child as current node 
        #         if not parent.left:
        #             parent.left = node
        #         else:
        #             parent.right = node
            
        #     # push the current node along with the depth to the stack
        #     stack.append(node) 
            
        # # the stack will have the root node at the end, so return the root node
        # while len(stack) > 1:
        #     stack.pop() 
            
        # return stack[0] 
        
        
        # Approach 2: Recursive DFS 
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        
        def dfs(index: int, expected_depth: int) -> Tuple[Optional[TreeNode], int]:
            n = len(traversal)
            i = index 
            depth = 0
            
            # count the number of dashes to get the depth
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # if the depth is not equal to the expected depth, then return None    
            if depth != expected_depth:
                return None, index
            
            # parse the numeric value of the node
            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
                
            # create a new node with the parsed value
            node = TreeNode(value)
            
            # recursively build the left subtree, the expected depth is the current depth + 1
            node.left, i = dfs(i, expected_depth + 1)

            node.right, i = dfs(i, expected_depth + 1)

            return node, i
        
        root, _ = dfs(0, 0)
        return root

