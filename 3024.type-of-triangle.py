#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # unpack the list into three variables
        a,b ,c = nums
        
        # Triangle Inequality Theorem
        # For any triangle, the sum of any two sides must be greater than the third side 
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        # check for equilateral triangle: all sides are equal
        if a == b == c:
            return "equilateral"
        
        # check for isosceles triangle: two sides are equal
        if a == b or b == c or a == c:
            return "isosceles"
        
        # other wise it is a scalene triangle
        return "scalene"
        
# @lc code=end

