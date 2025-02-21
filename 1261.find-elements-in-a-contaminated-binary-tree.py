#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
#
# algorithms
# Medium (77.72%)
# Likes:    1350
# Dislikes: 121
# Total Accepted:    174.4K
# Total Submissions: 206.4K
# Testcase Example:  '["FindElements","find","find"]\n[[[-1,null,-1]],[1],[2]]'
#
# Given a binary tree with the following rules:
#
#
# root.val == 0
# For any treeNode:
#
# If treeNode.val has a value x and treeNode.left != null, then
# treeNode.left.val == 2 * x + 1
# If treeNode.val has a value x and treeNode.right != null, then
# treeNode.right.val == 2 * x + 2
#
#
#
#
# Now the binary tree is contaminated, which means all treeNode.val have been
# changed to -1.
#
# Implement the FindElements class:
#
#
# FindElements(TreeNode* root) Initializes the object with a contaminated
# binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the
# recovered binary tree.
#
#
#
# Example 1:
#
#
# Input
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# Output
# [null,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1]);
# findElements.find(1); // return False
# findElements.find(2); // return True
#
# Example 2:
#
#
# Input
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# Output
# [null,true,true,false]
# Explanation
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False
#
# Example 3:
#
#
# Input
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# Output
# [null,true,false,false,true]
# Explanation
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True
#
#
#
# Constraints:
#
#
# TreeNode.val == -1
# The height of the binary tree is less than or equal to 20
# The total number of nodes is between [1, 10^4]
# Total calls of find() is between [1, 10^4]
# 0 <= target <= 10^6
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
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # Approach 1: Path Traversal without Precomputation
        # Time: O(log(target))
        # Space: O(1)
        # self.root = root

        # Approach 2: Precomputation
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        self.values = set()

        def dfs(node, val):
            # Preorder traversal to populate the set with values
            if node:
                self.values.add(val)
                dfs(node.left, 2 * val + 1)  # left child
                dfs(node.right, 2 * val + 2)  # right child

        if root:
            dfs(root, 0)

    def find(self, target: int) -> bool:
        # if target == 0:
        #     return self.root is not None

        # # collect directions to target
        # directions = []
        # y = target
        # while target > 0:
        #     if y % 2 == 1:  # odd, left child
        #         directions.append("left")
        #         y = (y - 1) // 2
        #     else:  # even, right child
        #         directions.append("right")
        #         y = (y - 2) // 2

        # current = self.root
        # for direction in reversed(directions):
        #     if not current:
        #         return False
        #     if direction == "left":
        #         current = current.left
        #     else:
        #         current = current.right

        # return current is not None

        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end
