#
# @lc app=leetcode id=2579 lang=python3
#
# [2579] Count Total Number of Colored Cells
#
# https://leetcode.com/problems/count-total-number-of-colored-cells/description/
#
# algorithms
# Medium (57.94%)
# Likes:    803
# Dislikes: 86
# Total Accepted:    184.5K
# Total Submissions: 278K
# Testcase Example:  '1'
#
# There exists an infinitely large two-dimensional grid of uncolored unit
# cells. You are given a positive integer n, indicating that you must do the
# following routine for n minutes:
#
#
# At the first minute, color any arbitrary unit cell blue.
# Every minute thereafter, color blue every uncolored cell that touches a blue
# cell.
#
#
# Below is a pictorial representation of the state of the grid after minutes 1,
# 2, and 3.
#
# Return the number of colored cells at the end of n minutes.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 1
# Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
#
#
# Example 2:
#
#
# Input: n = 2
# Output: 5
# Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1
# in the center, so we return 5.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#


# @lc code=start
class Solution:
    def coloredCells(self, n: int) -> int:
        # Approach 1: Iterative Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # if n =1, there's only 1 cell
        # if n == 1:
        #     return 1

        # # initialize the count for the first minute
        # total_cells = 1

        # # iterate from minute 2 to minute n
        # for minute in range(2, n + 1):
        #     # for each minute, the number of cells colored is given by
        #     # 4 * (minute - 1)
        #     total_cells += 4 * (minute - 1)

        # return total_cells

        # Approach 2: Gauss' Formula for Sum of First n Natural Numbers
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        # total cells colored after n minutes is given by 1 + summatin of 4 * i for i in range(1, n)
        return 1 + 4 * (n * (n - 1) // 2)


# @lc code=end
