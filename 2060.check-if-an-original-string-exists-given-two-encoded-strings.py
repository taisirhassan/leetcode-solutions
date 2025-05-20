#
# @lc app=leetcode id=2060 lang=python3
#
# [2060] Check if an Original String Exists Given Two Encoded Strings
#

# @lc code=start
from functools import lru_cache
import string
from typing import List


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        # Approach 1: Brute Force Backtracking 
        # Time Complexity: O(sum(26^n))
        # Space Complexity: O(sum(26^n))
        
    #    # generate the full set of possible original strings from an encoded string
    #     def expand(encoded: str) -> set:
    #         results = set() 
           
    #         def backtrack(idx: int, builder: List[str]):
    #            # if we've consumed the entire encoded string, join and store
    #             if idx == len(encoded):
    #                results.add("".join(builder))
    #                return 
               
    #             # if a letter, take it literally
    #             if encoded[idx].isalpha():
    #                 # take letter
    #                 builder.append(encoded[idx]) 
    #                 # move to next character
    #                 backtrack(idx + 1, builder)
    #                 # backtrack
    #                 builder.pop()
                    
    #             else:
    #                 # otherwise, parse a digit-block(up to 3 digits)
    #                 num = 0
    #                 for end in range(idx, min(idx + 3, len(encoded))):
    #                     num = num * 10 + int(encoded[end])
    #                     # try all possible lengths for this block
    #                     for combo in itertools.product(string.ascii_lowercase, repeat=num):
    #                         # take this block
    #                         builder.append("".join(combo))
    #                         # move past this block
    #                         backtrack(end + 1, builder)
    #                         # backtrack
    #                         builder.pop()
    #         backtrack(0, [])
    #         return results 
        
    #     # build both sets of possible original strings and check for intersection
    #     set1 = expand(s1)
    #     set2 = expand(s2)
        
    #     return not set1.isdisjoint(set2)
    
    # Approach 2: Dynamic Programming

        # # helper function to get all possible numbers from substring starting ix
        # def get_numbers(s: str, idx: int) -> List[int]:
        #     nums = []
        #     num = 0
        #     for i in range(idx, min(len(s), idx + 3)):
        #         if s[i].isdigit():
        #             num = num * 10 + int(s[i])
        #         else:
        #             break
        #         nums.append(num)
        #     return nums
        
        # # use memoization for dp state (i, j, diff)
        # @lru_cache(None)
        # def dp(i, j, diff):
        #     # i: index in s1, j: index in s2, diff: s1's "extra" character - s2's
        #     # if at end of both and diff== 0, found a match
        #     if i == len(s1) and j == len(s2):
        #         return diff == 0
            
        #     # try to consume letters if diff == 0 and both are letters and match
        #     if diff == 0:
        #         if i < len(s1) and j < len(s2) and s1[i].isalpha() and s2[j].isalpha() and s1[i] == s2[j]:
        #             # consume both letters
        #             if dp(i + 1, j + 1, 0):
        #                 return True
            
        #     # if diff > 0, need to consume from s2
        #     if diff > 0 and j < len(s2) and s2[j].isalpha():
        #         if dp(i, j + 1, diff -1): return True
            
        #     # if diff < 0, need to consume from s1
        #     if diff < 0 and i < len(s1) and s1[i].isalpha():
        #         if dp(i + 1, j, diff + 1): return True
            
        #     # try to parse numbers in s1 and add to diff
        #     if i < len(s1) and s1[i].isdigit():
        #         for num in get_numbers(s1, i):
        #             # consume this num
        #             if dp(i + len(str(num)), j, diff + num): return True
            
        #     # try to parse numbers in s2 and subtract from diff
        #     if j < len(s2) and s2[j].isdigit():
        #         for num in get_numbers(s2, j):
        #             if dp(i, j + len(str(num)), diff - num): return True
                    
        #     # no match found
        #     return False
        
        # return dp(0,0,0)
        
        n1, n2 = len(s1), len(s2)
        
        @lru_cache(None)
        def dfs(i: int, j:int, diff: int) -> bool:
            # if both strings are consumed, match only if no pending wildcards
            if i == n1 and j == n2:
                return diff == 0
            
            # Case A: diff == 0, must either match letters or spawn wildcards
            if diff == 0:
                # Case A1: both are letters and match
                if i < n1 and j < n2 and s1[i].isalpha() and s2[j].isalpha() and s1[i] == s2[j]:
                    if s1[i] == s2[j] and dfs(i + 1, j + 1, 0): 
                        return True
                
                # Case A2: spawn wildcards from s1 (digit block)
                if i < n1 and s1[i].isdigit():
                    val = 0
                    for k in range(i, min(i +3, n1)):
                        if not s1[k].isdigit():
                            break
                        val = val * 10 + int(s1[k])
                        if dfs(k + 1, j, diff + val):
                            return True
                        
                # Case A3: spawn wildcards from s2 (digit block)
                if j < n2 and s2[j].isdigit():
                    val = 0
                    for k in range(j, min(j + 3, n2)):
                        if not s2[k].isdigit():
                            break
                        val = val * 10 + int(s2[k])
                        if dfs(i, k + 1, diff - val):
                            return True
                return False
                        
            # Case B: diff > 0, -> s1 has extra wildcards to consume into s2
            if diff > 0:
                # Case B1: consume from s2
                if j < n2 and s2[j].isalpha():
                    if dfs(i, j + 1, diff - 1):
                        return True
                # Case B2: spawn wildcards from s2 (digit block)
                if j < n2 and s2[j].isdigit():  
                    val = 0
                    for k in range(j, min(j + 3, n2)):
                        if not s2[k].isdigit():
                            break
                        val = val * 10 + int(s2[k])
                        if dfs(i, k + 1, diff - val):
                            return True
                return False
        
            # Case C: diff < 0, -> s2 has extra wildcards to consume into s1    
            if diff < 0:
                # Case C1: consume from s1
                if i < n1 and s1[i].isalpha():
                    if dfs(i + 1, j, diff + 1):
                        return True
                # Case C2: spawn wildcards from s1 (digit block)
                if i < n1 and s1[i].isdigit():
                    val = 0
                    for k in range(i, min(i + 3, n1)):
                        if not s1[k].isdigit():
                            break
                        val = val * 10 + int(s1[k])
                        if dfs(k + 1, j, diff + val):
                            return True
            return False
        
        # start with both strings empty and diff = 0
        return dfs(0,0,0)
            
                
        

                
                    
                
        
# @lc code=end
