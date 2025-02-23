#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (65.62%)
# Likes:    15636
# Dislikes: 556
# Total Accepted:    1.5M
# Total Submissions: 2.2M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Approach 1: Recursion with Hashmap
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # create a dictionary to quickly look up the index of a value in inorder 
        # inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # def helper(pre_left, pre_right, in_left, in_right):
        #     # Base case: if there are no elements to construct the tree
        #     if pre_left > pre_right or in_left > in_right:
        #         return None
            
        #     # The first element in preorder is the root
        #     root_val = preorder[pre_left]
        #     root = TreeNode(root_val)
            
        #     # find the index of the root in the inorder list
        #     root_index = inorder_map[root_val]
            
        #     # number of elements in the left subtree 
        #     left_subtree_size = root_index - in_left
            
        #     # recursively build the left subtree
        #     root.left = helper(pre_left + 1, pre_left + left_subtree_size, in_left, root_index - 1)
        #     # recursively build the right subtree
        #     root.right = helper(pre_left + left_subtree_size + 1, pre_right, root_index + 1, in_right)
            
        #     return root
        # # call helper for the entire range of preorder and inorder lists
        # return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        
        # Approach 2: Iterative Solution Using Stack
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        if not preorder or not inorder:
            return None
        
        # create the root from the first element in preorder
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0
        
        # iterate over the preorder list starting from the second element 
        for pre_val in preorder[1:]:
            node = stack[-1] 
            # if the top of the stack is not equal to the inorder element, then the new node must be a left child i think
            if node.val != inorder[inorder_index]:
                node.left = TreeNode(pre_val)
                stack.append(node.left)
            else:
                # pop from the stack until the top of the stack is not equal to the inorder element                    
                while stack and stack[-1].val == inorder[inorder_index]:
                    node = stack.pop()
                    inorder_index += 1
                
                # the new node is the right child of the last node popped from the stack
                node.right = TreeNode(pre_val)
                stack.append(node.right)
                
        return root
# @lc code=end

