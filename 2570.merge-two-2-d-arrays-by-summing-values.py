#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
#
# algorithms
# Easy (74.17%)
# Likes:    750
# Dislikes: 31
# Total Accepted:    175.4K
# Total Submissions: 213.2K
# Testcase Example:  '[[1,2],[2,3],[4,5]]\n[[1,4],[3,2],[4,1]]'
#
# You are given two 2D integer arrays nums1 and nums2.
#
#
# nums1[i] = [idi, vali] indicate that the number with the id idi has a value
# equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value
# equal to vali.
#
#
# Each array contains unique ids and is sorted in ascending order by id.
#
# Merge the two arrays into one array that is sorted in ascending order by id,
# respecting the following conditions:
#
#
# Only ids that appear in at least one of the two arrays should be included in
# the resulting array.
# Each id should be included only once and its value should be the sum of the
# values of this id in the two arrays. If the id does not exist in one of the
# two arrays, then assume its value in that array to be 0.
#
#
# Return the resulting array. The returned array must be sorted in ascending
# order by id.
#
#
# Example 1:
#
#
# Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
# Output: [[1,6],[2,3],[3,2],[4,6]]
# Explanation: The resulting array contains the following:
# - id = 1, the value of this id is 2 + 4 = 6.
# - id = 2, the value of this id is 3.
# - id = 3, the value of this id is 2.
# - id = 4, the value of this id is 5 + 1 = 6.
#
#
# Example 2:
#
#
# Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
# Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
# Explanation: There are no common ids, so we just include each id with its
# value in the resulting list.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 200
# nums1[i].length == nums2[j].length == 2
# 1 <= idi, vali <= 1000
# Both arrays contain unique ids.
# Both arrays are in strictly ascending order by id.
#
#
#


# @lc code=start
class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        # Approach 1: Using A Dictionary
        # Time Complexity: O(n + m + k * log(k))
        # Space Complexity: O(n + m)

        # # Initialize a dictionary to store id:value mappings
        # id_to_value = {}

        # # Process nums1: Add each id and its value to the dictionary
        # for id_val, val in nums1:
        #     id_to_value[id_val] = id_to_value.get(id_val, 0) + val

        # # Process nums2: Add values to existing ids or create new entries
        # for id_val, val in nums2:
        #     id_to_value[id_val] = id_to_value.get(id_val, 0) + val

        # # Convert dictionary to list of [id, value] pairs and sort by id
        # result = sorted([[id_val, val] for id_val, val in id_to_value.items()])

        # # Return the merged, sorted array
        # return result

        # Approach 2: Using Two Pointers
        # Time Complexity: O(n + m)
        # Space Complexity: O(n + m)

        # Initialize pointers for nums1 and nums2
        i, j = 0, 0
        merged = []  # Result list

        # Loop until we reach the end of one list
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]

            # If both ids are the same, sum the values and add to result
            if id1 == id2:
                merged.append([id1, val1 + val2])
                i += 1
                j += 1
            # If id from nums1 is smaller, append it
            elif id1 < id2:
                merged.append([id1, val1])
                i += 1
            # If id from nums2 is smaller, append it
            else:
                merged.append([id2, val2])
                j += 1

        # Append the remaining elements from nums1 (if any)
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Append the remaining elements from nums2 (if any)
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged


# @lc code=end
