#
# @lc app=leetcode id=3362 lang=python3
#
# [3362] Zero Array Transformation III
#

# @lc code=start
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Approach 1: Brute Force 
        # Time Complexity: O(2^m * n)
        # Space Complexity: O(n + m^2)
        # n, m = len(nums), len(queries)
        # best_keep = m + 1 # smallest # queries we need to keep
       
        # # precompute for each query its range
        # ranges = [list(range(l, r + 1)) for l, r in queries]
       
        # # try every possible keep-size k = 0..m
        # for keep_size in range(m + 1):
        #    # all ways to pick keep_size queries
        #     for keep_idxs in combinations(range(m), keep_size):
        #        # build coverage counts
        #         coverage = [0] * n
        #         for qi in keep_idxs:
        #             for i in ranges[qi]:
        #                 coverage[i] += 1
                
        #         # check feasibility
        #         ok = True 
        #         for i in range(n):
        #             if coverage[i] < nums[i]:
        #                 ok = False 
        #                 break
                
        #         if ok:
        #             best_keep = keep_size
        #             break
        #     if best_keep == keep_size:
        #         break
        
        # if best_keep > m:
        #     return -1
        # return m - best_keep
        
        # Approach 2: Greedy with Priority Queue
        # Time Complexity: O((n + m) log m)
        # Space Complexity: O(n + m)
        n, m = len(nums), len(queries)
        # 1) Build cov & cap
        cov = [0]*(n+1)
        for l, r in queries:
            cov[l] += 1
            cov[r+1] -= 1
        for i in range(1, n):
            cov[i] += cov[i-1]
        cov = cov[:n]
        cap = [cov[i] - nums[i] for i in range(n)]
        if any(c < 0 for c in cap):
            return -1

        # 2) Prepare queries by start
        by_start = [[] for _ in range(n)]
        expire = [[] for _ in range(n+1)]
        for idx, (l, r) in enumerate(queries):
            by_start[l].append((r, idx))
            expire[r+1].append(idx)

        # 3) Sweep
        heap = []                    # max-heap of (-r, idx) for active removals
        active = 0                   # #currently active candidate removals
        dropped = 0                  # #queries we drop (i.e. keep)
        is_dropped = [False]*m
        is_expired = [False]*m

        for i in range(n):
            # Expire those ending before i
            for idx in expire[i]:
                if not is_dropped[idx]:
                    active -= 1
                is_expired[idx] = True

            # Add new queries starting at i
            for r, idx in by_start[i]:
                heapq.heappush(heap, (-r, idx))
                active += 1

            # If too many cover i, drop the worst (largest r)
            while active > cap[i]:
                # pop until we find a live candidate
                while heap:
                    negr, idx = heapq.heappop(heap)
                    if not is_dropped[idx] and not is_expired[idx]:
                        break
                is_dropped[idx] = True
                dropped += 1
                active -= 1

        return m - dropped

        
# @lc code=end

