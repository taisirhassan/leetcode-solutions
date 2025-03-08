#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
#
# algorithms
# Easy (59.56%)
# Likes:    802
# Dislikes: 25
# Total Accepted:    71K
# Total Submissions: 116.8K
# Testcase Example:  '"WBBWWBBWBW"\n7'
#
# You are given a 0-indexed string blocks of length n, where blocks[i] is
# either 'W' or 'B', representing the color of the i^th block. The characters
# 'W' and 'B' denote the colors white and black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive
# black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black
# block.
#
# Return the minimum number of operations needed such that there is at least
# one occurrence of k consecutive black blocks.
#
#
# Example 1:
#
#
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and
# 4th blocks
# so that blocks = "BBBBBBBWBW".
# It can be shown that there is no way to achieve 7 consecutive black blocks in
# less than 3 operations.
# Therefore, we return 3.
#
#
# Example 2:
#
#
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
#
#
#
# Constraints:
#
#
# n == blocks.length
# 1 <= n <= 100
# blocks[i] is either 'W' or 'B'.
# 1 <= k <= n
#
#
#


# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Approach 1: Brute Force Approach
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        n = len(blocks)
        # min_recolours = float("inf")

        # # iterate over all possible substrings of length k
        # for start in range(n - k + 1):
        #     # count number of "B" in the substring
        #     countB = 0
        #     for i in range(start, start + k):
        #         if blocks[i] == "B":
        #             countB += 1
        #     # calculate the number of recolours needed
        #     recolours = k - countB
        #     min_recolours = min(min_recolours, recolours)

        # return min_recolours

        # Approach 2: Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # prefix = [0] * (n + 1)

        # # precompute the prefix sum, where prefix[i] is the number of "B" in the substring blocks[:i]
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + (1 if blocks[i] == "B" else 0)

        # min_recolours = float("inf")
        # # check each substring of length k
        # for start in range(n - k + 1):
        #     # number of 'B' in the substring blocks[start:start+k]
        #     countB = prefix[start + k] - prefix[start]

        #     recolours = k - countB
        #     min_recolours = min(min_recolours, recolours)

        # return min_recolours

        # Approach 3: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # count 'B' in the first window
        current_B_count = 0
        for i in range(k):
            if blocks[i] == "B":
                current_B_count += 1

        # the recolours needed in the first window
        min_recolours = k - current_B_count
        # slide the window across the string
        for start in range(1, n - k + 1):
            # remove the leftmost character from the count
            if blocks[start - 1] == "B":
                current_B_count -= 1
            # add the rightmost character to the count
            if blocks[start + k - 1] == "B":
                current_B_count += 1
            # update the minimum recolours needed
            min_recolours = min(min_recolours, k - current_B_count)

        return min_recolours


# @lc code=end
