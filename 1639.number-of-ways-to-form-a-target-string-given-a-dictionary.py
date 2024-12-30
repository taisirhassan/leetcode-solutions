#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#

# @lc code=start
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0]) # Length of the words
        n = len(target) # Length of the target
        
        # # Approach 1: Brute Force with Recursion 
        # # Time: O((m*n)^k)
        # # Space: O(n)
        # # Count the frequency of each character in each word
        # freq = [0] * m # Initialize the frequency array
        # for k in range(m):
        #     count = 0
        #     for word in words:
        #         if word[k] == target[0]:
        #             count += 1
        #     freq[k] = count
            
        #     # Recursive helper function
        # def dfs(pos, k):
        #     # Base cases
        #     # Base Case 1: If all characters in target are formed
        #     if pos == n:
        #         return 1

        #     # Base Case 2: If no more positions left in words but target not fully formed
        #     if k == m:
        #         return 0 # No valid way along this path
        
        #     # Option 1: Skip the current position in words and move to the next position     
        #     ways = dfs(pos, k + 1)
        
        #     # Option 2: Use the current position if it matches the target character
        #     current_char = target[pos]  # Current target character to match
        #     count = 0 # Initialize count of matching characters at position k
        
        #     # Iterate through each word to count how many have the current target character at position k 
        #     for word in words:
        #         if word[k] == current_char:
        #             count += 1
                    
        #     if count > 0:
        #         # If there are matching characters, multiply by the number of ways to form the remaining target
        #         ways += count * dfs(pos + 1, k + 1)
                
        #         # Apply modulo to keep the number within the bounds
        #         ways %= MOD
                
        #     return ways # Return the total number of ways to form the target string for this stage
        
        # # Initiate the recursion starting from position 0 in target and position 0 in words
        # return dfs(0,0)
        
        # # Approach 2: Recursion with Memoization
        # # Time: O(w * k + t * k))
        # # Step 1: Precompute the frequency of each character at each position
        # # freq[k][c] will store the number of words where words[j][k] == c
        # # Initialize a list of lists with zeros for all positions and 26 lowercase letters
        # freq = [[0] * 26 for _ in range(m)] # Initialize the frequency array
        # # Iterate through each word in the list of words
        # for word in words:
        #     # Iterate through each character and its index in the current word
        #     for k, c in enumerate(word):
        #         # COnvert the character to its corresponding index by subtracting ord('a')
        #         c_idx = ord(c) - ord('a')
        #         # Increment the frequency count for the character at position k
        #         freq[k][c_idx] += 1
                
        # # Step 2: Define a memoization hash map
        # # The key will be a tuple (pos, k), representing the current state
        # # The value will be the number of ways to form target[pos:] starting from words' position idx
        # memo = {} # (pos, k) -> numWays
        # def dfs(pos,k):
        #     # Base Case 1: If all characters in target are formed
        #     if pos == n:
        #         return 1  # One valid way found

        #     # Base Case 2: If no more positions left in words but target not fully formed
        #     if k == m:
        #         return 0  # No valid way along this path

        #     # Check if the current state has already been computed
        #     key = (pos, k)
        #     if key in memo:
        #         return memo[key]  # Return the stored result to avoid recomputation
            
        #     # Option 1: Skip the current position in words and move to the next position
        #     ways = dfs(pos, k + 1)

        #     # Option 2: Use the current position if it matches the target character
        #     current_char = target[pos]  # Current target character to match
        #     c_idx = ord(current_char) - ord('a')  # Convert to index

        #     # Number of words that have the current target character at position idx
        #     count = freq[k][c_idx]

        #     if count > 0:
        #         # Multiply the number of matching words by the ways to form the remaining target
        #         ways += count * dfs(pos + 1, k + 1)
        #         # Apply modulo to keep the number within bounds
        #         ways %= MOD

        #     # Store the computed result in the memoization hash map
        #     memo[key] = ways

        #     return ways  # Return the total ways for this state

        # # Step 3: Initiate the recursion starting from position 0 in target and position 0 in words
        # return dfs(0, 0)
        
        # Approach 3: Dynamic Programming Bottom-Up
        # Time: O(m * n)
        # Space: O(26*m + n)
        
        # # Step 1: Precompute the frequency of each character at each position
        # # freq[k][c] will store the number of words where words[j][k] == c
        # # Initialize a list of lists with zeros for all positions and 26 lowercase letters
        # freq = [ [0] * 26 for _ in range(m) ]

        # # Iterate through each word in the list of words
        # for word in words:
        #     # Iterate through each character and its index in the current word
        #     for k, char in enumerate(word):
        #         # Convert character to its corresponding index (0 for 'a', 1 for 'b', etc.)
        #         c_idx = ord(char) - ord('a')
        #         # Increment the frequency count for this character at position k
        #         freq[k][c_idx] += 1
                
        # # Step 2: Initialize the DP table
        # # dp[i] will represent the number of ways to form the first i characters of the target
        # # Initialize all counts to 0
        # dp = [0] * (n+1) # Initialize the DP table with zeros
        # dp[0] = 1 # Base case: 1 way to form an empty string
        
        # # Step 3: Iterate over each position in the words
        # for k in range(m):
        #     # Iterate through the target string from end to start
        #     # This ensures that dp[i] is updated based on dp[i-1] from the previous step
        #     for i in range(n, 0, -1):
        #         # Current character in the target that we're trying to form
        #         current_char = target[i - 1]
        #         # Convert character to its corresponding index
        #         c_idx = ord(current_char) - ord('a')
        #         # Update dp[i] by adding the number of ways to form the first (i-1) characters
        #         # multiplied by the frequency of the current character at position k
        #         dp[i] = (dp[i] + dp[i - 1] * freq[k][c_idx]) % MOD

        # # Step 4: The final answer is the number of ways to form the entire target string
        # return dp[n]
        
        # Approach 4: Dynamic Programming Bottom-Up with Space Optimization
        # Time: O(m * n)
        # Space: O(n)
        
        # Step 1: Precompute the frequency of each character at each position
        # freq[k][c] will store the number of words where words[j][k] == c
        # Initialize a list of lists with zeros for all positions and 26 lowercase letters
        freq = [ [0] * 26 for _ in range(m) ]

        # Iterate through each word in the list of words
        for word in words:
            # Iterate through each character and its index in the current word
            for k, char in enumerate(word):
                # Convert character to its corresponding index (0 for 'a', 1 for 'b', etc.)
                c_idx = ord(char) - ord('a')
                # Increment the frequency count for this character at position k
                freq[k][c_idx] += 1

        # Step 2: Initialize two DP arrays to represent previous and current states
        # prev_dp[i] will store the number of ways to form the first i characters before processing position k
        # Initialize all counts to 0
        prev_dp = [0] * (n + 1)
        prev_dp[0] = 1  # Base case: One way to form an empty target string
        
        # Step 3: Iterate over each position in the words
        for k in range(m):
            # Initialize the current DP array as a copy of the previous DP array
            # This represents skipping the position k in the words
            curr_dp = prev_dp.copy()
            
            # Iterate through the target string from the first character to the last 
            for i in range(1, n + 1):
                # Current character in the target that we're trying to form
                current_char = target[i - 1]
                # Convert character to its corresponding index
                c_idx = ord(current_char) - ord('a')
                # Update curr_dp[i] by adding the number of ways to form the first (i-1) characters
                # multiplied by the frequency of the current character at position k
                curr_dp[i] = (curr_dp[i] + prev_dp[i - 1] * freq[k][c_idx]) % MOD
                
            # Update the previous DP array to the current DP array for the next iteration
            prev_dp = curr_dp
            
        # Step 4: The final answer is the number of ways to form the entire target string
        return prev_dp[n]
        

        
        
                    
        
# @lc code=end

