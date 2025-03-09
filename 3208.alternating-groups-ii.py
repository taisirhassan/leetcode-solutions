#
# @lc app=leetcode id=3208 lang=python3
#
# [3208] Alternating Groups II
#
# https://leetcode.com/problems/alternating-groups-ii/description/
#
# algorithms
# Medium (41.01%)
# Likes:    611
# Dislikes: 58
# Total Accepted:    121.8K
# Total Submissions: 206.9K
# Testcase Example:  '[0,1,0,1,0]\n3'
#
# There is a circle of red and blue tiles. You are given an array of integers
# colors and an integer k. The color of tile i is represented by
# colors[i]:
#
#
# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
#
#
# An alternating group is every k contiguous tiles in the circle with
# alternating colors (each tile in the group except the first and last one has
# a different color from its left and right tiles).
#
# Return the number of alternating groups.
#
# Note that since colors represents a circle, the first and the last tiles are
# considered to be next to each other.
#
#
# Example 1:
#
#
# Input: colors = [0,1,0,1,0], k = 3
#
# Output: 3
#
# Explanation:
#
#
#
# Alternating groups:
#
#
#
#
# Example 2:
#
#
# Input: colors = [0,1,0,0,1,0,1], k = 6
#
# Output: 2
#
# Explanation:
#
#
#
# Alternating groups:
#
#
#
#
# Example 3:
#
#
# Input: colors = [1,1,0,1], k = 4
#
# Output: 0
#
# Explanation:
#
#
#
#
#
# Constraints:
#
#
# 3 <= colors.length <= 10^5
# 0 <= colors[i] <= 1
# 3 <= k <= colors.length
#
#
#


# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n*k)
        # Space Complexity: O(1)

        # n = len(colors)
        # count = 0

        # # iterate over each starting index in a circular array
        # for i in range(n):
        #     is_alternating = True
        #     # check the alternating group starting at index i
        #     for j in range(1, k):
        #         # if the current tile has the same color as the previous tile, the group is not alternating
        #         if colors[(i + j) % n] == colors[(i + j - 1) % n]:
        #             is_alternating = False
        #             break
        #     if is_alternating:
        #         count += 1
        # return count

        # Approach 2: Sliding Window with Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # n = len(colors)
        # # precompute the valid array
        # valid = [0] * n
        # for i in range(n):
        #     valid[i] = 1 if colors[i] != colors[(i + 1) % n] else 0

        # # extend the valid list to handle the circular array
        # valid_extended = valid + valid

        # # the sliding window will be of size k
        # window_length = k - 1
        # current_sum = sum(valid_extended[:window_length])
        # count = 0

        # # check the first window(group at index 0)
        # if current_sum == window_length:
        #     count += 1

        # # slide the window over starting positions from 1 to n -1
        # for i in range(1, n):
        #     # slide the window: remove the leftmost element and add the rightmost element
        #     current_sum -= valid_extended[i - 1]
        #     current_sum += valid_extended[i + window_length - 1]
        #     # check if the window is valid
        #     if current_sum == window_length:
        #         count += 1
        # return count

        # Approach 3: Sliding Window with Modulo Arithmetic
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # n = len(colors)
        # count = 0

        # # helper function to check if the group is alternating or not
        # def valid(i):
        #     return 1 if colors[i] != colors[(i + 1) % n] else 0

        # window_length = k - 1  # the sliding window will be of size k
        # current_sum = 0
        # for i in range(window_length):
        #     current_sum += valid(i)

        # # check the first window(group at index 0)
        # if current_sum == window_length:
        #     count += 1

        # for i in range(1, n):
        #     # slide the window: remove the leftmost element and add the rightmost element
        #     current_sum -= valid(i - 1)
        #     current_sum += valid((i + window_length - 1) % n)
        #     # check if the window is valid
        #     if current_sum == window_length:
        #         count += 1
        # return count

        # Approach 4: Sliding Window with One Pass
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(colors)
        l = 0
        res = 0

        # iterate from 1 to n + k - 1 to handle the circular array
        for r in range(1, n + k - 1):
            if colors[r % n] != colors[(r - 1) % n]:
                # if we've reached window size k, increment the count
                if (r - l + 1) == k:
                    res += 1
                # if the window size is greater than k, slide the window by shifting the left pointer
                elif (r - l + 1) > k:
                    l += 1
                    res += 1  # increment the count because we formed a new group
            else:
                # break the group if the colors are the same, reset window starting just after r - 1 to form a new group, at index r
                l = r
        return res


# @lc code=end
