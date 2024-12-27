#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Approach 1: Recursion Approach
        # Time complexity: O(2^n) where n is the number of spots
        # Space complexity: O(n) as the maximum depth of the recursion stack would be n
        # self.count = 0  # Initialize count of valid ways
        # n = len(nums)  # Length of the nums array
        
        # def dfs(index: int, current_sum: int):
        #     # Base Case: If all numbers have been processed
        #     if index == n:
        #         if current_sum == target:
        #             self.count += 1  # Found a valid way
        #         return
            
        #     # Recursive Case:
        #     # Option 1: Add the current number
        #     dfs(index + 1, current_sum + nums[index])
            
        #     # Option 2: Subtract the current number
        #     dfs(index + 1, current_sum - nums[index])
        
        # # Start the recursion with index 0 and sum 0
        # dfs(0, 0)
        
        # return self.count  # Return the total count of valid ways
        
        # Approach 2: Recursion with Memoization (Top Down DP)
        # Time complexity: O(n * sum) where n is the number of spots and sum is the sum of all numbers
        # Space complexity: O(n * sum) as we are using a memoization dictionary of size n * sum
        # memo = {} # Initialize a memoization dictionary
        
        # # (index, current_sum) is the key for the memoization dictionary
        
        # def dfs(index, current_sum):
        #     # Base Case: If all numbers have been processed
        #     if index == len(nums):
        #         return 1 if current_sum == target else 0
            
        #     key = (index, current_sum);  # key for the memoization dictionary
            
        #     # If the result for the current index and sum is already computed, return it from the memo
        #     if key in memo:
        #         return memo[key]
            
        #     # Recursive Case:
        #     # Option 1: Add the current number
        #     add = dfs(index + 1, current_sum + nums[index])
            
        #     # Option 2: Subtract the current number
        #     subtract = dfs(index + 1, current_sum - nums[index])
            
        #     # Store the result in the memoization dictionary
        #     memo[key] = add + subtract
            
        #     return memo[key]
        
        # return dfs(0, 0)  # Start the recursion with index 0 and sum 0
        
            
        # Approach 3: Dynamic Programming (Bottom Up DP)
        # Time complexity: O(n * sum) where n is the number of spots and sum is the sum of all numbers
        # Space complexity: O(n * sum) as we are using a DP table of size n * sum
        
        # n = len(nums)
        # dp = [defaultdict(int) for _ in (n+1)]  # Initialize a DP table
        # dp[0][0] = 1   # Base case: one way to reach sum 0 without any numbers
        
        # # Iterate through the numbers in the nums array
        # for i in range(n):
        #     for total, count in dp[i].items():
        #         # Option 1: Add the current number
        #         dp[i+1][current_sum + nums[i]] += count
        #         # Option 2: Subtract the current number
        #         dp[i+1][current_sum - nums[i]] += count
                
        # return dp[n][target]  # Return the total count of valid ways
    
    # Approach 4: Optimized Dynamic Programming (Bottom Up DP)
    # Time complexity: O(n * sum) where n is the number of spots and sum is the sum of all numbers
    # Space complexity: O(sum) as we are using a DP table of size sum
    
        dp = defaultdict(int)  # Initialize a DP table
        dp[0] = 1  # Base case: one way to reach sum 0 without any numbers
        
        # Iterate through the numbers in the nums array
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items(): 
                next_dp[total + num] += count  # Option 1: Add the current number
                next_dp[total - num] += count  # Option 2: Subtract the current number
                
            dp = next_dp  # Update the DP table   
            
        return dp[target]  # Return the total count of valid ways 
        
        
    
    
            
        
        # Approach 5: 2D Dynamic Programming
        # total_sum = sum(nums)
        # dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # # Initialize the first row of the DP table
        # dp[0][nums[0] + total_sum] = 1
        # dp[0][-nums[0] + total_sum] += 1

        # # Fill the DP table
        # for index in range(1, len(nums)):
        #     for sum_val in range(-total_sum, total_sum + 1):
        #         if dp[index - 1][sum_val + total_sum] > 0:
        #             dp[index][sum_val + nums[index] + total_sum] += dp[
        #                 index - 1
        #             ][sum_val + total_sum]
        #             dp[index][sum_val - nums[index] + total_sum] += dp[
        #                 index - 1
        #             ][sum_val + total_sum]

        # # Return the result if the target is within the valid range
        # return (
        #     0
        #     if abs(target) > total_sum
        #     else dp[len(nums) - 1][target + total_sum]
        # )
        
        
        
# @lc code=end

