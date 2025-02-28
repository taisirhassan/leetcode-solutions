#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (79.13%)
# Likes:    11404
# Dislikes: 567
# Total Accepted:    1.3M
# Total Submissions: 1.6M
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
#
# Example 2:
#
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^5
#
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
#
#
#


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Approach 1: Brute Force with built in function
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        # Initialize the result list
        # result = []
        # # Iterate over each number from 0 to n
        # for i in range(n + 1):
        #     # Convert the number to binary and count '1's
        #     count = bin(i).count("1")
        #     result.append(count)
        # return result

        # Approach 2: Dynamic Programming using Right Shift
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # create a list with n + 1 elements, initialized to 0 for each element
        # dp = [0] * (n + 1)

        # # iterate over each number from 1 to n
        # for i in range(1, n + 1):
        #     # count the number of '1's in the binary representation of i
        #     # by counting the number of '1's in i // 2 and adding 1 if i is odd
        #     dp[i] = dp[i >> 1] + (i & 1)

        # return dp

        # Approach 3: Dynamic Programming using Bit Manipulation
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # initialize the dp list with 0 for dp(0)
        dp = [0] * (n + 1)
        # iterate over each number from 1 to n
        for i in range(1, n + 1):
            # dp[i & (i - 1)] is the number of '1's in the binary representation of i with the least significant bit removed
            dp[i] = dp[i & (i - 1)] + 1
        return dp  # return the result list


# @lc code=end
