#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#
# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
#
# algorithms
# Easy (61.97%)
# Likes:    742
# Dislikes: 26
# Total Accepted:    63.7K
# Total Submissions: 102.8K
# Testcase Example:  '[10,20,30,5,10,50]'
#
# Given an array of positive integers nums, return the maximum possible sum of
# an ascending subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.
#
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
# where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is
# ascending.
#
#
# Example 1:
#
#
# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of
# 65.
#
#
# Example 2:
#
#
# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum
# of 150.
#
#
# Example 3:
#
#
# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of
# 33.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#


# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # n = len(nums)  # length of the array
        # max_sum = 0  # maximum sum of the ascending subarray found so far
        # for i in range(
        #     n
        # ):  # iterate through the array to find the maximum sum of the ascending subarray
        #     sum = nums[i]  # sum of the ascending subarray starting at index i
        #     j = i + 1  # pointer to the next element in the array
        #     while (
        #         j < n and nums[j] > nums[j - 1]
        #     ):  # find the next element in the ascending subarray
        #         sum += nums[j]
        #         j += 1
        #     max_sum = max(max_sum, sum)

        # return max_sum

        # Approach 2: One Pass Iteration
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Get the length of the list
        n = len(nums)

        # Initialize max_sum and curr_sum with the first element since a subarray of size 1 is ascending by definition
        max_sum = nums[0]
        curr_sum = nums[0]

        # Loop through the array, starting from the second element
        for i in range(1, n):
            # If the current element is greater than the previous, it continues the ascending subarray
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]  # Add current element to the current subarray sum
            else:
                # Otherwise, start a new subarray starting from the current element
                curr_sum = nums[i]
            # Update max_sum if the current subarray sum is greater than the previous maximum
            max_sum = max(max_sum, curr_sum)

        # Return the maximum ascending subarray sum found
        return max_sum


# @lc code=end
