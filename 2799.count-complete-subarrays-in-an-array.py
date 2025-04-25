#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        # total distinct elements in the array
        # total_distinct = len(set(nums))
        # n = len(nums)
        # count = 0
        # # enumerate all possible subarrays
        # for i in range(n):
        #     seen = set()
        #     for j in range(i, n):
        #         seen.add(nums[j])
        #         # check if the subarray is complete by comparing the size of the set with the total distinct elements
        #         if len(seen) == total_distinct:
        #             count += 1
        # # move to the next subarray 
        # return count
        
        # Approach 2: Sliding Window
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # total distinct elements in the array
        # K = len(set(nums))
        # # length of the array
        # n = len(nums)
        
        # freq = defaultdict(int) # frequency of each element in the current window
        # distinct = 0 # number of distinct elements in the current window
        # left = 0 # left pointer of the window
        # count = 0 # number of complete subarrays
        # # grow the window to the right
        # for right in range(n):
        #     # add the current element to the window and update the frequency    
        #     if freq[nums[right]] == 0:
        #         distinct += 1
        #     freq[nums[right]] += 1
        #     # shrink the window from the left once it contains all distinct elements
        #     while distinct == K:
        #         # every extension of the window by 1 will result in a complete subarray
        #         count += n - right
        #         # remove the leftmost element from the window and update the frequency  
        #         freq[nums[left]] -= 1
        #         if freq[nums[left]] == 0:
        #             distinct -= 1
        #         left += 1
        # return count
        
        # Approach 3: Two Pointers
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # total distinct elements in the array
        n = len(nums)
        distinct_total = len(set(nums))
        
        def at_most(k: int) -> int:
            freq = defaultdict(int)
            left = 0
            count = 0
            distinct = 0
            for right, num in enumerate(nums):
                if freq[num] == 0:
                    distinct += 1
                freq[num] += 1
                # shrink the window from the left if it contains more than k distinct elements
                while distinct > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                # every extension of the window by 1 will result in a complete subarray
                count += right - left + 1
            return count
        
        total_subarrays = n * (n + 1) // 2 # total number of subarrays in the array (n choose 2)
        # subtract the number of subarrays that contain less than K distinct elements
        return total_subarrays - at_most(distinct_total - 1)
                
# @lc code=end

