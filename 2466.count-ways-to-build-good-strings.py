#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#
# https://leetcode.com/problems/count-ways-to-build-good-strings/description/
#
# algorithms
# Medium (54.25%)
# Likes:    2106
# Dislikes: 201
# Total Accepted:    156.8K
# Total Submissions: 263.4K
# Testcase Example:  '3\n3\n1\n1'
#
# Given the integers zero, one, low, and high, we can construct a string by
# starting with an empty string, and then at each step perform either of the
# following:
#
#
# Append the character '0' zero times.
# Append the character '1' one times.
#
#
# This can be performed any number of times.
#
# A good string is a string constructed by the above process having a length
# between low and high (inclusive).
#
# Return the number of different good strings that can be constructed
# satisfying these properties. Since the answer can be large, return it modulo
# 10^9 + 7.
#
#
# Example 1:
#
#
# Input: low = 3, high = 3, zero = 1, one = 1
# Output: 8
# Explanation:
# One possible valid good string is "011".
# It can be constructed as follows: "" -> "0" -> "01" -> "011".
# All binary strings from "000" to "111" are good strings in this example.
#
#
# Example 2:
#
#
# Input: low = 2, high = 3, zero = 1, one = 2
# Output: 5
# Explanation: The good strings are "00", "11", "000", "110", and "011".
#
#
#
# Constraints:
#
#
# 1 <= low <= high <= 10^5
# 1 <= zero, one <= low
#
#
#


# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        # # Approach 1: Brute Force Recursion
        # # Time complexity: O(2^high) where high is the maximum length of the string
        # # Space complexity: O(high) as the maximum depth of the recursion stack would be high
        # def dfs(length):
        #     # Base Case: If the length exceeds high, return 0
        #     if length > high:
        #         return 0

        #     # Initialize count: 1 if current length is within [low, high], else 0
        #     count = 1 if low <= length <= high else 0

        #     # Recursive Case: Append 0 or 1 and call the function recursively
        #     # Recursively append '0's and '1's
        #     # Append '0's block
        #     count += dfs(length + zero)
        #     # Append '1's block
        #     count += dfs(length + one)

        #     return count

        # total_count = dfs(0)  # Start the recursion with length 0
        # return total_count % MOD  # Return the total count modulo 10^9 + 7

        # Approach 2: Recursion with Memoization (Top Down DP)
        # Time complexity: O(high) where high is the maximum length of the string
        # Space complexity: O(high) as we are using a memoization dictionary of size high

        # memo = {}  # Initialize a memoization dictionary (length: count)

        # def dfs(length):
        #     # Base Case: If the length exceeds high, return 0
        #     if length > high:
        #         return 0

        #     # If the result for the current length is already computed, return it from the memo
        #     if length in memo:
        #         return memo[length]

        #     memo[length] = 1 if low <= length <= high else 0

        #     # Recursive Case: Append 0 or 1 and call the function recursively
        #     # Recursively append '0's and '1's
        #     # Append '0's block
        #     memo[length] += dfs(length + zero) + dfs(length + one)
        #     return memo[length] % MOD

        # # Start the recursion with length 0
        # return dfs(0)

        # Approach 3: Bottom Up DP
        dp = [0] * (high + 1)  # Initialize the dp array of size high+1
        dp[0] = 1

        # Iterate over the length of the string
        for i in range(1, high + 1):
            # If appending '0's block is possible
            if i >= zero:
                dp[i] += dp[i - zero]
                dp[i] %= MOD
            # If appending '1's block is possible
            if i >= one:
                dp[i] += dp[i - one]
                dp[i] %= MOD

        # Sum all valid ways to construct the string of length i
        total = sum(dp[low : high + 1]) % MOD
        return total


# @lc code=end
