#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
#
# algorithms
# Easy (46.04%)
# Likes:    1149
# Dislikes: 61
# Total Accepted:    126.2K
# Total Submissions: 272.9K
# Testcase Example:  '"bank"\n"kanb"'
#
# You are given two strings s1 and s2 of equal length. A string swap is an
# operation where you choose two indices in a string (not necessarily
# different) and swap the characters at these indices.
# 
# Return true if it is possible to make both strings equal by performing at
# most one string swap on exactly one of the strings. Otherwise, return
# false.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of
# s2 to make "bank".
# 
# 
# Example 2:
# 
# 
# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# 
# 
# Example 3:
# 
# 
# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation
# is required.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
    # If both strings are already equal, no swap is needed.
        if s1 == s2:
            return True
        
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        
        # n = len(s1)
        
        #     # Try every possible pair of indices in s1.
        # for i in range(n):
        #     for j in range(i, n):  # j starts from i to avoid duplicate swaps and allow swapping with itself.
        #         # Convert the string to a list to perform the swap.
        #         s1_list = list(s1)
        #         # Swap the characters at index i and j.
        #         s1_list[i], s1_list[j] = s1_list[j], s1_list[i]
        #         # Convert the list back to a string.
        #         swapped = ''.join(s1_list)
        #         # Check if after the swap the string equals s2.
        #         if swapped == s2:
        #             return True

        # # If no swap can make s1 equal to s2, return False.
        # return False
        
        # Approach 2: Count the differences
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # # List to store the indices where s1 and s2 differ.
        # diff = []
        
        # # Iterate through the strings comparing characters.
        # for i in range(len(s1)):
        #     if s1[i] != s2[i]:
        #         diff.append(i)
        
        # # For one swap to fix the differences, there must be exactly 2 positions that differ.
        # if len(diff) != 2:
        #     return False

        # # Check if swapping the two differing characters in one string would make the strings equal.
        # # This works if the character in s1 at the first differing index equals the character in s2 at the second,
        # # and the character in s1 at the second differing index equals the character in s2 at the first.
        # return s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]
        
# @lc code=end

