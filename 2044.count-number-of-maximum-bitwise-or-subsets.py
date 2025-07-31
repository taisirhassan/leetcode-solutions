#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
from collections import Counter


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Approach 1: Recursion/ DFS 
        # Time Complexity: O(2^n)
        # Space Complexity: O(n)
       # compute max possible OR value
        # max_or = 0
        # for num in nums:
        #     max_or |= num 
            
        # # count the number of subsets with max OR value
        # count = 0
        # def dfs(index, current_or):
        #     nonlocal count
        #     # if we have processed all elements, check if current OR equals max OR
        #     if index == len(nums):
        #         if current_or == max_or:
        #             count += 1
        #         return 
        #     # include the current element in the subset
        #     dfs(index + 1, current_or | nums[index])
        #     # exclude the current element from the subset
        #     dfs(index + 1, current_or)
        
        # dfs(0, 0)
        # return count
        
        # Approach 2: bitmask enumeration 
        # Time Complexity: O(n*2^n)
        # Space Complexity: O(1)
        # start with empty subset -> or = 0, count = 1 
        # dp[or] = count of subsets with OR value = or
        dp = Counter({0: 1})
        for num in nums:
            # for each number, create new subsets with the current number
            # and add them to the dp
            new_dp = Counter(dp) # carry over existing subsets
            for o, cnt in dp.items():
                new_dp[o | num] += cnt
            dp = new_dp
            
            # max possible OR is OR of full array
        full_or = 0
        for num in nums:
            full_or |= num
            
        # return count of subsets with OR value = max possible OR
        return dp[full_or] - (1 if full_or == 0 else 0)
# @lc code=end

