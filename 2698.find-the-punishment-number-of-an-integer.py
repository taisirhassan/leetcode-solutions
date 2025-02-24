#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
#
# algorithms
# Medium (62.87%)
# Likes:    1125
# Dislikes: 222
# Total Accepted:    138.7K
# Total Submissions: 168.3K
# Testcase Example:  '10'
#
# Given a positive integer n, return the punishment number of n.
# 
# The punishment number of n is defined as the sum of the squares of all
# integers i such that:
# 
# 
# 1 <= i <= n
# The decimal representation of i * i can be partitioned into contiguous
# substrings such that the sum of the integer values of these substrings equals
# i.
# 
# 
# 
# Example 1:
# 
# 
# Input: n = 10
# Output: 182
# Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy
# the conditions in the statement:
# - 1 since 1 * 1 = 1
# - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal
# to 8 + 1 == 9.
# - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum
# equal to 10 + 0 == 10.
# Hence, the punishment number of 10 is 1 + 81 + 100 = 182
# 
# 
# Example 2:
# 
# 
# Input: n = 37
# Output: 1478
# Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy
# the conditions in the statement:
# - 1 since 1 * 1 = 1. 
# - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
# - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
# - 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
# Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Approach 1: Brute Force Backtracking
        # Time Complexity: O(n^2 * 2^L) where L is the length of the string representation of i^2
        # Space Complexity: O(n) for the recursion stack
        # def can_partition_dfs(s: str, target: int) -> bool:
        #     def dfs(index: int, current_sum: int) -> bool:
        #         # if we have reached the end of the string, check if the sum is equal to the target 
        #         if index == len(s):
        #             return current_sum == target
        #         # try every possible partition starting from the current index
        #         for j in range(index + 1, len(s) + 1):
        #             # convert the curr substring to an integer
        #             part = int(s[index:j])
        #             # recurse with the next index and the updated sum
        #             if dfs(j, current_sum + part):
        #                 return True
        #         return False
        #     return dfs(0, 0)
        
        # total = 0
        # # check each integer i from 1 to n
        # for i in range(1, n + 1):
        #     # convert i to a string
        #     square_str = str(i * i)
        #     # if the dfs partition method confirms a valid partition, add i^2 to total 
        #     if can_partition_dfs(square_str, i):
        #         total += i * i
        # return total
        
        # Approach 2: Dynamic Programming with Memoization
        # Time Complexity: O(n^2 * L) where L is the length of the string representation of i^2
        # Space Complexity: O(n^2) for the memoization table
        # def can_partition(s: str, target: int, pos: int, memo: dict) -> bool:
        #     # base case: reached end of string 
        #     if pos == len(s):
        #         return target == 0
        #     # check memoization table
        #     key = (pos, target)
        #     if key in memo:
        #         return memo[key]
            
        #     current = 0 
        #     # try all prefixes starting at pos
        #     for i in range(pos, len(s)):
        #         current = current * 10 + int(s[i]) # build number digit by digit 
        #         if current > target: # early exit if current exceeds target
        #             break
        #         # recurse for the rest
        #         # if we can partition the rest of the string to get the target, return True
        #         if can_partition(s, target - current, i + 1, memo):
        #             memo[key] = True
        #             return True
        #         # if we can't partition the rest of the string to get the target, continue
        #     memo[key] = False
        #     return False 
        
        # result = 0
        # for i in range(1, n + 1):
        #     square_str = str(i * i)
        #     if can_partition(square_str, i, 0, {}):
        #         result += i * i
        # return result
        
       
    # @lc code=end

