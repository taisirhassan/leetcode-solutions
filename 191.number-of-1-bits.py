#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (73.18%)
# Likes:    6742
# Dislikes: 1346
# Total Accepted:    1.7M
# Total Submissions: 2.3M
# Testcase Example:  '11'
#
# Given a positive integer n, write a function that returns the number of set
# bits in its binary representation (also known as the Hamming weight).
#
#
# Example 1:
#
#
# Input: n = 11
#
# Output: 3
#
# Explanation:
#
# The input binary string 1011 has a total of three set bits.
#
#
# Example 2:
#
#
# Input: n = 128
#
# Output: 1
#
# Explanation:
#
# The input binary string 10000000 has a total of one set bit.
#
#
# Example 3:
#
#
# Input: n = 2147483645
#
# Output: 30
#
# Explanation:
#
# The input binary string 1111111111111111111111111111101 has a total of thirty
# set bits.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#
# Follow up: If this function is called many times, how would you optimize it?
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 1: Bit Shifting and Masking
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        # # initialize a counter for the set bits
        # count = 0

        # while n:
        #     # increment the counter if the last bit is set
        #     count += n & 1
        #     # shift the bits to the right to check the next bit in the next iteration
        #     n >>= 1

        # return count

        # Approach 2: Pythonic Way
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        # convert n to binary and count the number of 1s
        # return bin(n).count("1")

        # Approach 3: Brian Kernighan's Algorithm
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        # initialize a counter for the set bits
        count = 0

        # loop until n becomes 0
        while n:
            # this operation removes the last set bit from n
            n &= n - 1
            count += 1

        return count


# @lc code=end
