#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (34.92%)
# Likes:    30298
# Dislikes: 1868
# Total Accepted:    3.6M
# Total Submissions: 10.3M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach 1: Brute Force
        # Time Complexity: O(n^3)
        # Space Complexity: O(1)

        # n = len(s)
        # if n == 0:
        #     return ""
        # longest = ""

        # def is_palindrome(l: int, r: int) -> bool:
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        # # Enumerate every possible substring
        # for i in range(n):
        #     for j in range(i, n):
        #         # Check if substring s[i:j+1] is a palindrome.
        #         if is_palindrome(i, j):
        #             if j - i + 1 > len(longest):
        #                 longest = s[i : j + 1]
        # return longest

        # Approach 2: Expand Around Center (Two Pointers)
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # if not s:
        #     return ""

        # start, end = 0, 0

        # # Iterate over each index as a potential center.
        # for i in range(len(s)):
        #     # --- Check for odd-length palindromes ---
        #     l, r = i, i  # Start with both pointers at the center.
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l) > (end - start):
        #             start, end = l, r
        #         l -= 1
        #         r += 1

        #     # --- Check for even-length palindromes ---
        #     l, r = i, i + 1  # Start with pointers at adjacent indices.
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r - l) > (end - start):
        #             start, end = l, r
        #         l -= 1
        #         r += 1

        # return s[start : end + 1]

        # Approach 3: Dynamic Programming
        # Time Complexity: O(n^2)
        # Space Complexity: O(n^2)
        # n = len(s)
        # if n == 0:
        #     return ""

        # # dp[i][j] will be True if s[i:j+1] is a palindrome.
        # dp = [[False] * n for _ in range(n)]
        # start, max_length = 0, 1  # Single characters are palindromes

        # # All substrings of length 1 are palindromic.
        # for i in range(n):
        #     dp[i][i] = True

        # # Check for substrings of length 2.
        # for i in range(n - 1):
        #     if s[i] == s[i + 1]:
        #         dp[i][i + 1] = True
        #         start = i
        #         max_length = 2

        # # Check for substrings of length 3 and more.
        # for length in range(3, n + 1):  # length is the substring length
        #     for i in range(n - length + 1):
        #         j = i + length - 1  # Ending index of the substring
        #         if s[i] == s[j] and dp[i + 1][j - 1]:
        #             dp[i][j] = True
        #             if length > max_length:
        #                 start = i
        #                 max_length = length

        # return s[start : start + max_length]

        # Approach 4: Manacher's Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not s:
            return ""

        # Transform s: Insert '#' between characters and add boundary markers.
        # For example, "abba" becomes "^#a#b#b#a#$"
        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        p = [0] * n  # Array to hold the palindrome radius at each center.
        center = right = 0  # Current center and right edge of the palindrome.

        for i in range(1, n - 1):
            mirror = 2 * center - i  # Mirror position of i with respect to center.

            # If i is within the right boundary, minimize the expansion.
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around i.
            while T[i + p[i] + 1] == T[i - p[i] - 1]:
                p[i] += 1

            # Update center and right boundary if the palindrome expands past right.
            if i + p[i] > right:
                center = i
                right = i + p[i]

        # Find the maximum element in p.
        max_len, center_index = max((n, i) for i, n in enumerate(p))

        # Determine the start position in the original string.
        start = (center_index - max_len) // 2  # Undo the transformation.
        return s[start : start + max_len]


# @lc code=end
