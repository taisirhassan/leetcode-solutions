#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#
# https://leetcode.com/problems/number-of-ways-to-split-array/description/
#
# algorithms
# Medium (48.66%)
# Likes:    596
# Dislikes: 56
# Total Accepted:    49.5K
# Total Submissions: 101.6K
# Testcase Example:  '[10,4,-8,7]'
#
# You are given a 0-indexed integer array nums of length n.
#
# nums contains a valid split at index i if the following are true:
#
#
# The sum of the first i + 1 elements is greater than or equal to the sum of
# the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
#
#
# Return the number of valid splits in nums.
#
#
# Example 1:
#
#
# Input: nums = [10,4,-8,7]
# Output: 2
# Explanation:
# There are three ways of splitting nums into two non-empty parts:
# - Split nums at index 0. Then, the first part is [10], and its sum is 10. The
# second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid
# split.
# - Split nums at index 1. Then, the first part is [10,4], and its sum is 14.
# The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a
# valid split.
# - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6.
# The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid
# split.
# Thus, the number of valid splits in nums is 2.
#
#
# Example 2:
#
#
# Input: nums = [2,3,1,0]
# Output: 2
# Explanation:
# There are two valid splits in nums:
# - Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The
# second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid
# split.
# - Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6.
# The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid
# split.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time: O(n^2)
        # Space: O(1)
        # n = len(nums)
        # valid_splits = 0  # Initialize the count of valid splits

        # # Iterate through each possible split index
        # for i in range(n - 1):
        #     # Initialize the sum of the first i + 1 elements
        #     sum_first = sum(nums[: i + 1])

        #     # Initialize the sum of the last n - i - 1 elements
        #     sum_last = sum(nums[i + 1 :])

        #     # Check if the split is valid
        #     if sum_first >= sum_last:
        #         valid_splits += 1  # Increment if valid

        # return valid_splits  # Return the total count of valid splits

        # Approach 2: Prefix Sum
        # Time: O(n) where n is the length of the input array nums
        # Space: O(n) for the prefix sum array
        # n = len(nums)
        # if (
        #     n < 2
        # ):  # If the length of the input array is less than 2, return 0 as there are no valid splits
        #     return 0

        # # Initialize the prefix sum array
        # prefix_sum = [0] * n
        # prefix_sum[0] = nums[
        #     0
        # ]  # First element of the prefix sum array is the first element of the input array

        # # Calculate the prefix sum array
        # for i in range(1, n):
        #     prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # # Initialize the total sum of the input array
        # total_sum = prefix_sum[-1]

        # valid_splits = 0  # Initialize the count of valid splits

        # # Iterate through each possible split index
        # for i in range(n - 1):
        #     sum_first = prefix_sum[i]  # Sum of the first i + 1 elements
        #     sum_last = total_sum - sum_first  # Sum of the last n - i - 1 elements

        #     if sum_first >= sum_last:
        #         valid_splits += 1  # Increment if valid

        # return valid_splits  # Return the total count of valid splits

        # Approach 3: Prefix Sum Optimized
        # Time: O(n) where n is the length of the input array nums
        # Space: O(1)
        total_sum = sum(nums)  # Calculate the total sum of the input array
        n = len(nums)
        prefix_sum = 0  # Initialize the prefix sum
        valid_splits = 0  # Initialize the count of valid splits

        # Iterate through the array up to the second last element
        for i in range(n - 1):
            prefix_sum += nums[i]  # Update the prefix sum
            remaining_sum = total_sum - prefix_sum  # Calculate the remaining sum

            if prefix_sum >= remaining_sum:
                valid_splits += 1

            return valid_splits  # Return the total count of valid splits


# @lc code=end
