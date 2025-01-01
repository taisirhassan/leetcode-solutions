#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
#
# algorithms
# Easy (62.19%)
# Likes:    1727
# Dislikes: 68
# Total Accepted:    208.1K
# Total Submissions: 329.6K
# Testcase Example:  '"011101"'
#
# Given a string s of zeros and ones, return the maximum score after splitting
# the string into two non-empty substrings (i.e. left substring and right
# substring).
# 
# The score after splitting a string is the number of zeros in the left
# substring plus the number of ones in the right substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
# 
# 
# Example 2:
# 
# 
# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2
# + 3 = 5
# 
# 
# Example 3:
# 
# 
# Input: s = "1111"
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.
# 
# 
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        # Approach 1: Brute Force Approach
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # max_score = 0 # Initialize the maximum score to be zero
        n = len(s)
        
        # # Iterate through each possible split point 
        # # The split point range froms 1 to n-1 to ensure both substrings are non-empty
        # for split in range(1, n):
        #     left = s[:split] # Left substring
        #     right = s[split:] # Right substring
        
        #     # Count the number of zeroes 
        #     left_zeroes = left.count('0')
        
        #     # Count the number of ones
        #     right_ones = right.count('1')
        
        #     # Calculate the current score
        #     current_score = left_zeroes + right_ones
        
        #     # Update the maximum score
        #     max_score = max(max_score, current_score)
        
        # return max_score
        
        # Approach 2: Optimized Approach with Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # Initialize the prefix sum arrays
        # prefix_zeroes = [0] * n
        # prefix_zeroes[0] = 1 if s[0] == '0' else 0
        
        # for i in range(1, n):
        #     prefix_zeroes[i] = prefix_zeroes[i-1] + (1 if s[i] == '0' else 0)
            
        # # Initialize the suffix sums for ones
        # suffix_ones = [0] * n
        # suffix_ones[-1] = 1 if s[-1] == '1' else 0
        # for i in range(n-2, -1, -1):
        #     suffix_ones[i] = suffix_ones[i+1] + (1 if s[i] == '1' else 0)
            
        # # Initialize the maximum score
        # max_score = 0
        
        # # Iterate through each possible split point
        # for split in range(1, n):
        #     # Zeroes in the left substring
        #     left_zeroes = prefix_zeroes[split-1]
            
        #     # Ones in the right substring starting from the split
        #     right_ones = suffix_ones[split]
            
        #     # Calculate the current score
        #     current_score = left_zeroes + right_ones
            
        #     # Update the maximum score
        #     max_score = max(max_score, current_score)
            
        # return max_score
        
        # Approach 3: Single Pass Approach with Dynamic Counting
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        total_ones = s.count('1') # Count the total number of ones
        max_score  = 0 # Initialize the maximum score to be zero
        zeros_left = 0 # Initialize the number of zeroes in the left substring
        ones_right = total_ones # Initialize the number of ones in the right substring
        
        # Iterate through the string, stopping before the last character
        for i in range(n-1):
            # Update the number of zeroes in the left substring
            if s[i] == '0':
                zeros_left += 1
                # If the current charcater is '1', decrement the number of ones in the right substring as it will be included in the left substring
            else:
                ones_right -= 1
            
            # Update the maximum score
            max_score = max(max_score, zeros_left + ones_right)
            
        return max_score
        
# @lc code=end

