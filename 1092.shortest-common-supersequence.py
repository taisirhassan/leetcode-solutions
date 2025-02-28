#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (59.66%)
# Likes:    5175
# Dislikes: 76
# Total Accepted:    165.9K
# Total Submissions: 276K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences. If there are multiple valid strings, return
# any of them.
#
# A string s is a subsequence of string t if deleting some number of characters
# from t (possibly 0) results in the string s.
#
#
# Example 1:
#
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first
# "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
#
#
# Example 2:
#
#
# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"
#
#
#
# Constraints:
#
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Approach 1: Top Down DP with Memoization
        # Time: O(m*n * (m+n))
        # Space: O(m*n * (m+n))
        # dp(i,j) returns the shortest common supersequence of str1[i:] and str2[j:]
        # @lru_cache(maxsize=None)
        # def dp(i: int, j: int) -> str:
        #     # base case: if we've reached end of str1, return str2[j:]
        #     if i == len(str1):
        #         return str2[j:]
        #     # if we've reached end of str2, return str1[i:]
        #     if j == len(str2):
        #         return str1[i:]

        #     # if the current characters match, they will be in the supersequence
        #     if str1[i] == str2[j]:
        #         # take matching character and move to next character in both strings
        #         return str1[i] + dp(i + 1, j + 1)
        #     else:
        #         # option 1: include str1[i] in the supersequence and move to next character in str1
        #         option1 = str1[i] + dp(i + 1, j)
        #         # option 2: include str2[j] in the supersequence and move to next character in str2
        #         option2 = str2[j] + dp(i, j + 1)
        #         # return the shorter supersequence
        #         if len(option1) <= len(option2):
        #             return option1
        #         else:
        #             return option2

        # return dp(0, 0)

        # Approach 2: Bottom Up DP
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        n, m = len(str1), len(str2)

        # Initialize dp table where dp[i][j] is the length of SCS for str1[i:] and str2[j:]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base cases:
        # When str1 is exhausted, SCS is the remaining part of str2.
        for j in range(m, -1, -1):
            dp[n][j] = m - j
        # When str2 is exhausted, SCS is the remaining part of str1.
        for i in range(n, -1, -1):
            dp[i][m] = n - i

        # Fill the DP table from bottom-right up.
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        # Reconstruct the SCS from the dp table.
        i, j = 0, 0
        result = []
        while i < n and j < m:
            if str1[i] == str2[j]:
                # When the characters are equal, include the character and move diagonally.
                result.append(str1[i])
                i += 1
                j += 1
            elif dp[i + 1][j] <= dp[i][j + 1]:
                # If including str1[i] leads to a shorter SCS, choose it.
                result.append(str1[i])
                i += 1
            else:
                # Otherwise, choose str2[j].
                result.append(str2[j])
                j += 1

        # Append the remaining part if any string is not yet fully used.
        if i < n:
            result.append(str1[i:])
        if j < m:
            result.append(str2[j:])

        return "".join(result)

        # Approach 3: Bottom Up DP with LCS (Longest Common Subsequence)
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        # n, m = len(str1), len(str2)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]

        # # fill dp table for LCS length
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         # if characters match, increment LCS length by 1
        #         if str1[i - 1] == str2[j - 1]:
        #             dp[i][j] = 1 + dp[i - 1][j - 1]
        #         # otherwise, take the maximum of the two previous LCS lengths
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # # backtrack to find one LCS of str1 and str2
        # i, j = n, m
        # lcs = []
        # while i > 0 and j > 0:
        #     # if characters match, they will be in the LCS
        #     if str1[i - 1] == str2[j - 1]:
        #         lcs.append(str1[i - 1])
        #         i -= 1
        #         j -= 1
        #     # if the characters don't match, move in the direction of the larger LCS
        #     elif dp[i - 1][j] > dp[i][j - 1]:
        #         i -= 1
        #     else:
        #         j -= 1
        # lcs.reverse()  # reverse to get the LCS

        # # build the SCS from the LCS
        # scs = []
        # i = j = 0
        # # for each character in the lcs, add non-lcs characters from str1 and str2
        # for c in lcs:
        #     # add all characters froms str1 until we see the current character in the LCS
        #     while i < n and str1[i] != c:
        #         scs.append(str1[i])
        #         i += 1
        #     # add all characters from str2 until we see the current character in the LCS
        #     while j < m and str2[j] != c:
        #         scs.append(str2[j])
        #         j += 1
        #     # add the character from the LCS and move past it in both strings
        #     scs.append(c)
        #     i += 1
        #     j += 1
        # # add the remaining characters from str1 and str2
        # scs.extend(str1[i:])
        # scs.extend(str2[j:])

        # return "".join(scs)


# @lc code=end
