#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1: Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # bubble sort
        # n = len(nums)
        # swapped = True
        
        # # keep making passes until no swaps are made
        # while swapped:
        #     swapped = False
        #     # one pass of adjacent elements
        #     for i in range(n - 1):
        #         if nums[i] > nums[i + 1]:
        #             # swap if out of order  
        #             nums[i], nums[i + 1] = nums[i + 1], nums[i]
        #             swapped = True
        
        # Approach 2: Counting Sort
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # count the number of 0s, 1s, and 2s
        # counting sort 
        # count = [0,0,0]
        # for num in nums:
        #     count[num] += 1 

        # # overwrite nums in-place by writings 0s, then 1s, then 2s
        # index = 0
        # for color in range(3):
        #     for _ in range(count[color]):
        #         nums[index] = color 
        #         index += 1
        
        # Approach 3: Dutch National Flag Algorithm
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # three pointers: low, mid, high
        # low and mid start at 0, high starts at n - 1
        # if nums[mid] is 0, swap with nums[low] and increment both low and mid
        # if nums[mid] is 1, increment mid
        # if nums[mid] is 2, swap with nums[high] and decrement high
        
        low, mid = 0, 0
        high = len(nums) - 1
        
        # process elements until mid pointer crosses high pointer
        while mid <= high:
            if nums[mid] == 0:
                # expand 0-region: swap into low, advance both pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in the correct middle region: move mid pointer forward
                mid += 1
            else:
                # 2-region: swap into high, move high pointer backward
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        
# @lc code=end

