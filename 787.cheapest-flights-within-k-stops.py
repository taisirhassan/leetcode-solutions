#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (39.87%)
# Likes:    10339
# Dislikes: 437
# Total Accepted:    679.9K
# Total Submissions: 1.7M
# Testcase Example:  '4\n[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]\n0\n3\n1'
#
# There are n cities connected by some number of flights. You are given an
# array flights where flights[i] = [fromi, toi, pricei] indicates that there is
# a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return
# -1.
#
#
# Example 1:
#
#
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
# src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and
# has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because
# it uses 2 stops.
#
#
# Example 2:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and
# has cost 100 + 100 = 200.
#
#
# Example 3:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost
# 500.
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 10^4
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
#
#
#


# @lc code=start
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Approach 1: Dijkstra's Algorithm
        # Time: O(E + VlogV)
        # Space: O(V + E)

        # graph = defaultdict(list)
        # for start, end, price in flights:
        #     # build the graph using adjacency list representation
        #     graph[start].append((end, price))  # (city, cost)

        # # priority queue stores (cost, city, remaining_stops)
        # pq = [(0, src, k + 1)]  # k stops means k+1 flights

        # # visited[city] = (remaining_stops, cost) to prune worse paths
        # visited = {}

        # while pq:
        #     cost, city, stops = heapq.heappop(pq)

        #     # found destination
        #     if city == dst:
        #         return cost

        #     # no more stops allowed
        #     if stops <= 0:
        #         continue

        #     # skip if we've seen this city with better conditions
        #     if (
        #         city in visited
        #         and visited[city][0] >= stops
        #         and visited[city][1] <= cost
        #     ):
        #         continue

        #     # record this visit
        #     visited[city] = (stops, cost)

        #     # explore neighbours
        #     for next_city, price in graph[city]:
        #         heapq.heappush(pq, (cost + price, next_city, stops - 1))

        # return -1  # no path found

        # Approach 2: Bellman-Ford Algorithm (Dynamic Programming)
        # Time: O(k * E) where k is the number of stops and E is the number of flights
        # Space: O(V) where V is the number of cities

        # initialize prices array with infinity for all cities
        prices = [float("inf")] * n
        prices[src] = 0  # starting city has cost of 0

        # relax edges k+1 times to find the shortest path (k stops means k+1 flights)
        for i in range(k + 1):
            # create a copy of the prices array to avoid updating the array in the same iteration
            temp = prices.copy()
            # for each flight
            for start, end, price in flights:
                # if we can reach the start city
                if prices[start] != float("inf"):
                    # update min cost to reach end city
                    temp[end] = min(temp[end], prices[start] + price)
            prices = temp  # update prices for the next iteration
        return (
            prices[dst] if prices[dst] != float("inf") else -1
        )  # return the result (-1 if no path found)


# @lc code=end
