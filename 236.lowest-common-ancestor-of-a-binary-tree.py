#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (64.89%)
# Likes:    17317
# Dislikes: 451
# Total Accepted:    2M
# Total Submissions: 3.1M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Approach 1: Recursive DFS 
        # Time Complexity: O(N)
        # Space Complexity: O(N) due to recursion stack
        # # base caseL if the current node is None or matches p or q, return it
        # if root is None or root == p or root == q:
        #     return root 
        
        # # recurse on the left and right subtrees
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        
        # # if both left and right are not None, then this current node is the LCA
        # if left and right:
        #     return root 
        
        # # otherwise, return the non-None node
        # return left if left else right 
        
        # Approach 2: Iterative using parent pointers
        # dictionary to store parent pointers 
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        parent = {root: None}
        stack = [root]
        
        # traverse the tree until we find both p and q
        while p not in parent or q not in parent:
            node = stack.pop()
            
            # if left child exists, record its parent and add to stack 
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            # same for right child
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        # create a set to store ancestors of p and q 
        ancestors = set()
        # traverse from p to root and add all ancestors
        while p:
            ancestors.add(p)
            p = parent[p]
        
        # traverse from q to root and check if any ancestor is in the p's ancestor set     
        while q not in ancestors:
            q = parent[q]
            
        return q    
        
# @lc code=end

