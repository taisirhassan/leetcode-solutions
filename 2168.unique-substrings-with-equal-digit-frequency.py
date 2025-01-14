#
# @lc app=leetcode id=2168 lang=python3
#
# [2168] Unique Substrings With Equal Digit Frequency
#
# https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/description/
#
# algorithms
# Medium (61.25%)
# Likes:    95
# Dislikes: 12
# Total Accepted:    8K
# Total Submissions: 12.4K
# Testcase Example:  '"1212"'
#
# Given a digit string s, return the number of unique substrings of s where
# every digit appears the same number of times.
# 
# Example 1:
# 
# 
# Input: s = "1212"
# Output: 5
# Explanation: The substrings that meet the requirements are "1", "2", "12",
# "21", "1212".
# Note that although the substring "12" appears twice, it is only counted
# once.
# 
# 
# Example 2:
# 
# 
# Input: s = "12321"
# Output: 9
# Explanation: The substrings that meet the requirements are "1", "2", "3",
# "12", "23", "32", "21", "123", "321".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of digits.
# 
# 
#

# @lc code=start
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        
# @lc code=end

