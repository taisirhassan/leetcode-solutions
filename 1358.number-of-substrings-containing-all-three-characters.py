#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (68.26%)
# Likes:    3812
# Dislikes: 66
# Total Accepted:    245.4K
# Total Submissions: 342.4K
# Testcase Example:  '"abcabc"'
#
# Given a string s consisting only of characters a, b and c.
#
# Return the number of substrings containing at least one occurrence of all
# these characters a, b and c.
#
#
# Example 1:
#
#
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" and "abc" (again).
#
#
# Example 2:
#
#
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "aaacb", "aacb" and "acb".
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: 1
#
#
#
# Constraints:
#
#
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
#
#
#


# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Approach 1: Brute Force (TLE)
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # n = len(s)
        # total_substrings = 0

        # # iterate over all possible starting indices
        # for i in range(n):
        #     # set to keep track of unique characters in current substring
        #     seen = set()
        #     # expand substring from index i to j
        #     for j in range(i, n):
        #         seen.add(s[j])
        #         # if all three characters are present in the substring, increment the count
        #         if len(seen) == 3:
        #             total_substrings += 1
        # return total_substrings

        # Approach 2: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        count = {"a": 0, "b": 0, "c": 0}  # count of each character in the window
        total_substrings = 0
        left = 0  # left pointer of the window

        # expand the window with the right pointer
        for right in range(len(s)):
            count[
                s[right]
            ] += 1  # increment the count of the character at the right pointer

            # while the current window contains at least one of each character
            # move left pointer to the right to count all substring that ends at the right pointer
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                # all substrings from s[left:right + 1] to s[left: len(s)] are valid
                total_substrings += (
                    len(s) - right
                )  # add the count of all substrings that ends at the right pointer

                # shrink the window from the left
                count[s[left]] -= 1
                left += 1
        return total_substrings


# @lc code=end
