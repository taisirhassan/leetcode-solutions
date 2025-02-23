#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (71.92%)
# Likes:    2824
# Dislikes: 121
# Total Accepted:    117.2K
# Total Submissions: 161.4K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Given two integer arrays, preorder and postorder where preorder is the
# preorder traversal of a binary tree of distinct values and postorder is the
# postorder traversal of the same tree, reconstruct and return the binary
# tree.
# 
# If there exist multiple answers, you can return any of them.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [1], postorder = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and
# postorder traversal of the same binary tree.
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Approach 1: Recursion & Slicing
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        
        # # Base case: if the list is empty, return None
        # if not preorder or not postorder:
        #     return None
        
        # # the first element in preorder is the root of the tree
        # root = TreeNode(preorder[0])
        
        # # if there is only one node, return it.
        # if len(preorder) == 1:
        #     return root
        
        # # the second element in preorder is the root of the left subtree 
        # # find the index in postorder to determine the size of the left subtree
        # left_root_val = preorder[1]
        # left_subtree_size = postorder.index(left_root_val) + 1   
        
        # # recursively build the left & right subtrees 
        # # left sutree: from next element in preorder, and first left_subtree_size elements in postorder  
        # root.left = self.constructFromPrePost(preorder[1:1+left_subtree_size], postorder[:left_subtree_size])
        # # right subtree: from next element after left subtree in preorder, and the rest in postorder
        # root.right = self.constructFromPrePost(preorder[1+left_subtree_size:], postorder[left_subtree_size:-1])
        
        # return root
        
        # Approach 2: Recursion & Hash Map
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # map each value in postorder to is index
        # post_index = {val: i for i, val in enumerate(postorder)}
        
        # def helper(pre_start, pre_end, post_start, post_end):
        #     # base case: if there are no elements to construct the tree
        #     if pre_start > pre_end or post_start > post_end:
        #         return None
            
        #     # create root node
            
        #     root = TreeNode(preorder[pre_start])
            
        #     # if only one element is present, return the node 
        #     if pre_start == pre_end:
        #         return root
            
            
        #     # the next element in preorder is the root of the left subtree
        #     left_root_val = preorder[pre_start + 1]
        #     # find the index of the left root in postorder
        #     left_root_index = post_index[left_root_val]
        #     # determine the size of the left subtree
        #     left_subtree_size = left_root_index - post_start + 1
            
        #     # recursively build the left and right subtrees
        #     root.left = helper(pre_start + 1, pre_start + left_subtree_size, post_start, left_root_index)
        #     root.right = helper(pre_start + left_subtree_size + 1, pre_end, left_root_index + 1, post_end - 1)
            
        #     return root
        
        # # start recursion over the full range of the tree
        # return helper(0, len(preorder) - 1, 0, len(postorder) - 1)
        
        # Approach 3: Iterative Solution with Stack
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # edge case: if the list is empty, return None
        if not preorder or not postorder:
            return None
        
        # initialize the root from the first element in preorder
        root = TreeNode(preorder[0])
        stack = [root] 
        # this pointer tracks our current position in the preorder list 
        post_index = 0
        
        # iterate over preorder starting from second element 
        for pre_val in preorder[1:]:
            node = TreeNode(pre_val) 
            # while the stack's top node equals the current postorder value, means we have reached the end of the left subtree
            while stack and stack[-1].val == postorder[post_index]:
                stack.pop()
                post_index += 1
            
            # if the left child is empty, assign new node as left child, otherwise right child     
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            # add the new node to the stack
            stack.append(node)

        return root  # return the constructed tree root
# @lc code=end

