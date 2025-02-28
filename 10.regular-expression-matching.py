#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (28.70%)
# Likes:    12555
# Dislikes: 2255
# Total Accepted:    1.1M
# Total Submissions: 3.8M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
#
#
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
#
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
#
#
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Approach 1: Recursion with Memoization
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        # dictionary to memoize states (i, j)
        # memo = {}

        # def dp(i: int, j: int) -> bool:
        #     # if we have already computed the state, return it
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     # base case: if pattern is exhausted, string must be exhausted as well
        #     if j == len(p):
        #         return i == len(s)

        #     # check if the current characters match(considering '.' can match any character)
        #     first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

        #     # if there's a '*' in the pattern following the current character in p.
        #     if j + 1 < len(p) and p[j + 1] == "*":
        #         # two possibilities:
        #         # 1. skip "character*": dp(i, j+2)
        #         # 2. if there's a match, "consume" one character from the string and continue matching: dp(i+1, j)
        #         memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
        #         return memo[(i, j)]
        #     else:
        #         # otherwise, move to the next character in both string and pattern
        #         memo[(i, j)] = first_match and dp(i + 1, j + 1)
        #         return memo[(i, j)]

        # return dp(0, 0)

        # Approach 2: Dynamic Programming (Bottom-Up)
        # Time Complexity: O(m*n)
        # Space Complexity: O(m*n)
        m, n = len(s), len(p)
        # create a dp table with m+1 rows and n+1 columns
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # base case: empty string matches empty pattern
        dp[m][n] = True

        # fill the table backwards
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                # check if the current characters match(considering '.' can match any character)
                first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                # if there's a '*' in the pattern following the current character in p.
                if j + 1 < len(p) and p[j + 1] == "*":
                    # two possibilities where dp[i][j] is True:
                    # 1. skip "character*": dp[i][j+2]
                    # 2. if there's a match, "consume" one character from the string and continue matching: dp[i+1][j]
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # otherwise if no star, move to the next character in both string and pattern
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]


# @lc code=end
