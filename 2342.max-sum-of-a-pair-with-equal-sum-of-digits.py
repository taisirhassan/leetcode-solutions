#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
#
# algorithms
# Medium (55.69%)
# Likes:    733
# Dislikes: 22
# Total Accepted:    56.1K
# Total Submissions: 100K
# Testcase Example:  '[18,43,36,13,7]'
#
# You are given a 0-indexed array nums consisting of positive integers. You can
# choose two indices i and j, such that i != j, and the sum of digits of the
# number nums[i] is equal to that of nums[j].
#
# Return the maximum value of nums[i] + nums[j] that you can obtain over all
# possible indices i and j that satisfy the conditions.
#
#
# Example 1:
#
#
# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 +
# 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 +
# 7 = 50.
# So the maximum sum that we can obtain is 54.
#
#
# Example 2:
#
#
# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we
# return -1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
#
#
#


# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Approach 1: Brute Force
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # Helper function to calculate the sum of digits of a number.
        # def sum_digits(n: int) -> int:
        #     total = 0
        #     while n:
        #         total += n % 10  # Add the last digit to total.
        #         n //= 10  # Remove the last digit.
        #     return total

        # max_sum = (
        #     -1
        # )  # Initialize the maximum sum to -1 (default if no valid pair is found).
        # n = len(nums)

        # # Iterate over all unique pairs (i, j) where i < j.
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         # Check if the sum of digits for nums[i] and nums[j] are equal.
        #         if sum_digits(nums[i]) == sum_digits(nums[j]):
        #             # Update max_sum if this pair's sum is larger.
        #             max_sum = max(max_sum, nums[i] + nums[j])

        # return max_sum

        # Approach 2: Hash Map
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Helper function to calculate the sum of digits of a number
        # def sum_digits(n: int) -> int:
        #     total = 0
        #     while n:
        #         total += n % 10  # add the last digit
        #         n //= 10  # remove the last digit
        #     return total

        # # Dictionary to store the two largest numbers for each sum-of-digits value.
        # # Key: digit sum, Value: list [max1, max2]
        # digit_sum_dict = {}

        # # Iterate over each number in nums
        # for num in nums:
        #     # Calculate the sum of digits of the current number
        #     s = sum_digits(num)

        #     # If this digit sum is not in the dictionary, initialize it.
        #     if s not in digit_sum_dict:
        #         digit_sum_dict[s] = [num, None]  # [largest, second largest]
        #     else:
        #         # Retrieve the current pair for this digit sum
        #         max1, max2 = digit_sum_dict[s]
        #         # If the current number is greater than the largest number seen so far
        #         if num > max1:
        #             # Update pair: current largest becomes second largest
        #             digit_sum_dict[s] = [num, max1]
        #         # Else if it is not greater than the largest but greater than second largest
        #         elif max2 is None or num > max2:
        #             digit_sum_dict[s][1] = num

        # # Now, check each group to find the maximum valid sum (where a valid pair exists)
        # max_sum = -1  # default answer if no valid pair is found
        # for pair in digit_sum_dict.values():
        #     if (
        #         pair[1] is not None
        #     ):  # Ensure that a pair exists (i.e., second largest is available)
        #         current_sum = pair[0] + pair[1]
        #         max_sum = max(max_sum, current_sum)

        # return max_sum

        # Approach 3: Group by Sum of Digits
        # Time complexity: O(n log n)
        # Space complexity: O(n)
        def sum_digits(n: int) -> int:
            # Helper function to calculate sum of digits
            return sum(int(d) for d in str(n))

        # Dictionary to group numbers by their sum of digits
        groups = {}
        for num in nums:
            s = sum_digits(num)
            if s not in groups:
                groups[s] = []
            groups[s].append(num)

        max_sum = -1  # default if no valid pair is found
        # For each group, if there are at least two numbers, sort and pick top two.
        for s, values in groups.items():
            if len(values) >= 2:
                values.sort(reverse=True)
                current_sum = values[0] + values[1]
                max_sum = max(max_sum, current_sum)

        return max_sum


# @lc code=end
