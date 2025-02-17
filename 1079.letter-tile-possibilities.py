#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (76.40%)
# Likes:    2557
# Dislikes: 72
# Total Accepted:    113.1K
# Total Submissions: 147.3K
# Testcase Example:  '"AAB"'
#
# You have n  tiles, where each tile has one letter tiles[i] printed on it.
#
# Return the number of possible non-empty sequences of letters you can make
# using the letters printed on those tiles.
#
#
# Example 1:
#
#
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
#
#
# Example 2:
#
#
# Input: tiles = "AAABBC"
# Output: 188
#
#
# Example 3:
#
#
# Input: tiles = "V"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
#
#
#


# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Approach DFS Backtracking
        # Time: O(n!)
        # Space: O(n)
        # Create a frequency counter for the given tiles
        tile_counts = Counter(tiles)

        # Initialize the total count of valid sequences to 0.
        # Note: We are not counting the empty sequence.
        self.count = 0

        def dfs(counter):
            # Iterate over all letters in the counter
            for letter in counter:
                if counter[letter] > 0:
                    # Use the letter by decrementing its count
                    counter[letter] -= 1
                    # Every time we add a letter, it forms a valid sequence.
                    self.count += 1
                    # Recursively call dfs to add more letters to the sequence
                    dfs(counter)
                    # Backtrack: restore the count for the letter
                    counter[letter] += 1

        # Kick off the DFS recursion with the full frequency counter.
        dfs(tile_counts)

        # Return the total count of valid sequences
        return self.count


# @lc code=end
