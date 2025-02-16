#
# @lc app=leetcode id=1718 lang=python3
#
# [1718] Construct the Lexicographically Largest Valid Sequence
#
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/
#
# algorithms
# Medium (54.55%)
# Likes:    1032
# Dislikes: 163
# Total Accepted:    93.7K
# Total Submissions: 127.1K
# Testcase Example:  '3'
#
# Given an integer n, find a sequence that satisfies all of the
# following:
#
#
# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences
# of i is exactly i.
#
#
# The distance between two numbers on the sequence, a[i] and a[j], is the
# absolute difference of their indices, |j - i|.
#
# Return the lexicographically largest sequence. It is guaranteed that under
# the given constraints, there is always a solution.
#
# A sequence a is lexicographically larger than a sequence b (of the same
# length) if in the first position where a and b differ, sequence a has a
# number greater than the corresponding number in b. For example, [0,1,9,0] is
# lexicographically larger than [0,1,5,6] because the first position they
# differ is at the third number, and 9 is greater than 5.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: [3,1,2,3,2]
# Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the
# lexicographically largest valid sequence.
#
#
# Example 2:
#
#
# Input: n = 5
# Output: [5,3,1,4,3,5,2,4,2]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#


# @lc code=start
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Approach 1: Backtracking
        # Time Complexity: O((2n-1)!)
        # Space Complexity: O(2n-1)

        # the length of the result array is 2*n - 1, since we have n numbers and each number has 2 positions except 1.
        size = 2 * n - 1

        # init the result list
        res = [0] * size

        # used[i] is True if we have already placed number i in the sequence.
        # Index 0 is unused, so our numbers go from 1 to n.
        used = [False] * (n + 1)

        def backtrack(pos: int) -> bool:
            # Base Case: If we've reached the end, the sequence is complete.
            if pos == size:
                return True

            # Recursive Case: Try to place the next number.

            # if current position is already filled, move to the next index.
            if res[pos] != 0:
                return backtrack(pos + 1)

            # try placing numbers from n down to 1 (for lexicographical largeness) kinda greedy approach.
            for num in range(n, 0, -1):
                # skip if number is already used.
                if used[num]:
                    continue

                # special case: for number 1, we only place it at the current position.
                if num == 1:
                    res[pos] = 1
                    used[1] = True
                    # continue backtracking for the next positions.
                    if backtrack(pos + 1):
                        return True
                    # backtrack: unmark and reset the position.
                    res[pos] = 0
                    used[1] = False
                else:
                    # for numbers greater than 1, we need to ensure that pos + num is within bounds
                    # and that the target position is empty.
                    if pos + num >= size or res[pos + num] != 0:
                        continue
                    # place the number at both required positions.
                    res[pos] = num
                    res[pos + num] = num
                    used[num] = True
                    # continue to fill the next available position.
                    if backtrack(pos + 1):
                        return True
                    # Backtrack: remove the number placements.
                    res[pos] = 0
                    res[pos + num] = 0
                    used[num] = False

            # If no number can be placed at pos, return False to backtrack.
            return False

        # Start backtracking from position 0.
        backtrack(0)
        return res


# @lc code=end
