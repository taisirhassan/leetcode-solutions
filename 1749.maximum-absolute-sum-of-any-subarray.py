#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
#
# algorithms
# Medium (60.56%)
# Likes:    1421
# Dislikes: 25
# Total Accepted:    67.5K
# Total Submissions: 103.4K
# Testcase Example:  '[1,-3,2,3,-4]'
#
# You are given an integer array nums. The absolute sum of a subarray [numsl,
# numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 +
# numsr).
#
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
#
# Note that abs(x) is defined as follows:
#
#
# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
#
#
#
# Example 1:
#
#
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
#
#
# Example 2:
#
#
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8)
# = 8.
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


# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        # n = len(nums)
        # # precompute the prefix sum
        # prefix = [0] * (n + 1)
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # max_abs_sum = 0

        # # check all the subarrays
        # for i in range(n):
        #     for j in range(i, n):
        #         # Sum of subarray nums[i...j] can be computed in O(1)
        #         sub_sum = prefix[j + 1] - prefix[i]
        #         max_abs_sum = max(max_abs_sum, abs(sub_sum))

        # return max_abs_sum

        # Approach 2: Prefix Sum and Difference of Min and Max Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # initialize the prefix sum and track the minimum and maximum seen
        # prefix_sum = 0
        # min_prefix = 0
        # max_prefix = 0

        # for num in nums:
        #     prefix_sum += num
        #     min_prefix = min(min_prefix, prefix_sum)
        #     max_prefix = max(max_prefix, prefix_sum)

        # # the maximum absolute subarray sum is the difference between the max and min prefix sums.
        # return max_prefix - min_prefix

        # Approach 3: Kadane's Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Initialize running maximum and minimum subarray sums.
        max_ending_here = 0
        min_ending_here = 0
        # These will store the best seen sums so far.
        max_so_far = 0
        min_so_far = 0

        # Iterate through each number in the array.
        for num in nums:
            # Update the maximum subarray ending here: either start fresh with num,
            # or extend the previous subarray.
            max_ending_here = max(num, max_ending_here + num)
            # Update the minimum subarray ending here in a similar fashion.
            min_ending_here = min(num, min_ending_here + num)

            # Update the overall maximum and minimum.
            max_so_far = max(max_so_far, max_ending_here)
            min_so_far = min(min_so_far, min_ending_here)

        # The answer is the maximum between the best positive sum and the absolute of the best negative sum.
        return max(max_so_far, abs(min_so_far))


# @lc code=end
