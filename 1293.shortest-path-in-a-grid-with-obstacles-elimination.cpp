/*
 * @lc app=leetcode id=1293 lang=cpp
 *
 * [1293] Shortest Path in a Grid with Obstacles Elimination
 *
 * https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
 *
 * algorithms
 * Hard (45.41%)
 * Likes:    4628
 * Dislikes: 86
 * Total Accepted:    230.4K
 * Total Submissions: 506.7K
 * Testcase Example:  '[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]\n1'
 *
 * You are given an m x n integer matrix grid where each cell is either 0
 * (empty) or 1 (obstacle). You can move up, down, left, or right from and to
 * an empty cell in one step.
 * 
 * Return the minimum number of steps to walk from the upper left corner (0, 0)
 * to the lower right corner (m - 1, n - 1) given that you can eliminate at
 * most k obstacles. If it is not possible to find such walk return -1.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
 * Output: 6
 * Explanation: 
 * The shortest path without eliminating any obstacle is 10.
 * The shortest path with one obstacle elimination at position (3,2) is 6. Such
 * path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
 * Output: -1
 * Explanation: We need to eliminate at least two obstacles to find such a
 * walk.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 40
 * 1 <= k <= m * n
 * grid[i][j] is either 0 or 1.
 * grid[0][0] == grid[m - 1][n - 1] == 0
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    // Approach 1: BFS with 3D visited array
    // Time Complexity: O(m * n * k)
    // Space Complexity: O(m * n * k)
    int shortestPath(vector<vector<int>> &grid, int k){
        int m = grid.size(), n = grid[0].size();
        
        // Early exit if the destination is reachable without any eliminations. Simply would be the Manhattan distance.
        if (k >= m + n - 2)
            return m + n - 2;

        // 3D visited array: visited[x][y][remaining eliminations]
        vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(k + 1, false)));

        // Queue for BFS: each state is (x, y, remaining eliminations, steps taken)
        queue<tuple<int, int, int, int>> q;
        q.push({0, 0, k, 0});
        visited[0][0][k] = true;

        // Possible directions to move: down, up, right, left
        vector<vector<int>> directions = {
            {1, 0},  // down
            {-1, 0}, // up
            {0, 1},  // right
            {0, -1}  // left
        };

        // Begin BFS traversal
        while (!q.empty())
        {
            auto [x, y, remaining, steps] = q.front();
            q.pop();

            // If we have reached the destination (bottom right corner), return the number of steps.
            if (x == m - 1 && y == n - 1)
                return steps;

            // Explore all 4 directions.
            for (const auto &dir : directions)
            {
                int nx = x + dir[0];
                int ny = y + dir[1];

                // Check if the new coordinates are within bounds.
                if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                    continue;

                int newRemaining = remaining;

                // If the cell is an obstacle.
                if (grid[nx][ny] == 1)
                {
                    // Use one elimination if available.
                    if (newRemaining > 0)
                        newRemaining--;
                    else
                        continue; // Not enough eliminations left.
                }

                // If this state has not been visited before, mark it as visited and add it to the queue.
                if (!visited[nx][ny][newRemaining])
                {
                    visited[nx][ny][newRemaining] = true;
                    q.push({nx, ny, newRemaining, steps + 1});
                }
            }
        }

        // // Destination is unreachable.
        // return -1;
        // Approach 2: A* Search with Priority Queue and Heuristic Function
        // Time Complexity: O(m * n * k * log(m * n))
        // Space Complexity: O(m * n * k)
        // int m = grid.size(), n = grid[0].size();

        // // Early return: if k is large enough, the answer is the Manhattan distance.
        // if (k >= m + n - 2)
        //     return m + n - 2;

        // // 3D visited array: visited[x][y][remaining eliminations]
        // vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(k + 1, false)));

        // // Lambda for Manhattan distance heuristic.
        // auto heuristic = [&](int x, int y)
        // {
        //     return (m - 1 - x) + (n - 1 - y);
        // };

        // // Priority queue stores (f, steps, x, y, remaining eliminations)
        // typedef tuple<int, int, int, int, int> State;
        // priority_queue<State, vector<State>, greater<State>> pq;

        // // Start from the top-left corner.
        // pq.push({heuristic(0, 0), 0, 0, 0, k});
        // visited[0][0][k] = true;

        // // Directions: down, up, right, left.
        // vector<vector<int>> directions = {
        //     {1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        // while (!pq.empty())
        // {
        //     auto [f, steps, x, y, remaining] = pq.top();
        //     pq.pop();

        //     // Check if we've reached the destination.
        //     if (x == m - 1 && y == n - 1)
        //         return steps;

        //     for (auto &dir : directions)
        //     {
        //         int nx = x + dir[0], ny = y + dir[1];
        //         if (nx < 0 || nx >= m || ny < 0 || ny >= n)
        //             continue;

        //         int newRemaining = remaining;
        //         if (grid[nx][ny] == 1)
        //         {
        //             if (newRemaining > 0)
        //                 newRemaining--;
        //             else
        //                 continue;
        //         }

        //         if (!visited[nx][ny][newRemaining])
        //         {
        //             visited[nx][ny][newRemaining] = true;
        //             int nsteps = steps + 1;
        //             int newF = nsteps + heuristic(nx, ny);
        //             pq.push({newF, nsteps, nx, ny, newRemaining});
        //         }
        //     }
        // }

        // return -1;

    }
};
// @lc code=end

