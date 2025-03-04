#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/
#
# algorithms
# Medium (68.27%)
# Likes:    1417
# Dislikes: 56
# Total Accepted:    146.4K
# Total Submissions: 187.8K
# Testcase Example:  '12'
#
# Given an integer n, return true if it is possible to represent n as the sum
# of distinct powers of three. Otherwise, return false.
#
# An integer y is a power of three if there exists an integer x such that y ==
# 3^x.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: true
# Explanation: 12 = 3^1 + 3^2
#
#
# Example 2:
#
#
# Input: n = 91
# Output: true
# Explanation: 91 = 3^0 + 3^2 + 3^4
#
#
# Example 3:
#
#
# Input: n = 21
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^7
#
#
#


# @lc code=start
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Approach 1: Brute Force Backtracking
        # Time Complexity: O(2^log_3(n))
        # Space Complexity: O(log_3(n))
        # precompute all powers of 3 less than or equal to n
        # powers = []
        # power = 1
        # while power <= n:
        #     powers.append(power)
        #     power *= 3

        # # define the backtracking function
        # def backtrack(index: int, current_sum: int) -> bool:
        #     # base case: if we have reached the target sum
        #     if current_sum == n:
        #         return True
        #     # if we have exceeded the target sum or we have exhausted all powers
        #     if current_sum > n or index == len(powers):
        #         return False
        #     # Decision: include the current power. If it leads to a solution, return True
        #     if backtrack(index + 1, current_sum + powers[index]):
        #         return True
        #     # Decision: Exclude the current power. If it leads to a solution, return True
        #     if backtrack(index + 1, current_sum):
        #         return True

        #     return False

        # return backtrack(0, 0)

        # Approach 2: Greedy Approach
        # Time Complexity: O(log_3(n))
        # Space Complexity: O(1)

        # iterate until n becomes 0.
        while n:
            remainder = n % 3
            # if any remainder equals 2, then n cannot be represented as the sum of distinct powers of 3
            if remainder == 2:
                return False
            # divide n by 3 to continue with the next digit in base-3
            n //= 3

        return True


# @lc code=end
