#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
from collections import Counter


class Solution:
    # def countLargestGroup(self, n: int) -> int:
    #     # Approach 1: Brute Force With String Conversion
    #     # Time Complexity: O(n*log(n))
    #     # Space Complexity: O(k)
    #     # Create a dictionary to store the sum of digits for each number
    #     count_map = defaultdict(int)
        
    #     # Iterate through each number from 1 to n
    #     for i in range(1, n+1):
    #         # Convert the number to a string and sum the digits
    #         count_map[sum(int(digit) for digit in str(i))] += 1
            
    #     # Find the maximum value in the dictionary
    #     max_size = max(count_map.values())
        
    #     # Count the number of keys with the maximum value
    #     return sum(1 for value in count_map.values() if value == max_size)
    
    # # Approach 2: Brute Force Without String Conversion 
    # # Time Complexity: O(n*log(n))
    # # Space Complexity: O(k)
    # def countLargestGroup(self, n: int) -> int:
    #     # Create a dictionary to store the sum of digits for each number
    #     count_map = defaultdict(int)
        
    #     for i in range(1, n+1):
    #         # compute digit sum via division and modulus
    #         x,s = i,0
    #         while x > 0:
    #             s += x % 10 # add the last digit to the sum 
    #             x //= 10 # remove the last digit from x
    #         count_map[s] += 1
            
    #     # find the maximum value in the dictionary
    #     max_size = max(count_map.values())
        
    #     # count the number of keys with the maximum value
    #     return sum(1 for value in count_map.values() if value == max_size)
    
    
    # Approach 3: DP 
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countLargestGroup(self, n: int) -> int:
        # create a list to store the number of groups for each sum
        dp = [0] * (n+1)
        
        # iterate through each number from 1 to n
        for i in range(1, n+1):
            # reuse previously computed results
            dp[i] = dp[i//10] + i % 10
            
        # tally counts of each sum
        count = Counter(dp[1:]) # exclude index 0 because we start from 1
        
        # find the maximum value in the list
        max_size = max(count.values())
       
        # count the number of times the maximum value appears
        return sum(1 for value in count.values() if value == max_size)
# @lc code=end

