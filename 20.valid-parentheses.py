#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (41.49%)
# Likes:    25038
# Dislikes: 1843
# Total Accepted:    5.5M
# Total Submissions: 13.3M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
#
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
#
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
#
# Output: false
#
#
# Example 4:
#
#
# Input: s = "([])"
#
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # # Approach 1: Brute force
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        # while "()" in s or "{}" in s or "[]" in s:
        #     # Remove all occurrences of the valid pairs from the string
        #     s = s.replace("()", "")
        #     s = s.replace("{}", "")
        #     s = s.replace("[]", "")
        # # If the string is empty, then all brackets were valid and properly nested.
        # return s == ""

        # Approach 2: Utilizing a Stack
        # Initialize an empty stack to store opening brackets
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        # Mapping from closing brackets to the corresponding opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # Iterate over each character in the input string
        for c in s:
            # If the character is a closing bracket...
            if c in closeToOpen:
                # Check if the stack is not empty and the top matches the expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Remove the matching opening bracket from the stack

                else:
                    # If there's a mismatch or the stack is empty, the input is invalid.
                    return False
            else:
                # If it's an opening bracket, push it onto the stack.
                stack.append(c)

        # At the end, if the stack is empty, all brackets were properly closed.
        return not stack


# @lc code=end
