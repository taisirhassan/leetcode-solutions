#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (55.49%)
# Likes:    8775
# Dislikes: 271
# Total Accepted:    475.4K
# Total Submissions: 852.6K
# Testcase Example:  '"aab"'
#
# Given a string s, rearrange the characters of s so that any two adjacent
# characters are not the same.
#
# Return any possible rearrangement of s or return "" if not possible.
#
#
# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Approach 1: Brute Force - Backtracking
        # Time Complexity: O(N! * N)
        # Space Complexity: O(N)
        # n = len(s)
        # freq = {}
        # for char in s:
        #     freq[char] = freq.get(char, 0) + 1

        # # check if a valid reorganization is possible
        # if any(count > (n + 1) // 2 for count in freq.values()):
        #     return ""

        # result = [None] * n

        # def backtrack(index):
        #     # base case: if we have filled the entire result list, a valid reorganization is found
        #     if index == n:
        #         return True
        #     # iterate over each character in the frequency dictionary
        #     for char in list(freq.keys()):
        #         # skip if this character is not available
        #         if freq[char] == 0:
        #             continue
        #         # check that the current character is not the same as the previous character
        #         if index > 0 and result[index - 1] == char:
        #             continue

        #         # place the current character at the current index
        #         result[index] = char
        #         freq[char] -= 1  # decrement the frequency of the current character

        #         # recursively place the next character
        #         if backtrack(index + 1):
        #             return True
        #         # backtrack: restore the frequency of the current character if the placement is not possible
        #         freq[char] += 1
        #     return False  # no valid reorganization is found

        # # start backtracking from the first character
        # if backtrack(0):
        #     return "".join(result)
        # return ""

        # Approach 2: Greedy Approach using Max Heap
        # Time Complexity: O(NlogA) where A is the size of the alphabet
        # Space Complexity: O(A)
        # count = {}  # count of each character in the string
        # for char in s:
        #     count[char] = count.get(char, 0) + 1

        # n = len(s)
        # for freq in count.values():
        #     if freq > (n + 1) // 2:
        #         return ""

        # # build a max heap of the characters, store negative frequency to get the maximum frequency character
        # heap = [(-freq, char) for char, freq in count.items()]
        # heapq.heapify(heap)

        # result = []  # store the result

        # # while there are at least two characters left in the heap
        # while len(heap) >= 2:
        #     # extract the two characters with the highest frequency
        #     freq1, char1 = heapq.heappop(heap)
        #     freq2, char2 = heapq.heappop(heap)

        #     # append the characters to the result
        #     result.append(char1)
        #     result.append(char2)

        #     # increment the counts
        #     if freq1 + 1 < 0:
        #         heapq.heappush(heap, (freq1 + 1, char1))
        #     if freq2 + 1 < 0:
        #         heapq.heappush(heap, (freq2 + 1, char2))

        # # if there is one character left in the heap
        # if heap:
        #     freq, char = heapq.heappop(heap)
        #     result.append(char)

        # return "".join(result)

        # Approach 3: Greedy Approach using Sorting
        # Time Complexity: O(n + klogk) where k is the number of unique characters in the string
        # Space Complexity: O(k) 
        # n = len(s)
        # count = {}
        # for char in s:
        #     count[char] = count.get(char, 0) + 1

        # if max(count.values()) > (n + 1) // 2:
        #     return ""

        # # sort the characters by freqeuncy in descending order,
        # sorted_chars = sorted(count.items(), key=lambda x: -x[1])

        # res = [""] * n

        # index = 0

        # for char, freq in sorted_chars:
        #     for _ in range(freq):
        #         res[index] = char  # place the character at the current index
        #         index += 2  # move to the next even index
        #         # if the index exceeds the length of the string, move to the next odd index
        #         if index >= n:
        #             index = 1

        # return "".join(res)


# @lc code=end
