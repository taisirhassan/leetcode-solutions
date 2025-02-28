#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (36.09%)
# Likes:    10456
# Dislikes: 10009
# Total Accepted:    2.1M
# Total Submissions: 5.7M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
#
# Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
# Constraints:
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n is an integer.
# Either x is not zero or n > 0.
# -10^4 <= x^n <= 10^4
#
#
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Approach 1: Brute Force
        # Time complexity: O(n)
        # Space complexity: O(1)
        # handle negative exponent case by inverting x and making n positive
        # if n < 0:
        #     x = 1 / x
        #     n = -n

        # result = 1.0
        # # multiply x, n times
        # for _ in range(n):
        #     result *= x
        # return result

        # Approach 2: Recursive Exponentiation by squaring
        # Time complexity: O(logn)
        # Space complexity: O(logn)
        # def rec_pow(x: float, n: int) -> float:
        #     # Base case: any number to the power 0 is 1.
        #     if n == 0:
        #         return 1.0
        #     # Recursively compute half power.
        #     half = rec_pow(x, n // 2)
        #     # For even exponent, square the half.
        #     if n % 2 == 0:
        #         return half * half
        #     else:
        #         # For odd exponent, multiply an extra x.
        #         return half * half * x

        # # Handle negative exponent by inverting x.
        # if n < 0:
        #     return 1 / rec_pow(x, -n)
        # return rec_pow(x, n)

        # Approach 3: Iterative Exponentiation by squaring
        # Time complexity: O(logn)
        # Space complexity: O(1)
        # If n is negative, convert x^n to 1/(x^|n|)
        exponent = n
        if n < 0:
            x = 1 / x  # Invert x for negative exponent.
            exponent = -n  # Use the absolute value of n.

        result = 1.0  # Initialize result as 1, since any number raised to 0 is 1.

        # Loop until the exponent becomes 0.
        while exponent:
            # If the current exponent is odd, multiply the result by x.
            if exponent % 2 == 1:
                result *= x
            # Square the base for the next bit.
            x *= x
            # Use integer division to halve the exponent.
            exponent //= 2

        return result


# @lc code=end
