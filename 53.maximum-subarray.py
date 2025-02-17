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
        # n = len(nums)
        # max_sum = float("-inf")
        # # Outer loop: choose starting index of subarray
        # for i in range(n):
        #     current_sum = 0  # Initialize sum for this starting index
        #     # Inner loop: extend the subarray ending index one element at a time
        #     for j in range(i, n):
        #         current_sum += nums[j]  # Add current element to the subarray sum
        #         max_sum = max(max_sum, current_sum)  # Update max_sum if needed
        # return max_sum

        # Approach 3: Greedy Kadane's Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Initialize current_sum and max_sum with the first element of the array.
        # current_sum = max_sum = nums[0]

        # # Iterate from the second element to the end of the array.
        # for i in range(1, len(nums)):
        #     # Either add the current element to the current_sum or start new subarray from current element.
        #     current_sum = max(nums[i], current_sum + nums[i])
        #     # Update max_sum if current_sum is greater.
        #     max_sum = max(max_sum, current_sum)

        # return max_sum

        # Approach 4: Divide and Conquer
        # Time Complexity: O(nlogn)
        # Space Complexity: O(logn)
        # Helper function for divide and conquer.
        def helper(left: int, right: int) -> int:
            # Base case: only one element.
            if left == right:
                return nums[left]

            # Find the middle index.
            mid = (left + right) // 2

            # Recursively solve for the left and right halves.
            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)

            # Now, compute the maximum subarray sum that crosses the midpoint.
            # Start with the left half.
            cross_left_sum = float("-inf")
            temp_sum = 0
            for i in range(mid, left - 1, -1):
                temp_sum += nums[i]
                cross_left_sum = max(cross_left_sum, temp_sum)

            # Now, compute the right half.
            cross_right_sum = float("-inf")
            temp_sum = 0
            for i in range(mid + 1, right + 1):
                temp_sum += nums[i]
                cross_right_sum = max(cross_right_sum, temp_sum)

            # The maximum sum for the cross segment.
            cross_sum = cross_left_sum + cross_right_sum

            # Return the maximum among the three possible cases.
            return max(left_sum, right_sum, cross_sum)

        # Call the helper function on the entire array.
        return helper(0, len(nums) - 1)


# @lc code=end
