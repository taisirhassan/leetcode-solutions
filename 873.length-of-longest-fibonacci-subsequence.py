#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
#
# algorithms
# Medium (48.44%)
# Likes:    2155
# Dislikes: 82
# Total Accepted:    84.2K
# Total Submissions: 166.1K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# A sequence x1, x2, ..., xn is Fibonacci-like if:
#
#
# n >= 3
# xi + xi+1 == xi+2 for all i + 2 <= n
#
#
# Given a strictly increasing array arr of positive integers forming a
# sequence, return the length of the longest Fibonacci-like subsequence of arr.
# If one does not exist, return 0.
#
# A subsequence is derived from another sequence arr by deleting any number of
# elements (including none) from arr, without changing the order of the
# remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6,
# 7, 8].
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
#
# Example 2:
#
#
# Input: arr = [1,3,7,11,12,14,18]
# Output: 3
# Explanation: The longest subsequence that is fibonacci-like: [1,11,12],
# [3,11,14] or [7,11,18].
#
#
# Constraints:
#
#
# 3 <= arr.length <= 1000
# 1 <= arr[i] < arr[i + 1] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Approach 1: Brute Force with Hash Set
        # Time Complexity: O(n^2log(max(arr)))
        # Space Complexity: O(n)
        # n = len(arr)  # Length of the input array
        # s = set(arr)  # Convert array to set for O(1) lookups
        # max_len = 0  # Variable to track the maximum length found so far

        # # Iterate over all possible starting pairs (i, j)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         x = arr[i]  # First element of the subsequence
        #         y = arr[j]  # Second element of the subsequence
        #         curr_len = 2  # Current length starts at 2

        #         # Keep extending while the next Fibonacci number exists in the set
        #         while (x + y) in s:
        #             next_num = x + y
        #             x = y  # Move forward: second becomes first
        #             y = next_num  # Sum becomes second
        #             curr_len += 1  # Increment length

        #         # Update max_len if current length is at least 3
        #         if curr_len >= 3:
        #             max_len = max(max_len, curr_len)

        # # Return max_len if a valid subsequence was found, else 0
        # return max_len if max_len >= 3 else 0

        # Approach 2: Dynamic Programming with Hash Map
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)

        n = len(arr)  # Length of the input array
        # create a dictionary to quickly map a value to its index
        index = {x: i for i, x in enumerate(arr)}

        # initialize a 2D DP table where every pair (j, k) starts with length 2
        # because any two numbers can trivially form the start of a Fibonacci-like sequence.
        dp = [[2] * n for _ in range(n)]

        ans = 0  # Variable to track the maximum length found so far

        # iterate over all possible pairs (j,k)
        for k in range(n):
            for j in range(k):
                # compute the potential previous element that would complete the Fibonacci condition.
                potential_prev = arr[k] - arr[j]
                # check if this potential element exists in the array and its index is less than j.
                i = index.get(potential_prev)
                if i is not None and i < j:
                    # if found, update dp[j][k] based on the length ending at dp[i][j].
                    dp[j][k] = dp[i][j] + 1
                    # update the maximum length answer.
                    ans = max(ans, dp[j][k])

        # If no valid sequence of length at least 3 is found, return 0.
        return ans if ans >= 3 else 0


# @lc code=end
