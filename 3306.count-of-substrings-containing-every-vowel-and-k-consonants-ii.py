#
# @lc app=leetcode id=3306 lang=python3
#
# [3306] Count of Substrings Containing Every Vowel and K Consonants II
#
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/
#
# algorithms
# Medium (21.62%)
# Likes:    387
# Dislikes: 54
# Total Accepted:    33.8K
# Total Submissions: 104.5K
# Testcase Example:  '"aeioqq"\n1'
#
# You are given a string word and a non-negative integer k.
#
# Return the total number of substrings of word that contain every vowel ('a',
# 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
#
#
# Example 1:
#
#
# Input: word = "aeioqq", k = 1
#
# Output: 0
#
# Explanation:
#
# There is no substring with every vowel.
#
#
# Example 2:
#
#
# Input: word = "aeiou", k = 0
#
# Output: 1
#
# Explanation:
#
# The only substring with every vowel and zero consonants is word[0..4], which
# is "aeiou".
#
#
# Example 3:
#
#
# Input: word = "ieaouqqieaouqq", k = 1
#
# Output: 3
#
# Explanation:
#
# The substrings with every vowel and one consonant are:
#
#
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
#
#
#
#
# Constraints:
#
#
# 5 <= word.length <= 2 * 10^5
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5
#
#
#


# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # vowels
        # vowels = set("aeiou")
        # n = len(word)
        # total_valid = (
        #     0  # total number of substrings that contain every vowel and k consonants
        # )

        # # iterate over all starting indices of the substring
        # for i in range(n):
        #     # use counters to update frequency of vowels and consonants
        #     cons_count = 0
        #     vowel_freq = {v: 0 for v in vowels}

        #     # iterate over all ending indices of the substring
        #     for j in range(i, n):
        #         # check if the new character is a vowel or consonant
        #         if word[j] in vowels:
        #             vowel_freq[word[j]] += 1
        #         else:
        #             cons_count += 1

        #         # if the number of consonants is exactly k, check vowels
        #         if cons_count == k:
        #             # all vowels must appear at least once
        #             if all(vowel_freq[v] > 0 for v in vowels):
        #                 total_valid += 1
        #         # if the number of consonants is greater than k, break
        #         elif cons_count > k:
        #             break
        # return total_valid

        # Approach 2: Sliding Window With Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # n = len(word)
        # vowels = set("aeiou")

        # # Edge case: if k < 0 or k > length of the string, return 0
        # if k < 0 or k > n:
        #     return 0

        # # Build nextConsonant array
        # nextConsonant = [n] * n
        # next_consonant_index = n  # default if no consonant to the right
        # for i in range(n - 1, -1, -1):
        #     nextConsonant[i] = next_consonant_index
        #     if word[i] not in vowels:
        #         next_consonant_index = i

        # # Sliding window
        # start = 0
        # consonant_count = 0
        # vowel_count = Counter()

        # def has_all_vowels(v_count):
        #     return len(v_count) == 5  # all vowels are present

        # total_valid = 0

        # for end in range(n):
        #     # add the current character to the window
        #     c = word[end]
        #     if c in vowels:
        #         vowel_count[c] += 1
        #     else:
        #         consonant_count += 1

        #     # if we have more than k consonants, shrink the window
        #     while consonant_count > k and start <= end:
        #         left_char = word[start]
        #         if left_char in vowels:
        #             vowel_count[left_char] -= 1
        #             if vowel_count[left_char] == 0:
        #                 del vowel_count[left_char]
        #         else:
        #             consonant_count -= 1

        #         start += 1

        #     while consonant_count == k and has_all_vowels(vowel_count):
        #         # if the window is valid, increment the total count
        #         # Count how many ways we can extend this window
        #         # The next consonant index is nextConsonant[end].
        #         # All positions from end up to (nextConsonant[end] - 1) are safe
        #         # because they do not add an extra consonant.
        #         total_valid += (
        #             nextConsonant[end] - end
        #         )  # all substrings ending at end are valid

        #         # shrink from the left to see if another valid window
        #         left_char = word[start]
        #         if left_char in vowels:
        #             vowel_count[left_char] -= 1
        #             if vowel_count[left_char] == 0:
        #                 del vowel_count[left_char]
        #         else:
        #             consonant_count -= 1
        #         start += 1

        # return total_valid

        # Approach 3: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        def count_substrings_at_least_k(word: str, k: int) -> int:
            vowels = set("aeiou")
            n = len(word)

            vowel_count = Counter()
            consonant_count = 0
            result = 0

            start = 0
            for end in range(n):
                c = word[end]
                if c in vowels:
                    vowel_count[c] += 1
                else:
                    consonant_count += 1

                # While window is valid: has all vowels, and at least k consonants
                while len(vowel_count) == 5 and consonant_count >= k:
                    # All extensions from end to n-1 are valid
                    result += n - end

                    # Shrink from the left
                    left_char = word[start]
                    if left_char in vowels:
                        vowel_count[left_char] -= 1
                        if vowel_count[left_char] == 0:
                            del vowel_count[left_char]
                    else:
                        consonant_count -= 1

                    start += 1

            return result

        return count_substrings_at_least_k(word, k) - count_substrings_at_least_k(
            word, k + 1
        )


# @lc code=end
