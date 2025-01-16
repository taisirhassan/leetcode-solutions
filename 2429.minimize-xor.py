#
# @lc app=leetcode id=2429 lang=python3
#
# [2429] Minimize XOR
#
# https://leetcode.com/problems/minimize-xor/description/
#
# algorithms
# Medium (44.55%)
# Likes:    1021
# Dislikes: 71
# Total Accepted:    123.7K
# Total Submissions: 198.4K
# Testcase Example:  '3\n5'
#
# Given two positive integers num1 and num2, find the positive integer x such
# that:
#
#
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
#
#
# Note that XOR is the bitwise XOR operation.
#
# Return the integer x. The test cases are generated such that x is uniquely
# determined.
#
# The number of set bits of an integer is the number of 1's in its binary
# representation.
#
#
# Example 1:
#
#
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3
# = 0 is minimal.
#
#
# Example 2:
#
#
# Input: num1 = 1, num2 = 12
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0001 and 1100, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 1
# = 2 is minimal.
#
#
#
# Constraints:
#
#
# 1 <= num1, num2 <= 10^9
#
#
#


# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        # Count the required number of 1's for x (from num2)
        req = bin(num2).count("1")

        # Count the number of 1's in num1
        num1_ones = bin(num1).count("1")

        x = 0  # This will be our answer.

        # Determine the bit length we need to consider.
        # As per constraints, numbers can be up to 10^9 which fits within 32 bits.
        BIT_LENGTH = 32

        if num1_ones >= req:
            # We have more ones in num1 than required, so we can "drop" some 1's.
            # We want to pick req bits among those ones in num1.
            # Iterate from the most significant bit to the least significant bit.
            for i in range(BIT_LENGTH - 1, -1, -1):
                # Check if the i-th bit of num1 is set.
                if (num1 >> i) & 1:
                    if req > 0:
                        # Set the same bit in x
                        x |= 1 << i
                        req -= 1
                # Else, we skip it.
        # At this point, x has exactly the required number of ones,
        # specifically chosen from positions where num1 has ones.

        else:
            # If num1 has fewer ones than needed, start with x having num1's bits.
            x = num1
            extra = req - num1_ones  # Number of additional ones we need to add.

            # To minimize the XOR (and the numeric value), set extra ones in low positions.
            for i in range(BIT_LENGTH):
                # Only set the bit if x does not already have it.
                if ((x >> i) & 1) == 0:
                    x |= 1 << i
                    extra -= 1
                    if extra == 0:
                        break

        return x


# @lc code=end
