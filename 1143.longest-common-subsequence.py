#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (57.85%)
# Likes:    14049
# Dislikes: 213
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
#
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Approach 1: Brute Force Recursion
        # Time Complexity: O(2^(m + n))
        # Space Complexity: O(m + n)
        # def lcs(i: int, j: int) -> int:
        #     # base case: if either string is empty, return 0
        #     if i == 0 or j == 0:
        #         return 0
        #     # if last characters match,, add 1 and recur for the remaining parts
        #     if text1[i - 1] == text2[j - 1]:
        #         return 1 + lcs(i - 1, j - 1)
        #     # if last characters do not match, recur for the remaining parts, return the max of excluding one character from either string
        #     return max(lcs(i - 1, j), lcs(i, j - 1))

        # # start recursion from the full length of both strings
        # return lcs(len(text1), len(text2))

        # Approach 2: Recursion with memoization
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
        # m, n = len(text1), len(text2)

        # # dictionary to store results of subproblems
        # memo = {}

        # # recursive function to return length of LCS of text1[i:] and text2[j:]
        # def lcs(i: int, j: int) -> int:
        #     # base case: if either string is empty, return 0
        #     if i == 0 or j == 0:
        #         return 0
        #     # return cached result if already computed
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     # if last characters match, add 1 and recur for the remaining parts
        #     if text1[i - 1] == text2[j - 1]:
        #         memo[(i, j)] = 1 + lcs(i - 1, j - 1)
        #     else:
        #         # if last characters do not match, recur for the remaining parts, return the max of excluding one character from either string
        #         memo[(i, j)] = max(lcs(i - 1, j), lcs(i, j - 1))
        #     return memo[(i, j)]

        # return lcs(m, n)

        # Approach 3: Dynamic Programming Bottom-Up
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
        # m, n = len(text1), len(text2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # # build the table in a bottom-up manner
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         # if last characters match, add 1 and look diagonally
        #         if text1[i - 1] == text2[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         else:
        #             # if last characters do not match, take the max of excluding one character from either string
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # return dp[m][n]

        # Approach 4: Dynamic Programming Bottom-Up with Space Optimization
        # Time Complexity: O(m * n)
        # Space Complexity: O(min(m, n))
        m, n = len(text1), len(text2)
        # always use the shorter string for the DP columns to save space
        if m < n:
            text1, text2, m, n = text2, text1, n, m

        # initialize two 1D arrays to store the current and previous row of the DP table
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        # fill the dp table row by row
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if last characters match, add 1 and look diagonally for the previous result
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    # if last characters do not match, take the max of excluding one character from either string
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            # after processing row i, the current row becomes the previous row
            prev, curr = curr, prev

        return prev[
            n
        ]  # The result is in prev[n] of the last element of the last processed row


# @lc code=end
