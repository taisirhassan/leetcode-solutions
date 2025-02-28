#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.74%)
# Likes:    18023
# Dislikes: 707
# Total Accepted:    2.6M
# Total Submissions: 4.1M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: Sorting by Frequency
        # Time: O(nlogn)
        # Space: O(n)
        # frequency = Counter(nums)

        # # sort the unique elements by frequency
        # sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        # # return the first k elements from the sorted list
        # return [item[0] for item in sorted_items[:k]]

        # Approach 2: Heap
        # frequency = Counter(nums)

        # # use heapq.nlargest to extract the k largest elements from the heap with highest frequency
        # top_k = heapq.nlargest(k, frequency.keys(), key=lambda x: frequency[x])
        # return top_k

        # Approach 3: Bucket Sort (Most Optimal)
        # Time: O(n)
        # Space: O(n)
        # count the frequency of each element
        frequency = Counter(nums)

        # create buckets where index i holds elements with frequency i
        # the max frequency can be n, so we need n + 1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency.items():
            buckets[freq].append(num)

        # collect the top k frequent elements by iterating from highest frequency to lowest
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                # return the result if we have collected k elements
                if len(result) == k:
                    return result
        return result


# @lc code=end
