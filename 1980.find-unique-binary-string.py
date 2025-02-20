#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#
# https://leetcode.com/problems/find-unique-binary-string/description/
#
# algorithms
# Medium (74.74%)
# Likes:    2433
# Dislikes: 86
# Total Accepted:    268.9K
# Total Submissions: 339.5K
# Testcase Example:  '["01","10"]'
#
# Given an array of strings nums containing n unique binary strings each of
# length n, return a binary string of length n that does not appear in nums. If
# there are multiple answers, you may return any of them.
#
#
# Example 1:
#
#
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
#
#
# Example 2:
#
#
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
#
#
# Example 3:
#
#
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110"
# would also be correct.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.
#
#
#


# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Approach 1: Brute Force
        # Time: O(n^2)
        # Space: O(n)
        nums_set = set(nums)
        n = len(nums)

        def generate(curr: str) -> str:
            # base case: if the length of the current string is equal to n
            if len(curr) == n:
                # If the current string is not in the set of strings, return it
                if curr not in nums_set:
                    return curr
                # otherwise return an empty string
                return ""

            addZero = generate("0" + curr)
            if addZero != "":
                # early return if a valid string is found in this branch.
                return addZero

            # otherwise, try appending '1'.
            return generate(curr + "1")

        # start the recursion with an empty string.
        return generate("")

        # Approach 2: Cantor's Diagonalization
        # Time: O(n)
        # Space: O(n)
        # n = len(nums)  # the length of the string nums
        # result = ""  # the result string

        # # iterate through the length of the string
        # for i in range(n):
        #     # if the current character is 0, append 1 to the result string otherwise append 0
        #     result += "1" if nums[i][i] == "0" else "0"

        # return result  # return the unique binary string


# @lc code=end
