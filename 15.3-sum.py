#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (35.93%)
# Likes:    32340
# Dislikes: 3035
# Total Accepted:    4.4M
# Total Submissions: 12.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#
#
# Example 3:
#
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Brute Force With Set to Avoid Duplicates
        # Time Complexity: O(n^3)
        # Space Complexity: O(k) where k is the number of unique triplets
        # n = len(nums)
        # res_set = set()  # use a set to avoid duplicates

        # # iterate through every possible triplet combination
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             # if the sum of the triplet is 0, add the sorted tuple to the set
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 # sort the triplet to avoid duplicates
        #                 res_set.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        #                 # convert each tuple in the set to a list
        # return [list(triplet) for triplet in res_set]

        # Approach 2: Two Pointers
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # sort the list in ascending order to use two pointers approach
        nums.sort()
        res = []
        n = len(nums)

        # iterate over the array with index i for the first element of the triplet
        for i in range(n - 2):
            # skip duplicate values for i to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # set the left and right pointers for the remaining elements of the triplet
            left, right = i + 1, n - 1

            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                # if the sum of the triplet is 0, add the triplet to the result

                # if the sum is zero, add the triplet to the result
                if triplet_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # skip duplicate values for left and right to avoid duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # move the left and right pointers to the next unique values after skipping duplicates
                    left += 1
                    right -= 1
                elif triplet_sum < 0:
                    # if the sum is negative, move the left pointer to the right
                    left += 1
                else:
                    # if the sum is positive, move the right pointer to the left
                    right -= 1
        return res


# @lc code=end
