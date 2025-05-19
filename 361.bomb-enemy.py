from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # Brute Force: 
        # Time Complexity: O(m * n * (m + n))
        # Space Complexity: O(1)
        # if not grid or not grid[0]:
        #     return 0
        
        # m, n = len(grid), len(grid[0])
        # max_kills = 0
        
        # # helper to count enemies from (r, c) in direction (dr, dc)
        # def count_dir(r,c, dr, dc):
        #     cnt = 0
        #     # step until out of bounds or hit wall
        #     while 0 <= r < m and 0 <= c < n and grid[r][c] != 'W':
        #         if grid[r][c] == 'E':
        #             cnt += 1 
        #         r += dr 
        #         c += dc 
                
        #     return cnt 
        
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '0':
        #             # count enemies in all 4 directions
        #             kills = (
        #                 count_dir(i, j, 0, 1) + # right 
        #                 count_dir(i, j, 0, -1) + # left 
        #                 count_dir(i, j, 1, 0) + # down 
        #                 count_dir(i, j, -1, 0) # up 
        #             )
        #             max_kills = max(max_kills, kills) # update max kills 
                    
        # return max_kills
        
        # Approach 2: Dynamic Programming 
        # Time Complexity: O(m * n)
        # Space Complexity: O(n) 
        m, n = len(grid), len(grid[0])
        max_kills = 0
        row_hits = 0
        col_hits = [0] * n
        
        for i in range(m):
            for j in range(n):
                # recompute row if at the start of a row or after a wall
                if j == 0 or grid[i][j-1] == 'W':
                    row_hits = 0
                    k = j 
                    # count enemies to the right until a wall or end of row
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_hits += 1 
                        k += 1 
                        
                # recompute col_hits[j] if at the start of a column or after a wall
                if i == 0 or grid[i-1][j] == 'W':
                    col_hits[j] = 0
                    k = i 
                    # count enemies down until a wall or end of column
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_hits[j] += 1 
                            
                        k += 1 
                            
                # if empty space, place bomb on empty space
                if grid[i][j] == '0':
                    # the total enemies killed is the sum of enemies in the row and column
                    max_kills = max(max_kills, row_hits + col_hits[j]) # update max kills to max of current max kills and row_hits + col_hits[j] where j is the current column
                    
        return max_kills
        