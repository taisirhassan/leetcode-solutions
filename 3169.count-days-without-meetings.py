#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#
# https://leetcode.com/problems/count-days-without-meetings/description/
#
# algorithms
# Medium (34.15%)
# Likes:    650
# Dislikes: 13
# Total Accepted:    146.7K
# Total Submissions: 310.9K
# Testcase Example:  '10\n[[5,7],[1,3],[9,10]]'
#
# You are given a positive integer days representing the total number of days
# an employee is available for work (starting from day 1). You are also given a
# 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents
# the starting and ending days of meeting i (inclusive).
#
# Return the count of days when the employee is available for work but no
# meetings are scheduled.
#
# Note: The meetings may overlap.
#
#
# Example 1:
#
#
# Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
#
# Output: 2
#
# Explanation:
#
# There is no meeting scheduled on the 4^th and 8^th days.
#
#
# Example 2:
#
#
# Input: days = 5, meetings = [[2,4],[1,3]]
#
# Output: 1
#
# Explanation:
#
# There is no meeting scheduled on the 5^th day.
#
#
# Example 3:
#
#
# Input: days = 6, meetings = [[1,6]]
#
# Output: 0
#
# Explanation:
#
# Meetings are scheduled for all working days.
#
#
#
# Constraints:
#
#
# 1 <= days <= 10^9
# 1 <= meetings.length <= 10^5
# meetings[i].length == 2
# 1 <= meetings[i][0] <= meetings[i][1] <= days
#
#
#


# @lc code=start
# Approach 1: Brute Force
# Time Complexity: O(n * m)
# Space Complexity: O(n)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # # create a list to store the days that are occupied where index i is the day
        # occupied = [False] * (days + 1)
        # # mark the days that are occupied
        # for start, end in meetings:
        #     for day in range(start, end + 1):
        #         occupied[day] = True
        # # count the days that are not occupied
        # return occupied.count(False) - 1
    
    # Approach 2: Difference Array
    # Time Complexity: O(n + m)
    # Space Complexity: O(n)
        # create a difference array to store the days that are occupied where index i is the day
        # diff = [0] * (days + 2)
        
        # # mark the days that are occupied 
        # for start, end in meetings:
        #     # increment the day that the meeting starts
        #     diff[start] += 1 
        #     # decrement the day after the meeting ends
        #     diff[end + 1] -= 1
            
        # free = 0
        # running= 0
        
        # # count the days that are not occupied
        # for i in range(1, days+1):
        #     # add the difference to the running total
        #         running += diff[i]
        #     # if the running total is 0, then the day is free
        #         if running == 0:
        #             free += 1
        # return free
        
        # Approach 3: Merge Intervals
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        
        if not meetings:
            return days 
        # sort the meetings by start time
        meetings.sort()
        # create a list to store the merged meetings
        merged = []
        current_start, current_end = meetings[0]
        for start, end in meetings[1:]:
            # if the current meeting starts before the previous meeting ends, merge the meetings
            if start <= current_end:
                # merge the meetings
                current_end = max(current_end, end)
            else:
                # add the previous meeting to the list
                merged.append((current_start, current_end))
                # update the current meeting
                current_start, current_end = start, end
        # add the last meeting to the list
        merged.append([current_start, current_end])
        
        # total busy days is the sum of the days in the merged meetings
        busy = sum(end - start + 1 for start, end in merged)
        # return the total days minus the busy days
        return days - busy
        


        


# @lc code=end
