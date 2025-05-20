#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        # Approach 1: Brute Force
        # Time Complexity: O(n * q)
        # Space Complexity: O(n)
        # n = len(nums)
        # # cover[j] = number of queries that cover index j
        # cover = [0] * n
        
        # # build cover counts 
        # for idx, (l, r) in enumerate(queries):
        #     # decrement at each query we could choose j, so count coverage
        #     for j in range(l, r +1):
        #         cover[j] += 1
                
        # # check if we can decrement each nums[i] to zero
        # for j in range(n):
        #     if nums[j] > cover[j]:
        #         return False
        # return True
           
        # Approach 2: Difference Array
        # Time Complexity: O(n + q)
        # Space Complexity: O(n)
        n = len(nums)
        # initalize a difference array to efficiently count coverage
        coverage = [0] * (n + 1)
        
        # build the coverage array for each query
        for l,r in queries:
            coverage[l] += 1
            if r + 1 < n:
                coverage[r + 1] -= 1
                
        # convert coverage array to the actual coverage
        for i in range(1, n):
            coverage[i] += coverage[i-1]
            
        # now check if each nums[i] can be decremented to zero
        for i in range(n):
            if nums[i] > coverage[i]:
                return False  # not enough queries to zero out nums[i]
            
        return True
        
        
        
            
            
        
        
# @lc code=end

