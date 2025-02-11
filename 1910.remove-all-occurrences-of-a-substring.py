#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/
#
# algorithms
# Medium (78.24%)
# Likes:    2010
# Dislikes: 68
# Total Accepted:    188.1K
# Total Submissions: 240.5K
# Testcase Example:  '"daabcbaabcbc"\n"abc"'
#
# Given two strings s and part, perform the following operation on s until all
# occurrences of the substring part are removed:
#
#
# Find the leftmost occurrence of the substring part and remove it from s.
#
#
# Return s after removing all occurrences of part.
#
# A substring is a contiguous sequence of characters in a string.
#
#
# Example 1:
#
#
# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".
#
#
# Example 2:
#
#
# Input: s = "axxxxyyyyb", part = "xy"
# Output: "ab"
# Explanation: The following operations are done:
# - s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
# - s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
# - s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
# - s = "axyb", remove "xy" starting at index 1 so s = "ab".
# Now s has no occurrences of "xy".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s​​​​​​ and part consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        # Continue while there is an occurrence of 'part' in 's'.
        # while True:
        #     # Find the leftmost occurrence of 'part'.
        #     idx = s.find(part)

        #     # If not found, break out of the loop.
        #     if idx == -1:
        #         break

        #     # Remove the occurrence by slicing before and after the found index.
        #     s = s[:idx] + s[idx + len(part) :]
        # return s

        # Approach 2: Stack
        # Time Complexity: O(n*m)
        # Space Complexity: O(n+m)
        # Initialize a stack to store characters.
        # Initialize an empty list to use as a stack
        # stack = []
        # part_length = len(part)

        # # Process each character in 's'.
        # for char in s:
        #     # Append the current character to the stack.
        #     stack.append(char)

        #     # If the stack is long enough, check if the end of the stack matches 'part'.
        #     if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
        #         # If it matches, remove the last 'part_length' characters from the stack.
        #         for _ in range(part_length):
        #             stack.pop()

        # return "".join(stack)

        # Approach 3: KMP (Knuth-Morris-Pratt) Algorithm
        # Time Complexity: O(n + m)
        # Space Complexity: O(n + m)

        # Edge case: if part is empty, there's nothing to remove.
        if not part:
            return s

        # Precompute the LPS (Longest Prefix Suffix) array for 'part'.
        m = len(part)
        lps = [0] * m  # lps[0] is always 0.
        length = 0  # Length of the previous longest prefix that is also a suffix.
        i = 1  # Start from the second character of 'part'.

        while i < m:
            if part[i] == part[length]:
                # Found a matching character, increase the length and record it.
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Fall back to the last known longest prefix-suffix.
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Repeatedly search for 'part' in 's' and remove its leftmost occurrence.
        while True:
            n = len(s)
            i = 0  # Pointer for the text 's'.
            j = 0  # Pointer for the pattern 'part'.
            found = -1  # Will hold the starting index of 'part' in 's' if found.

            # Perform the KMP search.
            while i < n:
                if s[i] == part[j]:
                    i += 1
                    j += 1
                    # If we have matched the entire pattern, record the index.
                    if j == m:
                        found = i - j
                        break
                else:
                    if j != 0:
                        # Use the LPS array to avoid rechecking characters.
                        j = lps[j - 1]
                    else:
                        i += 1

            # If no occurrence of 'part' is found, break out of the loop.
            if found == -1:
                break

            # Remove the occurrence of 'part' from 's' by slicing it out.
            s = s[:found] + s[found + m :]

        return s


# @lc code=end
