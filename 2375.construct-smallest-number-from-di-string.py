#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#
# https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
#
# algorithms
# Medium (76.25%)
# Likes:    1569
# Dislikes: 76
# Total Accepted:    150K
# Total Submissions: 174.6K
# Testcase Example:  '"IIIDIDDD"'
#
# You are given a 0-indexed string pattern of length n consisting of the
# characters 'I' meaning increasing and 'D' meaning decreasing.
# 
# A 0-indexed string num of length n + 1 is created using the following
# conditions:
# 
# 
# num consists of the digits '1' to '9', where each digit is used at most
# once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].
# 
# 
# Return the lexicographically smallest possible string num that meets the
# conditions.
# 
# 
# Example 1:
# 
# 
# Input: pattern = "IIIDIDDD"
# Output: "123549876"
# Explanation:
# At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
# At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
# Some possible values of num are "245639871", "135749862", and "123849765".
# It can be proven that "123549876" is the smallest possible num that meets the
# conditions.
# Note that "123414321" is not possible because the digit '1' is used more than
# once.
# 
# Example 2:
# 
# 
# Input: pattern = "DDD"
# Output: "4321"
# Explanation:
# Some possible values of num are "9876", "7321", and "8742".
# It can be proven that "4321" is the smallest possible num that meets the
# conditions.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pattern.length <= 8
# pattern consists of only the letters 'I' and 'D'.
# 
# 
#

# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        # Approach 1: Brute Force with permutations 
        # Time Complexity: O(n!)
        # Space Complexity: O(n) 
        # n = len(pattern) 
        # digits = '123456789'[:n + 1]
        # for perm in permutations(digits):
        #     num = ''.join(perm)
        #     valid = True 
        #     for i in range(n):
        #         if pattern[i] == 'I' and num[i] >= num[i+1]:
        #             valid = False
        #             break
        #         if pattern[i] == 'D' and num[i] <= num[i+1]:
        #             valid = False
        #             break
        #     if valid:
        #         return num
        # return ''
        
        # Approach 2: Backtracking 
        # Time Complexity: O(9!)
        # Space Complexity: O(n)
        # n = len(pattern)
        # self.result = None 
        
        # def backtrack(curr, used, pos):
        #     if pos == n + 1:
        #         num = ''.join(curr)
        #         if self.result is None or num < self.result:
        #             self.result = num
        #         return
            
        #     prev = curr[-1] if curr else None 
        #     for d in '123456789':
        #         if d not in used:
        #             if pos == 0 or \
        #                 (pattern[pos - 1] == 'I' and prev < d) or \
        #                 (pattern[pos - 1] == 'D' and prev > d):
        #                 curr.append(d)
        #                 used.add(d)
        #                 backtrack(curr, used, pos + 1)
        #                 curr.pop()
        #                 used.remove(d)
        # backtrack([], set(), 0)
        # return self.result
        # Approach 3: Greedy with Stack 
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        pattern += 'I' # add a dummy 'I' to make sure the last digit is popped 
        stack = []
        result = ""
        num = 1 # start from 1 being the smallest digit, to apply greedy strategy
        
        for c in pattern:
            stack.append(str(num)) # push the number into the stack
            num += 1 # increment the number
            # if we see a 'I', pop all the elements in the stack 
            if c == 'I':
                while stack:
                    result += stack.pop()
        return result
        
        
        
# @lc code=end

