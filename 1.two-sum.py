#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (54.47%)
# Likes:    59715
# Dislikes: 2140
# Total Accepted:    15.8M
# Total Submissions: 28.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1: Brute Force
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Approach 2: Sorting
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        # A = []
        # for i, num in enumerate(nums):
        #     A.append((num, i))

        # A.sort()
        # # Initialize two pointers, one at the beginning and one at the end of the sorted list
        # i, j = 0, n - 1
        # # Use two pointers to search for a pair that sums to the target
        # while i < j:
        #     cur = A[i][0] + A[j][0]
        #     if cur == target:
        #         # Return the original indices in sorted order
        #         return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
        #     elif cur < target:
        #         i += 1
        #     else:
        #         j -= 1

        # return []

        # Approach 3: Hash Table (Two-pass)
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Create a dictionary mapping number to its index
        # indices = {}  # Key: num, Value: index

        # # First pass: populate the dictionary
        # for i, num in enumerate(nums):
        #     indices[num] = i

        # # Second pass: check for each number if the complement (target - num) exists
        # for i, num in enumerate(nums):
        #     diff = target - num
        #     # Ensure that the complement exists and is not the same element
        #     if diff in indices and indices[diff] != i:
        #         return [i, indices[diff]]

        # # Return an empty list if no solution found (problem guarantees one solution).
        # return []

        # Approach 4: Hash Table (One-pass)
        # Time complexity: O(n)
        # Space complexity: O(n)
        prevMap = {}  # Key: num, Value: index

        # Iterate over the list
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            diff = target - num

            # Check if the complement has already been seen in previous entries
            if diff in prevMap:
                return [prevMap[diff], i]

            # Save the current number with its index in the dictionary
            prevMap[num] = i

        # Return an empty list if no solution is found (again, problem guarantees a solution)
        return []


# @lc code=end
