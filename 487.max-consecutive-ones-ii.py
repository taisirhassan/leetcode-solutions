#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (50.82%)
# Likes:    1575
# Dislikes: 27
# Total Accepted:    163.8K
# Total Submissions: 320.2K
# Testcase Example:  '[1,0,1,1,0]'
#
# Given a binary array nums, return the maximum number of consecutive 1's in
# the array if you can flip at most one 0.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: 
# - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4
# consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3
# consecutive ones.
# The max number of consecutive ones is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1,0,1]
# Output: 4
# Explanation: 
# - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4
# consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4
# consecutive ones.
# The max number of consecutive ones is 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
# 
# Follow up: What if the input numbers come in one by one as an infinite
# stream? In other words, you can't store all numbers coming from the stream as
# it's too large to hold in memory. Could you solve it efficiently?
# 
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time: O(n^2)
        # Space: O(1)
        
        # n = len(nums)
        # max_length = 0
        
        # # function to count consecutive ones starting from a given index 
        # def count_ones(start):
        #     count = 0
        #     while start < n and nums[start] == 1:
        #         count += 1
        #         start += 1
        #     return count 
        
        # # first, check without any flip
        # i = 0
        # while i < n:
        #     if nums[i] == 1: 
        #         current_count = count_ones(i)  # count consecutive ones starting from i
        #         max_length = max(max_length, current_count) # update max_length
        #         i += current_count # skip the consecutive ones
        #     else:
        #         i += 1
                
        #     # now, try flipping each zero and count the ones 
        #     for i in range(n):
        #         if nums[i] == 0:
        #             # flip the zero temporarily 
        #             nums[i] = 1
                    
        #             # count the consecutive ones to the left 
        #             left_count = 0
        #             j = i - 1 
        #             while j >= 0 and nums[j] == 1:
        #                 left_count += 1
        #                 j -= 1
                        
        #             # count the consecutive ones to the right
        #             right_count = 0
        #             j = i + 1
        #             while j < n and nums[j] == 1:
        #                 right_count += 1
        #                 j += 1
                        
        #             # update max_length(flipped zero connects left and right segments)
        #             max_length = max(max_length, left_count + right_count + 1)
                    
        #             # restore the original value 
        #             nums[i] = 0
                    
        # return max_length
        
        # Approach 2: Dynamic Programming 
        # Time Complexity: O(n)
        # Space Complexity: O(n) 
        
        # n = len(nums)
        # # dp0[i] = the length of the current consecutive ones ending at index i without flipping any zeros
        # dp0 = [0] * n 
        # # dp1[i] = the length of the current consecutive ones ending at index i with flipping the last zero
        # dp1 = [0] * n
        
        # # base case for the first element, if first element is 1, then dp0[0] = 1 otherwise its's 0
        # dp0[0] = 1 if nums[0] == 1 else 0
        # # for dp1, even if first element is 0, we can flip it to 1, so dp1[0] = 1
        # dp1[0] = 1 
        
        # # initialize the result witht he best we can get at index 0
        # max_length = max(dp0[0], dp1[0])
        
        # # fill in the dp arrays for the rest of the elements 
        # for i in range(1, n):
        #     if nums[i] == 1:
        #         # if the current element is 1, then extend the sequence from the previous element
        #         dp0[i] = dp0[i-1] + 1
        #         dp1[i] = dp1[i-1] + 1
        #     else:
        #         # if the current element is 0, then we can only extend the sequence from the previous element if we flip the last zero
        #         dp0[i] = 0
        #         # with one flip, we can extend the sequence from the last one
        #         dp1[i] = dp0[i-1] + 1
            
        #     # update the max length found so far    
        #     max_length = max(max_length, dp0[i], dp1[i])
            
        # return max_length
        
        # Approach 3: Dynamic Programming with Constant Space
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        # dp0 = 0 # consecutive ones without flipping any zeros
        # dp1 = 0 # consecutive ones count with one flip
        # max_length = 0
        
        # for num in nums:
        #     if num == 1:
        #         dp0 += 1
        #         dp1 += 1
        #     else:
        #         # when a zero is encountered, we can only flip one zero, so we need to update dp1 and dp0 accordingly
        #         dp1 = dp0 + 1
        #         dp0 = 0 # reset as we sequence is broken
                
        #     max_length = max(max_length, dp0, dp1)
            
        # return max_length
        
        # Approach 4: Sliding Window 
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        left = 0 # left pointer of the window
        zero_count = 0 # count of zeros in the window
        max_length = 0 # max length of the window found
        
        # expand the window using the right pointer 
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # shrink the window from the left if there are more than one zero in the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            # update the max length of the window 
            current_window_length = right - left + 1 
        
            max_length = max(max_length, current_window_length)
        
        return max_length
# @lc code=end

