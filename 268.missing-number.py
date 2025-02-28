#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (68.75%)
# Likes:    12864
# Dislikes: 3390
# Total Accepted:    2.8M
# Total Submissions: 4.1M
# Testcase Example:  '[3,0,1]'
#
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.
#
#
# Example 1:
#
#
# Input: nums = [3,0,1]
#
# Output: 2
#
# Explanation:
#
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is
# the missing number in the range since it does not appear in nums.
#
#
# Example 2:
#
#
# Input: nums = [0,1]
#
# Output: 2
#
# Explanation:
#
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is
# the missing number in the range since it does not appear in nums.
#
#
# Example 3:
#
#
# Input: nums = [9,6,4,2,3,5,7,0,1]
#
# Output: 8
#
# Explanation:
#
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is
# the missing number in the range since it does not appear in
# nums.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
#
#
#
# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?
#
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1: Hash Set
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # create a hash set of the numbers in the input list
        # num_set = set(nums)
        # n = len(nums)

        # # check for each number in the range [0,n] if it's missing
        # for i in range(n + 1):
        #     if i not in num_set:
        #         return i  # return the missing number
        # return -1

        # Approach 2: Sorting
        # Time Complexity: O(n log n)
        # Space Complexity: O(1)
        # sort the array in-place
        # nums.sort()
        # n = len(nums)

        # # check each index to see if it the number matches the index
        # for i in range(n):
        #     if i != nums[i]:
        #         return i  # the first mismatch is the missing number
        # return n  # if no mismatches, the missing number is n

        # Approach 3: Sum Formula
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # n = len(nums)
        # # compute the sum of the numbers from 0 to n using the formula
        # expected_sum = n * (n + 1) // 2
        # # compute the actual sum of the numbers in the input list
        # actual_sum = sum(nums)
        # # the difference between the expected and actual sum is the missing number
        # return expected_sum - actual_sum

        # Approach 4: Bit Manipulation (XOR)
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        xor_all = 0
        xor_nums = 0

        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor_all ^= i  # accumulate the XOR of all numbers from 0 to n

        # XOR all numbers in the input list
        for num in nums:
            xor_nums ^= num  # accumulate the XOR of all numbers in the input list

        # the missing number is the XOR of all numbers from 0 to n and all numbers in the input list
        return xor_all ^ xor_nums


# @lc code=end
