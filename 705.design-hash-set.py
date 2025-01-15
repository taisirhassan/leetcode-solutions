#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (67.20%)
# Likes:    3841
# Dislikes: 315
# Total Accepted:    461.7K
# Total Submissions: 686.8K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
# 
# Implement MyHashSet class:
# 
# 
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or
# not.
# void remove(key) Removes the value key in the HashSet. If key does not exist
# in the HashSet, do nothing.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
# 
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
# 
# 
# Constraints:
# 
# 
# 0 <= key <= 10^6
# At most 10^4 calls will be made to add, remove, and contains.
# 
# 
#

# @lc code=start
  # Approach 1: Using Brute force
  # Time complexity: O(n) for all operations add, remove, contains where n is the number of elements in the hashset 
  # Space complexity: O(n) where n is the number of elements in the hashset

    # def __init__(self):
    #   self.data = [] # List of keys in the hashset
        

    # def add(self, key: int) -> None:
    #   if key not in self.data:
    #     self.data.append(key)
        

    # def remove(self, key: int) -> None:
    #   if key in self.data:
    #     self.data.remove(key)
        

    # def contains(self, key: int) -> bool:
    #   return key in self.data
    
    # Approach 2: Using a boolean array
    # Time complexity: O(1) for all operations add, remove, contains
    # Space Complexity: O(1000000) (or O(1) relative to the fixed key range).
    
    # def __init__(self):
    #   self.data = [False] * 1000001
      
    # def add(self, key: int) -> None:
    #   self.data[key] = True
      
    # def remove(self, key: int) -> None:
    #   self.data[key] = False
      
    # def contains(self, key: int) -> bool:
    #   return self.data[key]
    
    # Approach 3: Linked List with separate chaining
    # Time complexity: O(1) for all operations add, remove, contains
    # Space Complexity: O(n) where n is the number of elements in the hashset      
    
class MyHashSet:
  def __init__(self):
    self.bucket_count = 1000  # Number of buckets chosen based on the key range [0, 10^6]
    self.buckets = [[] for _ in range(self.bucket_count)]  # Create an array of empty buckets (lists)

  def _hash(self, key: int) -> int:
    return key % self.bucket_count  # Compute the bucket index using modulo operation

  def add(self, key: int) -> None:
    hash_index = self._hash(key)  # Get the appropriate bucket index for this key
    bucket = self.buckets[hash_index]  # Retrieve the bucket (list) at the computed index
    if key not in bucket:  # Only add the key if it's not already present in the bucket
      bucket.append(key)

  def remove(self, key: int) -> None:
    hash_index = self._hash(key)  # Compute the bucket index for the key
    bucket = self.buckets[hash_index]  # Retrieve the bucket corresponding to the key
    try:
      bucket.remove(key)  # Attempt to remove the key from the bucket
    except ValueError:
      pass  # If the key is not found in the bucket, do nothing

  def contains(self, key: int) -> bool:
    hash_index = self._hash(key)  # Compute the bucket index for the key
    return key in self.buckets[hash_index]  # Check if the key is present in the bucket



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

