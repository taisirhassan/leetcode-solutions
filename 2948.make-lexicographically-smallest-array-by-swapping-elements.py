#
# @lc app=leetcode id=2948 lang=python3
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
#
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/
#
# algorithms
# Medium (39.09%)
# Likes:    857
# Dislikes: 65
# Total Accepted:    88K
# Total Submissions: 146.1K
# Testcase Example:  '[1,5,3,9,8]\n2'
#
# You are given a 0-indexed array of positive integers nums and a positive
# integer limit.
#
# In one operation, you can choose any two indices i and j and swap nums[i] and
# nums[j] if |nums[i] - nums[j]| <= limit.
#
# Return the lexicographically smallest array that can be obtained by
# performing the operation any number of times.
#
# An array a is lexicographically smaller than an array b if in the first
# position where a and b differ, array a has an element that is less than the
# corresponding element in b. For example, the array [2,10,3] is
# lexicographically smaller than the array [10,2,3] because they differ at
# index 0 and 2 < 10.
#
#
# Example 1:
#
#
# Input: nums = [1,5,3,9,8], limit = 2
# Output: [1,3,5,8,9]
# Explanation: Apply the operation 2 times:
# - Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
# - Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
# We cannot obtain a lexicographically smaller array by applying any more
# operations.
# Note that it may be possible to get the same result by doing different
# operations.
#
#
# Example 2:
#
#
# Input: nums = [1,7,6,18,2,1], limit = 3
# Output: [1,6,7,18,1,2]
# Explanation: Apply the operation 3 times:
# - Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
# - Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
# - Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
# We cannot obtain a lexicographically smaller array by applying any more
# operations.
#
#
# Example 3:
#
#
# Input: nums = [1,7,28,19,10], limit = 3
# Output: [1,7,28,19,10]
# Explanation: [1,7,28,19,10] is the lexicographically smallest array we can
# obtain because we cannot apply the operation on any two indices.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= limit <= 10^9
#
#
#


# @lc code=start
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Approach 1: Union Find
        n = len(nums)

        # 1) Build pairs of (value, index) and sort them by value
        pairs = [(nums[i], i) for i in range(n)]
        pairs.sort(key=lambda x: x[0])  # sort by the value

        # 2) Union-Find Initialization
        parent = list(range(n))  # parent[i] is the parent of i
        size = [1] * n  # size[i] is the size of the set that i belongs to

        # 3) Union-Find Operations
        def find(x):
            if parent[x] != x:  # if x is not the root of the set that x belongs to
                parent[x] = find(
                    parent[x]
                )  # path compression by pointing x's parent to the root of the set
            return parent[x]  # return the root of the set that x belongs to

        def union(a, b):
            rootA, rootB = find(a), find(b)
            if rootA != rootB:
                if size[rootA] < size[rootB]:
                    rootA, rootB = rootB, rootA
                parent[rootB] = rootA
                size[rootA] += size[rootB]

        # 3) Union neighbors in the sorted list if difference <= limit
        for i in range(n - 1):
            val1, idx1 = pairs[i]
            val2, idx2 = pairs[i + 1]
            if abs(val1 - val2) <= limit:
                union(idx1, idx2)

        # 4) Group indices by their Union-Find representative
        comp_map = defaultdict(list)

        for i in range(n):
            comp_map[find(i)].append(
                i
            )  # find the root of the set that i belongs to and append i to the list of indices of the set

        # 5) For each component, sort values and indices, then place

        result = [0] * n
        for rep, indices in comp_map.items():
            # gather values
            vals = [nums[i] for i in indices]
            # sort indices and values
            indices.sort()
            vals.sort()
            # place sorted values into sorted positions
            for i, v in zip(indices, vals):
                result[i] = v

        return result


# @lc code=end
