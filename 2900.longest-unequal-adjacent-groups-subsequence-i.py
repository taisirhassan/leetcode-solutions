#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#

# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        # Approach 1: Brute Force
        # Time Complexity: O(2^n *n)
        # Space Complexity: O(n)
        # n = len(words)
        # best = []
        # def dfs(idx, subseq, last_group):
        #     nonlocal best 
        #     # update best if current subsequence is longer
        #     if len(subseq) > len(best):
        #         best = subseq.copy()
        #     # try to take or skip at each position index 
        #     for i in range(idx, n):
        #         if last_group is None or groups[i] != last_group:
        #             # choose word at index i 
        #             subseq.append(words[i])
        #             # recurse with next index and current group
        #             dfs(i+1, subseq, groups[i])
        #             # backtrack 
        #             subseq.pop()
        #             # skipping is implicit by looping
        # # start with the first word in the subsequence
        # dfs(0, [], None)
        # return best
        
        # Approach 2: Dynamic Programming
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        # n = len(words)
        # dp = [1] * n 
        # prev = [-1] * n
        # # build dp table where dp[i] is the length of the longest subsequence ending at index i
        # for i in range(n):
        #     for j in range(i):
        #         # if current word can be added to the subsequence 
        #         if groups[j] != groups[i] and dp[j] + 1 > dp[i]:
        #             dp[i] = dp[j] + 1
        #             prev[i] = j
        # # find end of the best subsequence 
        # max_len = max(dp)
        # idx = dp.index(max_len)
        # # reconstruct the subsequence from the previous indices 
        # subseq = []
        # while idx != -1:
        #     subseq.append(words[idx])
        #     idx = prev[idx]
        # # reverse the subsequence to get the correct order
        # subseq.reverse()
        # return subseq
        
        
        # Approach 3: Greedy
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # start from first word, for each following word add to result if group is diff from prev word added
        n = len(words)
        res = [words[0]]
        last_group = groups[0]
        # iterate through the rest of the words and groups
        for i in range(1, n):
            # if group is different from the last appended, it can be added
            if groups[i] != last_group:
                res.append(words[i])
                last_group = groups[i]
        return res
        
# @lc code=end

