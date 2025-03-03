#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#
# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
#
# algorithms
# Medium (85.28%)
# Likes:    1575
# Dislikes: 107
# Total Accepted:    226.3K
# Total Submissions: 251.9K
# Testcase Example:  '[9,12,5,10,14,3,10]\n10'
#
# You are given a 0-indexed integer array nums and an integer pivot. Rearrange
# nums such that the following conditions are satisfied:
#
#
# Every element less than pivot appears before every element greater than
# pivot.
# Every element equal to pivot appears in between the elements less than and
# greater than pivot.
# The relative order of the elements less than pivot and the elements greater
# than pivot is maintained.
#
# More formally, consider every pi, pj where pi is the new position of the i^th
# element and pj is the new position of the j^th element. If i < j and both
# elements are smaller (or larger) than pivot, then pi < pj.
#
#
#
#
# Return nums after the rearrangement.
#
#
# Example 1:
#
#
# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]
# Explanation:
# The elements 9, 5, and 3 are less than the pivot so they are on the left side
# of the array.
# The elements 12 and 14 are greater than the pivot so they are on the right
# side of the array.
# The relative ordering of the elements less than and greater than pivot is
# also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
#
#
# Example 2:
#
#
# Input: nums = [-3,4,3,2], pivot = 2
# Output: [-3,2,4,3]
# Explanation:
# The element -3 is less than the pivot so it is on the left side of the array.
# The elements 4 and 3 are greater than the pivot so they are on the right side
# of the array.
# The relative ordering of the elements less than and greater than pivot is
# also maintained. [-3] and [4, 3] are the respective orderings.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^6 <= nums[i] <= 10^6
# pivot equals to an element of nums.
#
#
#


# @lc code=start
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Approach 1: Python Stable Sorting
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)

        # custom key function to classify each element relative to the pivot
        # elements less than pivot get key 0, elements equal to pivot get key 1, and elements greater than pivot get key 2
        # return sorted(
        #     nums, key=lambda num: 0 if num < pivot else (1 if num == pivot else 2)
        # )

        # Approach 2: Stable Partition With Temporary Array
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # initialize three lists to store elements less than, equal to, and greater than the pivot
        less = []  # holds elements less than pivot
        equal = []  # holds elements equal to pivot
        greater = []  # holds elements greater than pivot

        # Categorize each element into the appropriate list
        for num in nums:
            if num < pivot:
                less.append(num)  # Add to less if smaller than pivot
            elif num == pivot:
                equal.append(num)  # Add to equal if equal to pivot
            else:
                greater.append(num)  # Add to greater if larger than pivot

        # Concatenate the lists in order: less + equal + greater
        result = less + equal + greater

        # Return the rearranged array
        return result


# @lc code=end
