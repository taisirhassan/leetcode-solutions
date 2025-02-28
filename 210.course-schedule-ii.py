#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (52.11%)
# Likes:    11187
# Dislikes: 361
# Total Accepted:    1.3M
# Total Submissions: 2.4M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
#
#
# Example 2:
#
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
#
#
# Example 3:
#
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
#
#
#


# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Approach 1: Topological Sort Using BFS (Kahn's Algorithm)
        # Time Complexity: O(V + E)
        # Space Complexity: O(V + E)
        # graph = defaultdict(list)
        # # array to keep track of prerequisites for each course (in-degree)
        # indegree = [0] * numCourses

        # # create the graph
        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)
        #     indegree[course] += 1

        # # initialize a queue with courses that have no prerequisites
        # queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        # order = []  # list to store the order of courses

        # # process courses with no prerequisites
        # while queue:
        #     current = queue.popleft()
        #     order.append(current)

        #     # reduce the in-degree of all neighbours
        #     for neighbour in graph[current]:
        #         indegree[neighbour] -= 1
        #         # if the neighbour has no more prerequisites, add it to the queue
        #         if indegree[neighbour] == 0:
        #             queue.append(neighbour)
        # # if all courses have been processed, return the order, else return an empty list (cycle)
        # return order if len(order) == numCourses else []

        # Approach 2: Topological Sort Using DFS
        # Time Complexity: O(V + E)
        # Space Complexity: O(V + E)
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

            # 0: not visited, 1: visiting, 2: visited
            state = [0] * numCourses
            order = []  # to hold the order of courses
            self.cycle_found = False  # flag to check if a cycle is found

            def dfs(course: int):
                # if a cycle is found, return early
                if self.cycle_found:
                    return

                # mark the course as visiting
                state[course] = 1
                for neighbour in graph[course]:
                    # if the neighbour is not visited, visit it
                    if state[neighbour] == 0:
                        dfs(neighbour)
                    # if neighbour is in visiting state, a cycle exists
                    elif state[neighbour] == 1:
                        # a cycle is found
                        self.cycle_found = True
                        return
                # mark the course as visited after processing all neighbours
                state[course] = 2
                order.append(course)

            # call dfs on all courses
            for i in range(numCourses):
                if state[i] == 0:
                    dfs(i)
            # if a cycle is found, return an empty list
            return [] if self.cycle_found else order[::-1]


# @lc code=end
