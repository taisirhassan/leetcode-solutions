#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        # approach 1: brute force 
        # time complexity: O(n)
        # space complexity: O(1)
       
    #    ans = 0
    #    # rods are labeled from 0 to 9
    #    for rod in map(str, range(10)):
    #         hasR = hasG = hasB = False
    #        # scan for red
    #         for i in range(0, len(rings), 2):
    #            if rings[i] == 'R' and rings[i+1] == rod:
    #                hasR = True
    #                break
               
    #         for i in range(0, len(rings), 2):
    #            # scan for green
    #            if rings[i] == 'G' and rings[i+1] == rod:
    #                hasG = True
    #                break
    #         for i in range(0, len(rings), 2):
    #            # scan for blue
    #            if rings[i] == 'B' and rings[i+1] == rod:
    #                hasB = True
    #                break
    #         if hasR and hasG and hasB:
    #            ans += 1
    #    return ans
    
    # approach 2: hash map
    # time complexity: O(n)
    # space complexity: O(1)
    
        # rod_colours = defaultdict(set)
        # for i in range(0, len(rings), 2):
        #     colour, rod = rings[i], rings[i+1]
        #     rod_colours[rod].add(colour)
        # # count the number of rods that have all three colours
        # return sum(len(colours) == 3 for colours in rod_colours.values())
        
        
    # approach 3: bitmask
    # time complexity: O(n)
    # space complexity: O(1)
    # mapping colour char to a bit
        bit = {'R': 1, 'G': 2, 'B': 4}
        masks = [0] * 10 # one slot for each rod
        
        # build up mask for each rod
        for i in range(0, len(rings), 2):
            colour, rod = rings[i], int(rings[i+1])
            masks[rod] |= bit[colour] # set the bit for the colour
            
        # count rods with all three colours (7 in binary)
        return sum(mask == 7 for mask in masks)
    
      
        
# @lc code=end

