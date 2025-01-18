#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Medium (55.49%)
# Likes:    14664
# Dislikes: 914
# Total Accepted:    2M
# Total Submissions: 3.6M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# Implement the MinStack class:
# 
# 
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# 
# 
# You must implement a solution with O(1) time complexity for each function.
# 
# 
# Example 1:
# 
# 
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= val <= 2^31 - 1
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
# 
# 
#

# @lc code=start
class MinStack:

    # Approach 1: Brute Force Approach

    # def __init__(self):

    #     self.stack = []  # The main stack to store values.

    # def push(self, val: int) -> None:

    #     self.stack.append(val)  # Simply add the new value to the end of the list.

    # def pop(self) -> None:
    #     # Remove the last element from the stack.
    #     if self.stack:
    #         self.stack.pop()

    # def top(self) -> int:
    #     # Return the last element in the stack.
    #     if self.stack:
    #         return self.stack[-1]

    # def getMin(self) -> int:
    #     # Time Complexity: O(n) using brute force approach
    #     if self.stack:
    #         current_min = self.stack[0]

    #         # Compute the minimum by scanning every element in the stack.
    #         for num in self.stack:
    #             if num < current_min:
    #                 current_min = num
    #         return current_min

    # Approach 2: Utilizing 2 stacks, one for minimum and one normal stack
    def __init__(self):

        self.stack = []  # The main stack to store values.
        self.min_stack = []  # Stack to hold the minimum values at each point

    def push(self, val: int) -> None:
        self.stack.append(val)  # Simply add the new value to the end of the list.
        # If the min_stack is empty or the current value is less than or equal to the top of min_stack,
        # push the new value to maintain the current minimum.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the top element from the data stack.
        top_val = self.stack.pop()
        # If the popped value is the same as the top of the min stack,
        # it means the current minimum is being removed. So, pop it from min_stack as well.
        if top_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the last element in the stack.
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        # Time Complexity: O(1) using brute force approach
        return self.min_stack[
            -1
        ]  # The top of the min stack is always the current minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

