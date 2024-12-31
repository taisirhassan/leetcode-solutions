#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#


# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # Approach 1: Brute Force Approach would involve going over all pairs of spots, calculating their score using the above formula and returning the highest of these scores.
        # Time complexity: O(n^2) where n is the number of spots
        # Space complexity: O(1) as we are using constant space
        # max_score = float('-inf')  # Keeps track of the maximum score
        # n = len(values)            # Number of spots

        # for i in range(n):
        #     for j in range(i+1, n):
        #         score = values[i] + values[j] + i - j
        #         max_score = max(max_score, score)  # Update the max score

        # return max_score

        # Approach 2: Dynamic Programming
        # Time complexity: O(n) where n is the number of spots
        # Space complexity: O(n) as we are using an additional array of size n

        # n = len(values)                     # Number of spots
        # dp = [0] * n                        # Initialize a DP array of size n

        # dp[0] = values[0] + 0               # Base case: first element of the DP array is values[0] + 0
        # max_score = float('-inf')           # Initialize the maximum score

        # # Iterate through the array starting from the second element (index 1)
        # for j in range(1, n):
        #     # Calculate the current score using the best dp[j-1] seen so far and current j
        #     current_score = dp[j-1] + values[j] - j
        #     max_score = max(max_score, current_score)

        #     # Update dp[j] to be the maximum of dp[i-1] and the current (values[j] + i)
        #     dp[j] = max(dp[j-1], values[j] + j)

        # return max_score

        # Approach 3: Optimized Dynamic Programming

        # Time complexity: O(n) where n is the number of spots
        # Space complexity: O(1) as we are using constant space

        # Initialize the maximum value of (values[i] + i) with the first element
        max_prev = values[0] + 0
        max_score = float("-inf")
        n = len(values)  # Number of spots

        # Iterate through the array starting from the second element (index 1)
        for j in range(1, n):
            # Calculate the current score using the best (values[i] + i) seen so far and current j
            current_score = max_prev + values[j] - j
            # Update the max score by comparing existing max_score and current_score
            max_score = max(max_score, current_score)

            # Update max_prev to be the maximum of itself and the current (values[j] + j)
            # This ensures that for the next iteration, we have the best possible (values[i] + i)
            max_prev = max(max_i_plus_val, values[j] + j)

        return max_score


# @lc code=end
