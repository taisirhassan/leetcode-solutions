#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#
# https://leetcode.com/problems/tuple-with-same-product/description/
#
# algorithms
# Medium (61.36%)
# Likes:    676
# Dislikes: 27
# Total Accepted:    36.5K
# Total Submissions: 57.7K
# Testcase Example:  '[2,3,4,6]'
#
# Given an array nums of distinct positive integers, return the number of
# tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements
# of nums, and a != b != c != d.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# All elements in nums are distinct.
# 
# 
#

# @lc code=start
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        # Approach 1: Brute Force
        # Time Complexity: O(N^4)
        # Space Complexity: O(1)
        # n = len(nums)
        # count = 0

        # # Iterate through all possible quadruple combinations (i, j, k, l)
        # for i in range(n):
        #     for j in range(n):
        #         # Ensure the first two indices are distinct.
        #         if j == i:
        #             continue
        #         for k in range(n):
        #             # Ensure the third index is distinct from i and j.
        #             if k == i or k == j:
        #                 continue
        #             for l in range(n):
        #                 # Ensure the fourth index is distinct from i, j, and k.
        #                 if l == i or l == j or l == k:
        #                     continue
        #                 # Check if the product of the first pair equals the product of the second pair.
        #                 if nums[i] * nums[j] == nums[k] * nums[l]:
        #                     count += 1  # Count this valid quadruple tuple.

        # return count
        # Approach 2: Using Hashmap
        # Time Complexity: O(N^2)
        # Space Complexity: O(N^2)
        
        # Dictionary to count the frequency of the product
        prod_count = defaultdict(int)
        
        n = len(nums)
        
        # Loop through all unique pairs in the array.
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                prod_count[product] += 1  # Increment the count for this product
                
        result = 0 
        # For each product, if there are at least 2 pairs, add the corresponding quadruple count.
        for count in prod_count.values():
            if count >= 2:
                # Each valid pair of pairs gives 8 tuples, and number of ways to choose 2 pair is (count choose 2) = count * (count - 1) / 2
                result += count * (count - 1) * 4 # (count * (count - 1)) // 2 * 8
                
        return result
        
        
# @lc code=end

