#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (51.48%)
# Likes:    35166
# Dislikes: 1492
# Total Accepted:    4.7M
# Total Submissions: 9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n^3)
        # Space Complexity: O(1)
        # n = len(nums)

        # max_sum = float("-inf")
        # # iterate through all possible subarrays
        # for i in range(n):
        #     # iterate through all possible subarrays starting from i
        #     for j in range(i, n):
        #         # calculate the sum of the current subarray nums[i:j+1]
        #         current_sum = 0
        #         # iterate through the subarray nums[i:j+1]
        #         for k in range(i, j + 1):
        #             # add the current element to the sum
        #             current_sum += nums[k]
        #             # update the maximum sum
        #         max_sum = max(max_sum, current_sum)

        # return max_sum
        
        # Approach 2: Bruteforce Optimized
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        
        


# @lc code=end
