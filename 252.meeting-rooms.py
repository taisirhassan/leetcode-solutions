#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (58.61%)
# Likes:    2070
# Dislikes: 110
# Total Accepted:    447.4K
# Total Submissions: 762.1K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
#
#
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
#
#
#


# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # n = len(intervals)
        # # Compare every pair of intervals.
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         # Check if intervals[i] and intervals[j] overlap.
        #         # Overlap exists if one meeting starts before the other ends and vice versa.
        #         if (
        #             intervals[i][0] < intervals[j][1]
        #             and intervals[j][0] < intervals[i][1]
        #         ):
        #             return False  # Overlap found.
        # return True  # No overlaps found.

        # Approach 2: Sorting
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
        # If there are no meetings or just one, there's no conflict.
        if not intervals or len(intervals) < 2:
            return True

        # Sort the intervals based on their start times.
        intervals.sort(key=lambda x: x[0])

        # Iterate over the intervals starting from the second interval.
        for i in range(1, len(intervals)):
            # If the start time of the current meeting is less than the end time of the previous meeting,
            # then the meetings overlap.
            if intervals[i][0] < intervals[i - 1][1]:
                return False  # Cannot attend overlapping meetings.

        # If no overlapping intervals are found, return True.
        return True


# @lc code=end
