#
# @lc app=leetcode id=2845 lang=python3
#
# [2845] Count of Interesting Subarrays
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # n = len(nums)
        # # build good array
        # good = [1 if num % modulo == k else 0 for num in nums]
        # # build prefix sum array
        # prefix = [0] * (n + 1)
        # # calculate prefix sum of good array by
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + good[i]
        # # count the number of interesting subarrays
        # count = 0
        # # enumerate all possible subarrays
        # for i in range(n):
        #     for j in range(i, n):
        #         # check if the subarray is interesting
        #         cnt = prefix[j + 1] - prefix[i]
        #         if cnt % modulo == k:   
        #             count += 1
        # return count
        
        # Approach 2: Prefix Sum with Hashmap
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        freq = defaultdict(int)
        freq[0] = 1 # empty subarray is interesting
        count = 0
        prefix = 0
        for num in nums:
            if num % modulo == k:
                prefix += 1
            current_mod = prefix % modulo
            
            need = (current_mod - k) % modulo
            count += freq[need]
            # update the frequency of the current prefix sum    
            freq[current_mod] += 1
        return count

        
# @lc code=end

