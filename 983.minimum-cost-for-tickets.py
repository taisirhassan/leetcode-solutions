#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (65.33%)
# Likes:    8121
# Dislikes: 158
# Total Accepted:    343K
# Total Submissions: 521K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# You have planned some train traveling one year in advance. The days of the
# year in which you will travel are given as an integer array days. Each day is
# an integer from 1 to 365.
#
# Train tickets are sold in three different ways:
#
#
# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
#
#
# The passes allow that many days of consecutive travel.
#
#
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days:
# 2, 3, 4, 5, 6, 7, and 8.
#
#
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
#
#
# Example 1:
#
#
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel
# your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.
#
#
# Example 2:
#
#
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: For example, here is one way to buy passes that lets you travel
# your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total, you spent $17 and covered all the days of your travel.
#
#
#
# Constraints:
#
#
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
#
#
#


# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        # # Approach 1: Top Down DP with memoization
        # # Time: O(n) because we are memoizing the results
        # # Space: O(n) for memoization
        # memo = {}

        # def dfs(i):
        #     # Base Case 1: If we have already traveled all the days
        #     if i >= n:
        #         return 0
        #     # If the result is already computed, return it
        #     if i in memo:
        #         return memo[i]

        #     # Otherwise, we need to compute the result for the current day

        #     # Initialize the result to be the cost of traveling on the current day
        #     memo[i] = float("inf")
        #     j = i
        #     for cost, duration in zip(
        #         costs, [1, 7, 30]
        #     ):  # For each type of ticket we can buy (1-day, 7-day, 30-day)
        #         # Find the next day we need to travel
        #         while j < n and days[j] < days[i] + duration:
        #             j += 1
        #         memo[i] = min(
        #             memo[i], cost + dfs(j)
        #         )  # Find the minimum cost of traveling from the next day
        #     return memo[i]

        # return dfs(0)  # Start from the first day

        # Convert the list of travel days to a set for O(1) lookups

        # Approach 2: Bottom Up DP

        days_set = set(days)

        # The last day we need to cover
        last_day = days[-1]

        # Initialize DP array where dp[i] represents the min cost up to day i
        dp = [0] * (last_day + 1)

        # Iterate through all the days
        for day in range(1, last_day + 1):
            if day not in days_set:
                # If it is not a travel day, we don't need to buy a ticket
                dp[day] = dp[day - 1]
            else:
                # Otherwise, we need to buy a ticket
                cost1 = dp[max(0, day - 1)] + costs[0]

                cost7 = dp[max(0, day - 7)] + costs[1]

                cost30 = dp[max(0, day - 30)] + costs[2]

                # The minimum cost for the current day
                dp[day] = min(cost1, cost7, cost30)

        # The answer is the minimum cost up to the last travel day
        return dp[last_day]


# @lc code=end
