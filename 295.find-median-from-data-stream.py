#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (52.68%)
# Likes:    12315
# Dislikes: 260
# Total Accepted:    928.4K
# Total Submissions: 1.8M
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value, and the median is the mean of the two
# middle values.
# 
# 
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# 
# 
# Implement the MedianFinder class:
# 
# 
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10^-5 of the actual answer will be accepted.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 
# 
# 
# Constraints:
# 
# 
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling
# findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are in the range [0, 100], how would
# you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how
# would you optimize your solution?
# 
# 
#

# @lc code=start
class MedianFinder:
  # Approach 1: Sorting Brute Force 

    def __init__(self):
      # self.data = []
      
      self.small = [] # Max heap
      self.large = [] # Min heap 
        

    def addNum(self, num: int) -> None:
      # self.data.append(num)
      # Step 1: Push the new number onto the max-heap.
        heapq.heappush(self.small, -num)
        
        # Step 2: Move the largest element from self.small to self.large.
        #         Since self.small is a max-heap (stored as negatives),
        #         popping gives us the largest element (as negative).
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 3: Maintain the size property: if large has more elements,
        #         move one element back to small.
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
      # self.data.sort() 
      # n = len(self.data)
      # return ( self.data[n//2] if (n & 1) else (self.data[n//2 - 1] + self.data[n//2]) / 2 )
      if len(self.small) > len(self.large):
        # Odd number of elements: median is the top of the max-heap.
        return -self.small[0]
      else:
          # Even number of elements: median is the average of the two middle values.
          return (-self.small[0] + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

