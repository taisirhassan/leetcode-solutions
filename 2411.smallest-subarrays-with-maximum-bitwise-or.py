#
# @lc app=leetcode id=2411 lang=python3
#
# [2411] Smallest Subarrays With Maximum Bitwise OR
#

# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # approach 1: brute force 
        # time complexity: O(n^3)
        # space complexity: O(n)
        # n = len(nums)
        # answer = [0] * n
        
        # # for each index i, find the smallest subarray that contains nums[i]
        # for i in range(n):
        #     # find max or of subarray starting at i
        #     max_or = 0
        #     for k in range(i, n):
        #         max_or |= nums[k]
        #     # now find smallest j where OR reaches max_or
        #     cur_or = 0
        #     for j in range(i, n):
        #         cur_or |= nums[j]
        #         if cur_or == max_or:
        #             answer[i] = j - i + 1 # length of subarray
        #             break
                    
                
        # return answer
        
        # approach 2: prefix sum, suffix-or + early stop
        # time complexity: O(n^2)
        # space complexity: O(n)
        # n = len(nums)
        # answer = [0] * n
        
        # # build suffix or array
        # suffix_or = [0] * (n + 1)
        # for i in range(n - 1, -1, -1):
        #     suffix_or[i] = suffix_or[i+1] | nums[i]
            
        # # for each index i, find the smallest subarray that contains nums[i]
        # for i in range(n):
        #     # find max or of subarray starting at i
        #     cur_or = 0
        #     target = suffix_or[i]
        #     # now find smallest j where OR reaches max_or
        #     for j in range(i, n):
        #         cur_or |= nums[j]
        #         if cur_or == target:
        #             answer[i] = j - i + 1 # length of subarray
        #             break
                    
        # return answer
        
        # approach 3: bit tracking
        # time complexity: O(n)
        # space complexity: O(n)
        n = len(nums)
        answer = [1] * n
        
        # next pos[b] = smallest index >= i where bit b is set; init to "not seen"
        next_pos = [float('inf')] * 32
        
        # proc from rightmost index back
        for i in range(n - 1, -1, -1):
            x = nums[i]
            # update next_pos for each bit in x
            for b in range(32):
                if x & (1 << b):
                    next_pos[b] = i
                    
                    
            # find farthest next pos for any bit in x among all bits seen so far
            farthest = i
            for b in range(32):
                if next_pos[b] != float('inf'):
                    farthest = max(farthest, next_pos[b])
                    
            # update answer[i] to max length of subarray ending at i
            answer[i] = farthest - i + 1
                        
        return answer
    
        
        # track the last index where each bit is set
    
    
# @lc code=end

