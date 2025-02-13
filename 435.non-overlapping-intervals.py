#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (54.56%)
# Likes:    8464
# Dislikes: 230
# Total Accepted:    719.2K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.
#
# Note that intervals which only touch at a point are non-overlapping. For
# example, [1, 2] and [2, 3] are non-overlapping.
#
#
# Example 1:
#
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are
# non-overlapping.
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
#
#
# Example 3:
#
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
#
#
#


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Approach 1: Brute Force
        # Time complexity: O(2^N)
        # Space complexity: O(N)
        # Edge-case: if no intervals exist.
        # if not intervals:
        #     return 0

        # # Sort intervals by start time.
        # intervals.sort(key=lambda x: x[0])
        # n = len(intervals)

        # def rec(i: int, last_end: int) -> int:
        #     """
        #     Recursive helper function to determine the maximum number of non-overlapping intervals
        #     starting from index i given the end time of the last selected interval (last_end).

        #     Args:
        #         i (int): current index in intervals.
        #         last_end (int): end time of the last interval that was included.

        #     Returns:
        #         int: Maximum count of non-overlapping intervals from index i onward.
        #     """
        #     # Base case: no more intervals to process.
        #     if i == n:
        #         return 0

        #     # Option 1: Skip the current interval.
        #     best = rec(i + 1, last_end)

        #     # Option 2: If current interval doesn't overlap, include it.
        #     if intervals[i][0] >= last_end:
        #         best = max(best, 1 + rec(i + 1, intervals[i][1]))

        #     return best

        # # Start recursion with no interval chosen yet (use -infinity for last_end).
        # max_non_overlap = rec(0, -float("inf"))
        # return n - max_non_overlap

        # Approach 2: Dynamic Programming (Bottom-Up)
        # Time complexity: O(N^2)
        # Space complexity: O(N)
        # Edge-case: if no intervals, no removals needed.
        # if not intervals:
        #     return 0

        # # Sort intervals by their start time.
        # intervals.sort(key=lambda x: x[0])
        # n = len(intervals)

        # # Initialize DP array where each interval can form a chain of length 1 by itself.
        # dp = [1] * n

        # # Build DP table: for each interval i, check all previous intervals j.
        # for i in range(1, n):
        #     for j in range(i):
        #         # If intervals[j] does not overlap with intervals[i]
        #         if intervals[j][1] <= intervals[i][0]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # # Maximum non-overlapping intervals that can be kept.
        # max_non_overlap = max(dp)
        # # Minimum removals = total intervals - maximum non-overlapping intervals.
        # return n - max_non_overlap

        # Approach 3: Dynamic Programming (Top-Down Optimized)
        # Time complexity: O(NlogN)
        # Space complexity: O(N)
        # Base case: if no intervals, no removals needed.
        # if not intervals:
        #     return 0

        # # Sort intervals by their start time.
        # intervals.sort(key=lambda x: x[0])
        # n = len(intervals)

        # # Prepare a list of start times for binary search.
        # starts = [iv[0] for iv in intervals]

        # # Memoization array to cache results for subproblems.
        # dp = [-1] * n

        # def binary_search(i: int) -> int:
        #     """
        #     Find the index of the first interval that starts at or after intervals[i][1]
        #     using binary search.
        #     """
        #     # Use bisect_left on the 'starts' array.
        #     target = intervals[i][1]
        #     return bisect.bisect_left(starts, target, lo=i + 1)

        # def helper(i: int) -> int:
        #     """
        #     Returns the maximum number of non-overlapping intervals
        #     starting from index i.
        #     """
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]

        #     # Option 1: Take the current interval.
        #     next_index = binary_search(i)
        #     take = 1 + helper(next_index)

        #     # Option 2: Skip the current interval.
        #     skip = helper(i + 1)

        #     # Cache the result.
        #     dp[i] = max(take, skip)
        #     return dp[i]

        # # Maximum number of non-overlapping intervals.
        # max_non_overlap = helper(0)

        # # Removals = total intervals - maximum non-overlapping intervals.
        # return n - max_non_overlap

        # Approach 4: Greedy
        # Time complexity: O(NlogN)
        # Space complexity: O(1)
        if not intervals:
            return 0

        # Sort intervals by their end time.
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        # Initialize a count of non-overlapping intervals.
        count = 1  # Always include the first interval.
        # Keep track of the end time of the last added interval.
        end = intervals[0][1]

        # Iterate over the remaining intervals.
        for i in range(1, n):
            # If the current interval starts at or after 'end', it doesn't overlap.
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]  # Update the end to current interval's end.

        # Minimum removals = total intervals - count of non-overlapping intervals.
        return n - count


# @lc code=end
