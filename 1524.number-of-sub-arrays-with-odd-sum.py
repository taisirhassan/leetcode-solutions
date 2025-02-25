#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/
#
# algorithms
# Medium (43.85%)
# Likes:    1451
# Dislikes: 64
# Total Accepted:    53.7K
# Total Submissions: 114.4K
# Testcase Example:  '[1,3,5]'
#
# Given an array of integers arr, return the number of subarrays with an odd
# sum.
#
# Since the answer can be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
#
#
# Example 2:
#
#
# Input: arr = [2,4,6]
# Output: 0
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
#
#
# Example 3:
#
#
# Input: arr = [1,2,3,4,5,6,7]
# Output: 16
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 100
#
#
#


# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(arr)

        # Approach 1: Brute Force Approach
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # MOD = 10**9 + 7
        # count = 0
        # n = len(arr)

        # for i in range(n):
        #     current_sum = 0
        #     for j in range(i, n):
        #         current_sum += arr[j]
        #         if current_sum % 2 == 1:  # if the sum is odd
        #             count = (
        #                 count + 1
        #             ) % MOD  # increment the count by 1 and take modulo

        # return count  # return the final count of subarrays with odd sum

        # Approach 2: Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # # dp[i][0] is the number of subarrays ending at i with even sum
        # # dp[i][1] is the number of subarrays ending at i with odd sum
        # dp = [[0, 0] for _ in range(n)]

        # # base case: single element
        # dp[0][arr[0] % 2] = 1

        # result = dp[0][1]  # count of subarrays with odd sum

        # for i in range(1, n):
        #     if arr[i] % 2 == 0:  # if the current element is even
        #         dp[i][0] = dp[i - 1][0] + 1  # even + even = even
        #         dp[i][1] = dp[i - 1][1]  # odd + even = odd
        #     else:  # if the current element is odd
        #         dp[i][0] = dp[i - 1][1]  # odd + odd = even
        #         dp[i][1] = dp[i - 1][0] + 1  # odd + even = odd

        #     result = (result + dp[i][1]) % MOD

        # return result

        # Approach 3: Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # count of prefix sums with even and odd parities
        # start with 1 even count for empty subarray (sum = 0)
        even_count = 1
        odd_count = 0

        result = 0
        current_sum = 0

        for num in arr:
            # update running sum
            current_sum += num

            # if current sum is odd
            if current_sum % 2 == 1:
                # every even prefix sum before current position can form an odd sum subarray
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # every odd prefix sum before current position can form an odd sum subarray
                result = (result + odd_count) % MOD
                even_count += 1

        return result


# @lc code=end
