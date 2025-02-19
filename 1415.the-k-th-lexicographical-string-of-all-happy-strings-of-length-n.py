#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
#
# algorithms
# Medium (74.74%)
# Likes:    1444
# Dislikes: 39
# Total Accepted:    154.7K
# Total Submissions: 181.3K
# Testcase Example:  '1\n3'
#
# A happy string is a string that:
#
#
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
# 1-indexed).
#
#
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings
# and strings "aa", "baa" and "ababbc" are not happy strings.
#
# Given two integers n and k, consider a list of all happy strings of length n
# sorted in lexicographical order.
#
# Return the kth string of this list or return an empty string if there are
# less than k happy strings of length n.
#
#
# Example 1:
#
#
# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1.
# The third string is "c".
#
#
# Example 2:
#
#
# Input: n = 1, k = 4
# Output: ""
# Explanation: There are only 3 happy strings of length 1.
#
#
# Example 3:
#
#
# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc",
# "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You
# will find the 9^th string = "cab"
#
#
#
# Constraints:
#
#
# 1 <= n <= 10
# 1 <= k <= 100
#
#
#


# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Approach 1: Backtracking
        # Time Complexity: O(3*2^(n-1))
        # Space Complexity: O(n)
        # self.count = 0  # count of happy strings
        # self.res = None  # kth happy string

        # def backtrack(s: str):
        #     # if the length of the string is equal to n then we have found a happy string of length n
        #     if len(s) == n:
        #         self.count += 1  # increment the count of happy strings
        #         # if the count is equal to k, then we have found the kth happy string
        #         if self.count == k:
        #             self.res = s  # store the kth happy string
        #         return

        #     for c in ["a", "b", "c"]:
        #         # if the string is empty or the last character is not equal to c
        #         if not s or s[-1] != c:
        #             # if we have already found the kth happy string, then return
        #             if self.res is not None:
        #                 return
        #             backtrack(s + c)  # add c to the string

        # # Start backtracking from an empty string.
        # backtrack("")
        # # Return the found string or an empty string if kth string does not exist.
        # return self.res if self.res is not None else ""

        # Approach 2: Generate all happy strings and return the kth string if it exists using combinatorics
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # calculate the total number of happy strings of length n.
        total = 3 * 2 ** (n - 1)
        # if k is greater than the total number of happy strings, then return an empty string
        if k > total:
            return ""

        res = ""
        # the first character of the string can be any of the three characters "a", "b", "c". We will fix the first character.
        for c in ["a", "b", "c"]:
            count = 2 ** (
                n - 1
            )  # each first character has 2^(n-1) possible happy strings starting with it.
            if k > count:
                k -= count  # Skip all strings starting with this letter and move to the next letter.
            else:
                res += c  # Fix the letter and move to the next position.
                break

        # build the remaining positions.
        for i in range(1, n):
            # for the next character, exclude the last character of res.
            candidates = [c for c in ["a", "b", "c"] if c != res[-1]]
            # for each candidate, calculate the number of valid strings starting with that candidate.
            for c in candidates:
                # for the current position, there are 2^(n - i - 1) possibilities.
                count = 2 ** (n - i - 1) if (n - i - 1) >= 0 else 1
                if k > count:
                    k -= count  # skip all strings starting with this candidate.
                else:
                    res += (
                        c  # fix the candidate and break to move to the next position.
                    )
                    break

        return res


# @lc code=end
