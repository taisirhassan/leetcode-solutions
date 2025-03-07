#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#
# https://leetcode.com/problems/design-a-number-container-system/description/
#
# algorithms
# Medium (44.78%)
# Likes:    818
# Dislikes: 61
# Total Accepted:    107.6K
# Total Submissions: 188.7K
# Testcase Example:  '["NumberContainers","find","change","change","change","change","find","change","find"]\n' +
  '[[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]'
#
# Design a number container system that can do the following:
# 
# 
# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# 
# 
# Implement the NumberContainers class:
# 
# 
# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the
# number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1
# if there is no index that is filled by number in the system.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["NumberContainers", "find", "change", "change", "change", "change", "find",
# "change", "find"]
# [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
# Output
# [null, -1, null, null, null, null, 1, null, 2]
# 
# Explanation
# NumberContainers nc = new NumberContainers();
# nc.find(10); // There is no index that is filled with number 10. Therefore,
# we return -1.
# nc.change(2, 10); // Your container at index 2 will be filled with number 10.
# nc.change(1, 10); // Your container at index 1 will be filled with number 10.
# nc.change(3, 10); // Your container at index 3 will be filled with number 10.
# nc.change(5, 10); // Your container at index 5 will be filled with number 10.
# nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the
# smallest index that is filled with 10 is 1, we return 1.
# nc.change(1, 20); // Your container at index 1 will be filled with number 20.
# Note that index 1 was filled with 10 and then replaced with 20. 
# nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index
# that is filled with 10 is 2. Therefore, we return 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= index, number <= 10^9
# At most 10^5 calls will be made in total to change and find.
# 
# 
#

# @lc code=start
class NumberContainers:
  
  # Approach 1: Simple Dictionary with Linear Search
  # Time complexity: O(n)
  # Space complexity: O(n)

    def __init__(self):
      self.index_to_number = {} # dictionary to store index and number
      self.num_to_indices = {} # dictionary to map a number to a min-heap of indices that contain this number
        

    def change(self, index: int, number: int) -> None:
       # if the index already had a number, we don't immediately remove it from its old heap
        # (lazy deletion will handle it during the find operation).
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            # No need to remove from heap immediately; lazy deletion will check correctness later.
        
        # update the mapping of the index to the new number.
        self.index_to_number[index] = number
        
        # if this number is not present in the dictionary, initialize a new heap for it.
        if number not in self.num_to_indices:
            self.num_to_indices[number] = []
        # push the index to the heap of the number. 
        heapq.heappush(self.num_to_indices[number], index)
        

    def find(self, number: int) -> int:
      # indices = [idx for idx, num in self.index_to_number.items() if num == number] # indices of number in the dictionary 
      # return min(indices) if indices else -1
      
      # if the number is not present in the dictionary, return -1.
        if number not in self.num_to_indices:
            return -1
       
       # retrieve the heap for the given number.
        heap = self.num_to_indices[number]
        
        # remove the old indices from the heap. 
        while heap and self.index_to_number.get(heap[0], None) != number:
            heapq.heappop(heap)
            
         # If the heap becomes empty, no valid index exists.
        if not heap:
            return -1
        
        # The smallest valid index is at the top of the heap.
        return heap[0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

