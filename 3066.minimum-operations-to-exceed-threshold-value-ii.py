#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/
#
# algorithms
# Medium (28.80%)
# Likes:    120
# Dislikes: 12
# Total Accepted:    39K
# Total Submissions: 121.1K
# Testcase Example:  '[2,11,10,1,3]\n10'
#
# You are given a 0-indexed integer array nums, and an integer k.
#
# In one operation, you will:
#
#
# Take the two smallest integers x and y in nums.
# Remove x and y from nums.
# Add min(x, y) * 2 + max(x, y) anywhere in the array.
#
#
# Note that you can only apply the described operation if nums contains at
# least two elements.
#
# Return the minimum number of operations needed so that all elements of the
# array are greater than or equal to k.
#
#
# Example 1:
#
#
# Input: nums = [2,11,10,1,3], k = 10
# Output: 2
# Explanation: In the first operation, we remove elements 1 and 2, then add 1 *
# 2 + 2 to nums. nums becomes equal to [4, 11, 10, 3].
# In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to
# nums. nums becomes equal to [10, 11, 10].
# At this stage, all the elements of nums are greater than or equal to 10 so we
# can stop.
# It can be shown that 2 is the minimum number of operations needed so that all
# elements of the array are greater than or equal to 10.
#
#
# Example 2:
#
#
# Input: nums = [1,1,2,4,9], k = 20
# Output: 4
# Explanation: After one operation, nums becomes equal to [2, 4, 9, 3].
# After two operations, nums becomes equal to [7, 4, 9].
# After three operations, nums becomes equal to [15, 9].
# After four operations, nums becomes equal to [33].
# At this stage, all the elements of nums are greater than 20 so we can stop.
# It can be shown that 4 is the minimum number of operations needed so that all
# elements of the array are greater than or equal to 20.
#
#
# Constraints:
#
#
# 2 <= nums.length <= 2 * 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= 10^9
# The input is generated such that an answer always exists. That is, there
# exists some sequence of operations after which all elements of the array are
# greater than or equal to k.
#
#
#


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Approach 1: Brute Force
        # Time: O(n^2)
        # Space: O(n)
        # operations = 0
        # # Continue until every element in nums is at least k.
        # while min(nums) < k:
        #     # If there are fewer than two elements, the operation can't be performed.
        #     if len(nums) < 2:
        #         return -1  # Based on problem constraints, this should not happen.

        #     # Sort a copy of nums to get the two smallest elements.
        #     sorted_nums = sorted(nums)
        #     x = sorted_nums[0]  # smallest
        #     y = sorted_nums[1]  # second smallest

        #     # Compute the new value as described.
        #     new_val = 2 * x + y

        #     # Remove one occurrence of x and one occurrence of y from nums.
        #     nums.remove(x)
        #     nums.remove(y)

        #     # Append the new value to nums.
        #     nums.append(new_val)

        #     # Increment the operation count.
        #     operations += 1

        # return operations

        # Approach 2: Priority Queue
        # Time: O(nlogn)
        # Space: O(n)
        # Transform the list into a min-heap.
        heapq.heapify(nums)
        operations = 0

        # Continue until every element in nums is at least k.
        while nums[0] < k:
            # If we have fewer than two elements, we cannot perform the operation.
            if len(nums) < 2:
                return -1  # Shouldn't happen as per problem guarantee.

            # Get the two smallest elements.
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Calculate the new element: since x is the smallest, new_val = 2*x + y.
            new_val = 2 * x + y

            # Add the new element back into the heap.
            heapq.heappush(nums, new_val)

            # Count this operation.
            operations += 1

        return operations


# @lc code=end
