#
# @lc app=leetcode id=2425 lang=python3
#
# [2425] Bitwise XOR of All Pairings
#
# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/
#
# algorithms
# Medium (58.00%)
# Likes:    438
# Dislikes: 15
# Total Accepted:    25K
# Total Submissions: 42.3K
# Testcase Example:  '[2,1,3]\n[10,2,5,0]'
#
# You are given two 0-indexed arrays, nums1 and nums2, consisting of
# non-negative integers. There exists another array, nums3, which contains the
# bitwise XOR of all pairings of integers between nums1 and nums2 (every
# integer in nums1 is paired with every integer in nums2 exactly once).
#
# Return the bitwise XOR of all integers in nums3.
#
#
# Example 1:
#
#
# Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
# Output: 13
# Explanation:
# A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
# The bitwise XOR of all these numbers is 13, so we return 13.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 0
# Explanation:
# All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^
# nums2[1], nums1[1] ^ nums2[0],
# and nums1[1] ^ nums2[1].
# Thus, one possible nums3 array is [2,5,1,6].
# 2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 10^5
# 0 <= nums1[i], nums2[j] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Approach 1: Brute Force
        # Time: O(n * m)
        # Space: O(1)
        # Initialize the XOR accumulator for nums3
        # result = 0

        # # Iterate over each element in nums1
        # for x in nums1:
        #     # Iterate over each element in nums2
        #     for y in nums2:
        #         # Compute the XOR for the current pair and accumulate it
        #         result ^= x ^ y
        # return result

        # Approach 2: Hash Map
        # Time: O(n + m)
        # Space: O(n + m)

        # len1, len2 = len(nums1), len(nums2)

        # # Dictionary to store weighted frequency (total occurrences in the pairing)
        # freq = {}

        # # For each number in nums1, it contributes len2 times.
        # for num in nums1:
        #     freq[num] = freq.get(num, 0) + len2

        # # For each number in nums2, it contributes len1 times.
        # for num in nums2:
        #     freq[num] = freq.get(num, 0) + len1

        # # Initialize answer to 0.
        # ans = 0

        # # For each unique number, add it (via XOR) if its total count is odd.
        # for num, count in freq.items():
        #     if count % 2 == 1:
        #         ans ^= num

        # return ans

        # Approach 3: Bit Manipulation (Optimized)
        # Time: O(n + m)
        # Space: O(1)
        len1, len2 = len(nums1), len(nums2)

        xor1, xor2 = 0, 0

        # If nums2 has an odd number of elements, then each element in nums1 appears odd times.
        if len2 % 2 == 1:
            for num in nums1:
                xor1 ^= num  # Accumulate XOR of nums1
        # Otherwise, xor1 remains 0.

        # If nums1 has an odd number of elements, then each element in nums2 appears odd times.
        if len1 % 2 == 1:
            for num in nums2:
                xor2 ^= num  # Accumulate XOR of nums2
        # Otherwise, xor2 remains 0.

        # The final answer is XOR of the contributions.
        return xor1 ^ xor2


# @lc code=end
