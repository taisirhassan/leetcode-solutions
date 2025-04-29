# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#

# @lc code=start
from math import inf
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # # Approach 1: Brute Force 
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # n = len(nums)
        # # global max
        # M = max(nums)
        # ans = 0
        
        # # enumerate all subarrays
        # for i in range(n):
        #     max_count = 0
        #     for j in range(i, n):
        #         if nums[j] == M:
        #             max_count += 1 
        #         if max_count >= k:
        #             ans += 1
        # return ans
        
        # Approach 2: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        count= 0
        left = 0
        max_num = max(nums)
        max_count = 0
        # window right bound
        for right in range(n):
            if nums[right] == max_num:
                max_count += 1  
            # shrink window from left
            while max_count >= k:
                count += n - right # count all subarrays ending at right 
                if nums[left] == max_num:
                    max_count -= 1 # decrease max_count
                left += 1 # move left bound
        return count
                
# @lc code=end
