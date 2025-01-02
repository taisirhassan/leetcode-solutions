#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#
# https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
#
# algorithms
# Medium (53.39%)
# Likes:    713
# Dislikes: 45
# Total Accepted:    83.1K
# Total Submissions: 129.4K
# Testcase Example:  '["aba","bcb","ece","aa","e"]\n[[0,2],[1,4],[1,1]]'
#
# You are given a 0-indexed array of strings words and a 2D array of integers
# queries.
#
# Each query queries[i] = [li, ri] asks us to find the number of strings
# present in the range li to ri (both inclusive) of words that start and end
# with a vowel.
#
# Return an array ans of size queries.length, where ans[i] is the answer to the
# i^th query.
#
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
#
#
# Example 1:
#
#
# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]
# Explanation: The strings starting and ending with a vowel are "aba", "ece",
# "aa" and "e".
# The answer to the query [0,2] is 2 (strings "aba" and "ece").
# to query [1,4] is 3 (strings "ece", "aa", "e").
# to query [1,1] is 0.
# We return [2,3,0].
#
#
# Example 2:
#
#
# Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
# Output: [3,2,1]
# Explanation: Every string satisfies the conditions, so we return [3,2,1].
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^5
# 1 <= words[i].length <= 40
# words[i] consists only of lowercase English letters.
# sum(words[i].length) <= 3 * 10^5
# 1 <= queries.length <= 10^5
# 0 <= li <= ri < words.length
#
#
#


# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Approach 1: Brute Force
        # Time: O(n * m) where n is the number of queries and m is the length of the longest word
        # Space: O(1)

        # Initialize the vowels
        vowels = set("aeiou")

        # Helper function to check if a word starts and ends with a vowel
        def isVowel(word):
            # Check if the first and last character of the word is a vowel
            return word[0] in vowels and word[-1] in vowels

        # # Initialize the result array
        # result = []
        # # Iterate through each query

        # for li, ri in queries:
        #     count = 0  # Initialize count for the current query

        #     # Iterate through the specified range of words
        #     for i in range(li, ri + 1):
        #         if isVowel(words[i]):
        #             count += 1  # Increment count if the word is valid

        #     result.append(count)  # Append the result for the current query

        # return result

        # Approach 2: Prefix Sum
        # Time: O(m + n)) where n is the number of words and m is the length of the longest word
        # Space: O(m) for the prefix sum array where m is the length of the longest word

        # Initialize the prefix sum array
        prefix_sum = [0] * len(words)

        # Populate the prefix sum array
        for i, word in enumerate(words):
            if isVowel(word):
                prefix_sum[i] = 1
                if i == 0:
                    prefix_sum[i] = 1  # First word is valid
                else:
                    prefix_sum[i] = (
                        prefix_sum[i - 1] + 1
                    )  # Increment the prefix sum count

            else:
                if i != 0:
                    prefix_sum[i] = prefix_sum[i - 1]  # Carry forward the count

        # Initialize the result array
        result = []

        # Iterate through each query
        for li, ri in queries:
            if li == 0:
                # If the range starts at 0, take prefix[ri] as is
                result.append(prefix_sum[ri])
            else:
                # Otherwise, subtract the prefix sums to get the count in range
                result.append(prefix_sum[ri] - prefix_sum[li - 1])

        return result


# @lc code=end
