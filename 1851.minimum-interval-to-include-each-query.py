#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#
# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
#
# algorithms
# Hard (51.21%)
# Likes:    1035
# Dislikes: 40
# Total Accepted:    47K
# Total Submissions: 91.3K
# Testcase Example:  '[[1,4],[2,4],[3,6],[4,4]]\n[2,3,4,5]'
#
# You are given a 2D integer array intervals, where intervals[i] = [lefti,
# righti] describes the i^th interval starting at lefti and ending at righti
# (inclusive). The size of an interval is defined as the number of integers it
# contains, or more formally righti - lefti + 1.
#
# You are also given an integer array queries. The answer to the j^th query is
# the size of the smallest interval i such that lefti <= queries[j] <= righti.
# If no such interval exists, the answer is -1.
#
# Return an array containing the answers to the queries.
#
#
# Example 1:
#
#
# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,4] is the smallest interval containing 2. The
# answer is 4 - 2 + 1 = 3.
# - Query = 3: The interval [2,4] is the smallest interval containing 3. The
# answer is 4 - 2 + 1 = 3.
# - Query = 4: The interval [4,4] is the smallest interval containing 4. The
# answer is 4 - 4 + 1 = 1.
# - Query = 5: The interval [3,6] is the smallest interval containing 5. The
# answer is 6 - 3 + 1 = 4.
#
#
# Example 2:
#
#
# Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
# Output: [2,-1,4,6]
# Explanation: The queries are processed as follows:
# - Query = 2: The interval [2,3] is the smallest interval containing 2. The
# answer is 3 - 2 + 1 = 2.
# - Query = 19: None of the intervals contain 19. The answer is -1.
# - Query = 5: The interval [2,5] is the smallest interval containing 5. The
# answer is 5 - 2 + 1 = 4.
# - Query = 22: The interval [20,25] is the smallest interval containing 22.
# The answer is 25 - 20 + 1 = 6.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^5
# 1 <= queries.length <= 10^5
# intervals[i].length == 2
# 1 <= lefti <= righti <= 10^7
# 1 <= queries[j] <= 10^7
#
#
#


# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Approach 1: Brute Force
        # Time Complexity: O(n * q)
        # Space Complexity: O(q)
        # res = []
        # # For each query, check every interval.
        # for q in queries:
        #     min_size = float("inf")
        #     for start, end in intervals:
        #         # Check if the query is within the interval.
        #         if start <= q <= end:
        #             size = end - start + 1
        #             min_size = min(min_size, size)
        #     # Append the result: if no interval found, use -1.
        #     res.append(min_size if min_size != float("inf") else -1)
        # return res

        # Approach 2: Sort + Priority Queue
        # Time Complexity: O(nlogn + qlogq)
        # Space Complexity: O(n + q)
        # Sort intervals by start time.
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        # Pair each query with its original index, then sort by query value.
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        # Result array, initialized with -1.
        res = [-1] * len(queries)

        # Min-heap will store tuples of (interval_size, end, start).
        min_heap = []
        j = 0  # Pointer for intervals

        # Process queries in sorted order.
        for q, qi in sorted_queries:
            # Add intervals whose start is <= current query.
            while j < n and intervals[j][0] <= q:
                start, end = intervals[j]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end, start))
                j += 1

            # Remove intervals from the heap that do not cover the query.
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # If heap is not empty, the top has the smallest interval covering q.
            if min_heap:
                res[qi] = min_heap[0][0]

        return res


# @lc code=end
