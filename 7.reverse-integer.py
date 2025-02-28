#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (29.55%)
# Likes:    13849
# Dislikes: 13730
# Total Accepted:    3.9M
# Total Submissions: 12.9M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#
#
# Example 1:
#
#
# Input: x = 123
# Output: 321
#
#
# Example 2:
#
#
# Input: x = -123
# Output: -321
#
#
# Example 3:
#
#
# Input: x = 120
# Output: 21
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # Approach 1: Mathematical Reversal
        # Time complexity: O(1)
        # Space complexity: O(1)
        # Limits for a 32-bit signed integer
        # INT_MAX = 2**31 - 1
        # INT_MIN = -(2**31)

        # # determine the sign of the input
        # sign = 1 if x >= 0 else -1
        # x = abs(x)

        # result = 0  # this variable will store the reversed number

        # # process each digit until x becomes 0
        # while x:
        #     # get the last digit of x
        #     digit = x % 10
        #     # remove the last digit from x
        #     x //= 10
        #     # check for overflow before appending
        #     if result > (INT_MAX - digit) // 10:
        #         return 0
        #     # append the digit to the result
        #     result = result * 10 + digit

        # return sign * result  # reapply the original sign and return

        # Approach 2: String Conversion
        # Time complexity: O(1)
        # Space complexity: O(1)
        # Limits for a 32-bit signed integer.
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -(2**31)  # -2147483648

        # Determine the sign of x.
        sign = 1 if x >= 0 else -1

        # Reverse the string representation of the absolute value of x.
        reversed_str = str(abs(x))[::-1]

        # Convert the reversed string back to an integer.
        result = sign * int(reversed_str)

        # Return 0 if the reversed integer exceeds the 32-bit signed integer range.
        return result if INT_MIN <= result <= INT_MAX else 0


# @lc code=end
