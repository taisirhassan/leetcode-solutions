#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (54.79%)
# Likes:    9536
# Dislikes: 662
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
  '[[],[1],[2],[2],[],[1],[2],[]]'
#
# Implement the RandomizedSet class:
# 
# 
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns
# true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns
# true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is
# called). Each element must have the same probability of being returned.
# 
# 
# You must implement the functions of the class such that each function works
# in average O(1) time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# 
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was
# inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now
# contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2
# randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now
# contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set,
# getRandom() will always return 2.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= val <= 2^31 - 1
# At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is
# called.
# 
# 
#

# @lc code=start
class RandomizedSet:
  # Approach 1: Using a set with List Conversion
  
  # Approach 2: Using a dictionary 
  

    def __init__(self):
      # # using a set to store the values 
      # self.values = set()
      # using a dictionary to store the values and their indices
      self.nums = []
      # dictionary to map values to its index in the list
      self.val_to_index = {}
        
    def insert(self, val: int) -> bool:
      # # if the value already exists, return False
      # if val in self.values:
      #   return False
      # # add the value to the set
      # self.values.add(val)
      # return True
      
      # # if already present, return False
      # if val in self.dict_only:
      #   return False
      
      # # insert the value into the dictionary with a dummy value 
      # self.dict_only[val] = True 
      # return True 
      
      # Approach 3: List + Dictionary 
      # list to store the elements for random access
      
      # check if val already exists in the dictionary
      if val in self.val_to_index:
        return False
      # add the value to the list and dictionary
      self.nums.append(val)
      # store the index of the value in the dictionary
      self.val_to_index[val] = len(self.nums) - 1
      return True
    
        

    def remove(self, val: int) -> bool:
      # # if the value doesn't exist, return false
      # if val not in self.values:
      #   return False
      # # remove the value from the set
      # self.values.remove(val)
      # return True
      
      # if the value doesn't exist, return False
      # if val not in self.dict_only:
      #   return False
      # # remove the value from the dictionary
      # del self.dict_only[val]
      # return True
      
      # check if val exists, if not return false
      if val not in self.val_to_index:
        return False
      
      # index of the element to remove
      idx_to_remove = self.val_to_index[val]
      # get the last element in the list
      last_element = self.nums[-1]
      
      # overwrite the element to remove with the last element
      self.nums[idx_to_remove] = last_element
      # update the index of the last element in the dictionary
      self.val_to_index[last_element] = idx_to_remove
      # remove the last element from the list
      self.nums.pop()
      # remove the element from the dictionary
      del self.val_to_index[val]
      return True
        

    def getRandom(self) -> int:
      # # convert the set to a list to select a random element
      # return random.choice(list(self.values))
      
      # convert the dictionary keys to a list to select a random element
      # return random.choice(list(self.dict_only.keys()))
      
      # return a random element from the list
      return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

