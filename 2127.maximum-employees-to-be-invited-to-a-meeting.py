#
# @lc app=leetcode id=2127 lang=python3
#
# [2127] Maximum Employees to Be Invited to a Meeting
#
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/description/
#
# algorithms
# Hard (37.63%)
# Likes:    1510
# Dislikes: 63
# Total Accepted:    73.2K
# Total Submissions: 117.3K
# Testcase Example:  '[2,2,1,2]'
#
# A company is organizing a meeting and has a list of n employees, waiting to
# be invited. They have arranged for a large circular table, capable of seating
# any number of employees.
#
# The employees are numbered from 0 to n - 1. Each employee has a favorite
# person and they will attend the meeting only if they can sit next to their
# favorite person at the table. The favorite person of an employee is not
# themself.
#
# Given a 0-indexed integer array favorite, where favorite[i] denotes the
# favorite person of the i^th employee, return the maximum number of employees
# that can be invited to the meeting.
#
#
# Example 1:
#
#
# Input: favorite = [2,2,1,2]
# Output: 3
# Explanation:
# The above figure shows how the company can invite employees 0, 1, and 2, and
# seat them at the round table.
# All employees cannot be invited because employee 2 cannot sit beside
# employees 0, 1, and 3, simultaneously.
# Note that the company can also invite employees 1, 2, and 3, and give them
# their desired seats.
# The maximum number of employees that can be invited to the meeting is 3.
#
#
# Example 2:
#
#
# Input: favorite = [1,2,0]
# Output: 3
# Explanation:
# Each employee is the favorite person of at least one other employee, and the
# only way the company can invite them is if they invite every employee.
# The seating arrangement will be the same as that in the figure given in
# example 1:
# - Employee 0 will sit between employees 2 and 1.
# - Employee 1 will sit between employees 0 and 2.
# - Employee 2 will sit between employees 1 and 0.
# The maximum number of employees that can be invited to the meeting is 3.
#
#
# Example 3:
#
#
# Input: favorite = [3,0,1,4,1]
# Output: 4
# Explanation:
# The above figure shows how the company will invite employees 0, 1, 3, and 4,
# and seat them at the round table.
# Employee 2 cannot be invited because the two spots next to their favorite
# employee 1 are taken.
# So the company leaves them out of the meeting.
# The maximum number of employees that can be invited to the meeting is 4.
#
#
#
# Constraints:
#
#
# n == favorite.length
# 2 <= n <= 10^5
# 0 <= favorite[i] <= n - 1
# favorite[i] != i
#
#
#


# @lc code=start
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        reverse_graph = [[] for _ in range(n)]
        for i in range(n):
            reverse_graph[favorite[i]].append(i)

        # Step 1: Find all cycles
        def find_cycles():
            visited = [0] * n  # 0: unvisited, 1: visiting, 2: visited
            cycles = []
            for i in range(n):
                if visited[i] == 0:
                    path = []
                    current = i
                    while True:
                        if visited[current] == 0:
                            visited[current] = 1
                            path.append(current)
                            current = favorite[current]
                        else:
                            if visited[current] == 1:
                                # Found a cycle
                                idx = path.index(current)
                                cycle = path[idx:]
                                cycles.append(cycle)
                            # Mark all nodes in the path as visited
                            for node in path:
                                visited[node] = 2
                            break
            return cycles

        cycles = find_cycles()

        max_cycle = 0
        mutual_pairs = []
        for cycle in cycles:
            if len(cycle) == 2:
                mutual_pairs.append((cycle[0], cycle[1]))
            else:
                if len(cycle) > max_cycle:
                    max_cycle = len(cycle)

        # Step 2: Modify reverse_graph by removing mutual pair edges
        for a, b in mutual_pairs:
            if a in reverse_graph[b]:
                reverse_graph[b].remove(a)
            if b in reverse_graph[a]:
                reverse_graph[a].remove(b)

        # Step 3: Compute max_depth using post-order traversal
        max_depth = [0] * n
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                stack = []
                post_order = []
                # DFS to get post_order
                stack.append((i, False))
                while stack:
                    node, processed = stack.pop()
                    if processed:
                        post_order.append(node)
                    else:
                        if visited[node]:
                            continue
                        visited[node] = True
                        stack.append((node, True))
                        # Push children in reverse order to maintain order
                        for child in reversed(reverse_graph[node]):
                            if not visited[child]:
                                stack.append((child, False))
                # Process nodes in post_order
                for node in post_order:
                    max_d = 0
                    for child in reverse_graph[node]:
                        if max_depth[child] > max_d:
                            max_d = max_depth[child]
                    max_depth[node] = max_d + 1

        # Step 4: Compute maximum sum_chain from mutual pairs
        max_sum_chain = 0
        for a, b in mutual_pairs:
            sum_chain = max_depth[a] + max_depth[b]
            if sum_chain > max_sum_chain:
                max_sum_chain = sum_chain

        return max(max_cycle, max_sum_chain)


# @lc code=end
