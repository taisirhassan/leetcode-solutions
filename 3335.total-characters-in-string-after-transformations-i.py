#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#

# @lc code=start
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
       
       # use recurrence relation to compute the length of the string after t transformations
       # prev[x] = length of string after t-1 transformations
       # current[x] = length of string after t transformations
       
        prev = [1] * 26 # length of string after t-1 transformations
        current = [0] * 26 # length of string after t transformations
       
        # base case k = 0: f(c, 0) = 1 for any char c
        for k in range(1, t + 1):
            # build current state from previous state
            for x in range(25):
                # f(c, k) = f(c, k-1) + f(next_char, k-1)
                current[x] = prev[x+1] 
                # for 'z' (x=25): expands to "ab" (x=0, x=1)
                current[25] = (prev[0] + prev[1]) % MOD
            # rotate arrays for next iteration
            prev, current = current, prev
        
        # now prev[x] = f(s[x], t)
        total = 0
        # sum the length of each char after t transformations
        for ch in s:
            # convert char to index (0-25)
            idx = ord(ch) - ord('a')
            # add the length of the char after t transformations
            total = (total + prev[idx]) % MOD
        return total
# @lc code=end

