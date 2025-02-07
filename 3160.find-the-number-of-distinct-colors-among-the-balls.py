#
# @lc app=leetcode id=3160 lang=python3
#
# [3160] Find the Number of Distinct Colors Among the Balls
#
# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
#
# algorithms
# Medium (41.02%)
# Likes:    542
# Dislikes: 59
# Total Accepted:    108.4K
# Total Submissions: 208.4K
# Testcase Example:  '4\n[[1,4],[2,5],[1,3],[3,4]]'
#
# You are given an integer limit and a 2D array queries of size n x 2.
#
# There are limit + 1 balls with distinct labels in the range [0, limit].
# Initially, all balls are uncolored. For every query in queries that is of the
# form [x, y], you mark ball x with the color y. After each query, you need to
# find the number of distinct colors among the balls.
#
# Return an array result of length n, where result[i] denotes the number of
# distinct colors after i^th query.
#
# Note that when answering a query, lack of a color will not be considered as a
# color.
#
#
# Example 1:
#
#
# Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
#
# Output: [1,2,2,3]
#
# Explanation:
#
#
#
#
# After query 0, ball 1 has color 4.
# After query 1, ball 1 has color 4, and ball 2 has color 5.
# After query 2, ball 1 has color 3, and ball 2 has color 5.
# After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color
# 4.
#
#
#
# Example 2:
#
#
# Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
#
# Output: [1,2,2,3,4]
#
# Explanation:
#
#
#
#
# After query 0, ball 0 has color 1.
# After query 1, ball 0 has color 1, and ball 1 has color 2.
# After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
# After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has
# color 4.
# After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has
# color 4, and ball 4 has color 5.
#
#
#
#
# Constraints:
#
#
# 1 <= limit <= 10^9
# 1 <= n == queries.length <= 10^5
# queries[i].length == 2
# 0 <= queries[i][0] <= limit
# 1 <= queries[i][1] <= 10^9
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        # Approach 1: Brute force with set
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        # Create an array representing each ball, initially all uncolored (None).
        # The array has size (limit + 1) because balls are labeled from 0 to limit.
        balls = [None] * (limit + 1)

        # This will hold the result after processing each query.
        result = []

        # Process each query one by one.
        for x, y in queries:
            # Update the color of ball x to y.
            balls[x] = y

            # Create a set to track distinct colors.
            # We will iterate over every ball in the balls array.
            distinct_colors = set()
            for color in balls:
                # Only add colored balls (i.e., ignore those that are None).
                if color is not None:
                    distinct_colors.add(color)

            # The number of distinct colors is the size of the set.
            result.append(len(distinct_colors))

        return result
        # Approach 2: Two dictionaries
        # Time complexity: O(n)
        # Space complexity: O(n)

        # # Dictionary mapping ball number to its current color.
        # ball_to_color = {}
        # # Dictionary mapping color to the count of balls painted with that color.
        # color_freq = {}
        # # List to store the number of distinct colors after each query.
        # result = []

        # # Process each query in the list of queries.
        # for x, y in queries:
        #     # Check if ball x has been colored before.
        #     if x in ball_to_color:
        #         # Retrieve the old color of ball x.
        #         old_color = ball_to_color[x]
        #         # Decrement the frequency for this old color.
        #         color_freq[old_color] -= 1
        #         # If no ball now has the old color, remove it from the frequency dictionary.
        #         if color_freq[old_color] == 0:
        #             del color_freq[old_color]

        #     # Update ball x's color to the new color y.
        #     ball_to_color[x] = y
        #     # Increment the frequency for the new color y.
        #     # If the color is not yet present, add it with a count of 1.
        #     if y in color_freq:
        #         color_freq[y] += 1
        #     else:
        #         color_freq[y] = 1

        #     # The current distinct color count is the number of keys in color_freq.
        #     result.append(len(color_freq))

        # return result


# @lc code=end
