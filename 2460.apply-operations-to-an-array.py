#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#
# https://leetcode.com/problems/apply-operations-to-an-array/description/
#
# algorithms
# Easy (68.33%)
# Likes:    713
# Dislikes: 41
# Total Accepted:    111.8K
# Total Submissions: 156.6K
# Testcase Example:  '[1,2,2,1,1,0]'
#
# You are given a 0-indexed array nums of size n consisting of non-negative
# integers.
#
# You need to apply n - 1 operations to this array where, in the i^th operation
# (0-indexed), you will apply the following on the i^th element of nums:
#
#
# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to
# 0. Otherwise, you skip this operation.
#
#
# After performing all the operations, shift all the 0's to the end of the
# array.
#
#
# For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end,
# is [1,2,1,0,0,0].
#
#
# Return the resulting array.
#
# Note that the operations are applied sequentially, not all at once.
#
#
# Example 1:
#
#
# Input: nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]
# Explanation: We do the following operations:
# - i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
# - i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change
# nums[2] to 0. The array becomes [1,4,0,1,1,0].
# - i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
# - i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change
# nums[4] to 0. The array becomes [1,4,0,2,0,0].
# - i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change
# nums[5] to 0. The array becomes [1,4,0,2,0,0].
# After that, we shift the 0's to the end, which gives the array
# [1,4,2,0,0,0].
#
#
# Example 2:
#
#
# Input: nums = [0,1]
# Output: [1,0]
# Explanation: No operation can be applied, we just shift the 0 to the end.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 2000
# 0 <= nums[i] <= 1000
#
#
#


# @lc code=start
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Approach 1: Simulation Followed by Shifting
        # Time: O(n)
        # Space: O(n)

        # n = len(nums)
        # for i in range(n - 1):
        #     # if the current element is equal to the next element
        #     if nums[i] == nums[i + 1]:
        #         # multiply the current element by 2
        #         nums[i] *= 2
        #         # set the next element to 0
        #         nums[i + 1] = 0
        # # after all the operations, shift all the 0's to the end
        # # create a new array to store the result
        # non_zero = [num for num in nums if num != 0]
        # # count the number of zeros
        # zeros_count = n - len(non_zero)
        # # append the zeros at the end
        # non_zero.extend([0] * zeros_count)
        # return non_zero

        # Approach 2: Simulation Followed by Shifting (Optimized) Two Pointers
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        # first pass: perform the operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        # second pass: shift the zeros to the end, use two pointers to shift non-zero elements to the beginning
        j = 0  # pointer to place the next non-zero element
        for i in range(n):
            if nums[i] != 0:
                # place the non-zero element at index j
                nums[j] = nums[i]
                j += 1

        # fill the rest of the array with zeros
        while j < n:
            nums[j] = 0
            j += 1
        return nums


# @lc code=end
