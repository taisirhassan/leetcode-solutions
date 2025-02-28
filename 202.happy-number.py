#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (57.22%)
# Likes:    10921
# Dislikes: 1545
# Total Accepted:    1.8M
# Total Submissions: 3.1M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # # Approach 1: Hash Set
        # # Time complexity: O(logn)
        # # Space complexity: O(logn)
        # def get_next(number: int) -> int:
        #     total_sum = 0
        #     while number:
        #         digit = number % 10
        #         total_sum += digit * digit
        #         number //= 10
        #     return total_sum

        # seen = set()  # set to store the seen numbers
        # while n != 1 and n not in seen:
        #     seen.add(n)  # add n to the set
        #     n = get_next(n)  # get the next number

        # return n == 1  # if n is 1 then it is a happy number

        # Approach 2: Recursive Approach
        # Time complexity: O(logn)
        # Space complexity: O(logn)
        # def helper(number: int, seen: set) -> bool:
        #     # base condition: if the number is 1 then it is a happy number
        #     if number == 1:
        #         return True
        #     # if the number is already seen then it is not a happy number
        #     if number in seen:
        #         return False
        #     seen.add(number)  # add the number to the seen set

        #     # calculate the sum of the squares of the digits
        #     next_number = sum(int(digit) ** 2 for digit in str(number))
        #     # recursively call the helper function
        #     return helper(next_number, seen)

        # # start with the number n and an empty set
        # return helper(n, set())

        # Approach 3: Floyd's Cycle Detection Algorithm (Fast and Slow Pointers)
        # Time complexity: O(logn)
        # Space complexity: O(1)
        def get_next(number: int) -> int:
            total_sum = 0
            while number:
                digit = number % 10
                total_sum += digit * digit
                number //= 10
            return total_sum

        slow = n  # slow pointer starts at n
        fast = get_next(
            n
        )  # fast pointer starts at the next number, and moves one step ahead initially

        # loop until the fast and slow pointers meet or either of them reaches 1
        while fast != 1 and slow != fast:
            slow = get_next(slow)  # move the slow pointer one step ahead
            fast = get_next(get_next(fast))  # move the fast pointer two steps ahead

        return fast == 1  # if fast pointer reaches 1, then n is a happy number


# @lc code=end
