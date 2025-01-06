#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
#
# algorithms
# Medium (86.02%)
# Likes:    2296
# Dislikes: 95
# Total Accepted:    139.3K
# Total Submissions: 161.6K
# Testcase Example:  '"110"'
#
# You have n boxes. You are given a binary string boxes of length n, where
# boxes[i] is '0' if the i^th box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box. Box i
# is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may
# be more than one ball in some boxes.
#
# Return an array answer of size n, where answer[i] is the minimum number of
# operations needed to move all the balls to the i^th box.
#
# Each answer[i] is calculated considering the initial state of the boxes.
#
#
# Example 1:
#
#
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first
# box in one operation.
# 2) Second box: you will have to move one ball from the first box to the
# second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third
# box in two operations, and move one ball from the second box to the third box
# in one operation.
#
#
# Example 2:
#
#
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
#
#
# Constraints:
#
#
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.
#
#
#


# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Approach 1: Brute Force
        # Time Complexity: O(n^2) for the nested loops
        # Space Complexity: O(n) for the answer array
        n = len(boxes)
        answer = [0] * n  # Initialize the answer array with zeros

        # # Iterate through each box as the target
        # for i in range(n):
        #     operations = 0  # Initialize the number of operations needed to move all balls to the target box

        #     # Iterate through all boxes to calculate the operations needed
        #     for j in range(n):
        #         if boxes[j] == "1":
        #             operations += abs(i - j)

        #     answer[i] = operations  # Store the total operations for box i

        # return answer

        # Approach 2: Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Initialize Prefix Sum arrays
        # prefix_counts = [0] * n
        # prefix_positions = [0] * n
        # suffix_counts = [0] * n
        # suffix_positions = [0] * n

        # # Compute prefix_counts and prefix_positions

        # count = 0
        # pos_sum = 0
        # for i in range(n):
        #     if boxes[i] == "1":
        #         count += 1
        #         pos_sum += i
        #     prefix_counts[i] = count
        #     prefix_positions[i] = pos_sum

        # # Compute suffix_counts and suffix_positions
        # count = 0
        # pos_sum = 0
        # for i in range(n - 1, -1, -1):
        #     if boxes[i] == "1":
        #         count += 1
        #         pos_sum += i
        #     suffix_counts[i] = count
        #     suffix_positions[i] = pos_sum

        # # Calculate operations for each box
        # for i in range(n):
        #     # Operations from the left side
        #     if i > 0:
        #         left_count = prefix_counts[i - 1]
        #         left_pos_sum = prefix_positions[i - 1]
        #         left_operations = left_count * i - left_pos_sum
        #     else:
        #         left_operations = 0

        #     # Operations from the right side
        #     if i < n - 1:
        #         right_count = suffix_counts[i + 1]
        #         right_pos_sum = suffix_positions[i + 1]
        #         right_operations = right_pos_sum - right_count * i
        #     else:
        #         right_operations = 0

        #     # Total operations for box i
        #     answer[i] = left_operations + right_operations

        # return answer

        # Approach 3: Optimized Prefix Sum
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Left to Right Pass
        left_count = 0  # Number of '1's to the left of the current box
        left_distance = 0  # Total distance from left '1's to current box
        for i in range(n):
            answer[i] += left_distance  # Add the current left_distance to answer[i]

            if boxes[i] == "1":
                left_count += 1  # Increment left_count if current box has a ball

            left_distance += left_count  # Update left_distance for the next box

        # Right to Left Pass

        right_count = 0  # Number of '1's to the right of the current box
        right_distance = 0  # Total distance from right '1's to current box

        for i in range(n - 1, -1, -1):
            answer[i] += right_distance  # Add the current right_distance to answer[i]

            if boxes[i] == "1":
                right_count += 1  # Increment right_count if current box has a ball

            right_distance += right_count  # Update right_distance for the next box

        return answer


# @lc code=end
