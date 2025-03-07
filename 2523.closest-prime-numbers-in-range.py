#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#
# https://leetcode.com/problems/closest-prime-numbers-in-range/description/
#
# algorithms
# Medium (38.89%)
# Likes:    777
# Dislikes: 59
# Total Accepted:    133K
# Total Submissions: 262.6K
# Testcase Example:  '10\n19'
#
# Given two positive integers left and right, find the two integers num1 and
# num2 such that:
#
#
# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above
# conditions.
#
#
# Return the positive integer array ans = [num1, num2]. If there are multiple
# pairs satisfying these conditions, return the one with the smallest num1
# value. If no such numbers exist, return [-1, -1].
#
#
# Example 1:
#
#
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or
# [17,19].
# Since 11 is smaller than 17, we return the first pair.
#
#
# Example 2:
#
#
# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the
# conditions cannot be satisfied.
#
#
#
# Constraints:
#
#
# 1 <= left <= right <= 10^6
#
#
#
# .spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px
# 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan;
# outline:0;
# }
# .spoiler {overflow:hidden;}
# .spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s
# ease;-o-transition: all 0s ease;transition: margin 0s ease;}
# .spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
# .spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
#
#
#


# @lc code=start
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Approach 1: Brute Force Approach
        # Time Complexity: O(n^2 sqrt(n))
        # Space Complexity: O(1)
        # def is_prime(n):
        #     if n < 2:
        #         return False
        #     # check if n is divisible by any number from 2 to sqrt(n)
        #     for i in range(2, int(sqrt(n)) + 1):
        #         # if n is divisible by i, then n is not a prime number
        #         if n % i == 0:
        #             return False
        #     return True

        # best_gap = float("inf")
        # ans = [-1, -1]

        # # check all pairs of numbers between left and right
        # for i in range(left, right):
        #     if not is_prime(i):
        #         continue  # skip if i is not a prime number
        #     for j in range(i + 1, right + 1):
        #         if not is_prime(j):
        #             continue  # skip if j is not a prime number
        #         diff = j - i
        #         if diff < best_gap:
        #             best_gap = diff
        #             ans = [i, j]
        #             # if the gap is 2, then we can't find a better pair, break early
        #             if best_gap == 2:
        #                 return ans
        # return ans

        # Approach 2: Prime List Approach
        # Time Complexity: O(n sqrt(n))
        # Space Complexity: O(n)
        # def is_prime(n):
        #     if n < 2:
        #         return False
        #     # check if n is divisible by any number from 2 to sqrt(n)
        #     for i in range(2, int(sqrt(n)) + 1):
        #         # if n is divisible by i, then n is not a prime number
        #         if n % i == 0:
        #             return False
        #     return True

        # # collect all prime numbers between left and right
        # primes = [num for num in range(left, right + 1) if is_prime(num)]

        # # if less than 2 prime numbers are found, return [-1, -1]
        # if len(primes) < 2:
        #     return [-1, -1]

        # best_gap = float("inf")
        # ans = [-1, -1]
        # # find the adjacent prime numbers with the smallest gap
        # for i in range(len(primes) - 1):
        #     diff = primes[i + 1] - primes[i]
        #     if diff < best_gap:
        #         best_gap = diff
        #         ans = [primes[i], primes[i + 1]]
        # return ans

        # Approach 3: Sieve of Eratosthenes
        # Time Complexity: O(n log(log(n)))
        # Space Complexity: O(n)

        # create a boolean list for sieve where index i indicates if i is prime, we initialize all entries as True except 0 and 1.
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes.

        # use the Sieve of Eratosthenes to mark non-prime numbers.
        # we iterate from 2 up to sqrt(right)
        for i in range(2, int(sqrt(right)) + 1):
            if sieve[i]:
                # mark multiples of i as not prime.
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

        # collect the prime numbers in the range [left, right]
        primes = []
        for i in range(left, right + 1):
            if sieve[i]:
                primes.append(i)

        # if there are less than 2 primes, return [-1,-1] as no valid pair exists.
        if len(primes) < 2:
            return [-1, -1]

        # Initialize the answer with default values and a large gap.
        best_gap = float("inf")
        ans = [-1, -1]

        # Iterate through consecutive primes and check their difference.
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < best_gap:
                best_gap = diff
                ans = [primes[i], primes[i + 1]]

        return ans


# @lc code=end
