#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (36.26%)
# Likes:    4529
# Dislikes: 1014
# Total Accepted:    425K
# Total Submissions: 1.2M
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language that uses the English alphabet. However, the
# order of the letters is unknown to you.
#
# You are given a list of strings words from the alien language's dictionary.
# Now it is claimed that the strings in words are sorted lexicographically by
# the rules of this new language.
#
# If this claim is incorrect, and the given arrangement of string in words
# cannot correspond to any order of letters, return "".
#
# Otherwise, return a string of the unique letters in the new alien language
# sorted in lexicographically increasing order by the new language's rules. If
# there are multiple solutions, return any of them.
#
#
# Example 1:
#
#
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
#
#
# Example 2:
#
#
# Input: words = ["z","x"]
# Output: "zx"
#
#
# Example 3:
#
#
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Approach 1: Topological Sort using DFS
        # Time: O(V + E)
        # Space: O(V + E)
        # # build adjacency graph
        # graph = {}
        # # Keep track of all characters
        # chars = set("".join(words))

        # # compare adjacent words to build graph
        # for i in range(len(words) - 1):
        #     w1, w2 = words[i], words[i + 1]
        #     # Check if w2 is prefix of w1 (invalid case)
        #     if len(w1) > len(w2) and w1.startswith(w2):  # invalid case
        #         return ""

        #     # Find first differing character
        #     for j in range(len(w1)):
        #         if j >= len(w2):
        #             break
        #         if w1[j] != w2[j]:
        #             if w1[j] not in graph:
        #                 graph[w1[j]] = set()
        #             graph[w1[j]].add(w2[j])
        #             break

        # # DFS with cycle detection
        # visited = set()  # For nodes in current path
        # processed = set()  # For all visited nodes
        # result = []

        # def dfs(node):
        #     if node in visited:  # Cycle detected
        #         return False
        #     if node in processed:  # Already processed
        #         return True

        #     visited.add(node)
        #     if node in graph:
        #         for neighbor in graph[node]:
        #             if not dfs(neighbor):
        #                 return False

        #     visited.remove(node)
        #     processed.add(node)
        #     result.append(node)
        #     return True

        # # Process all characters
        # for c in chars:
        #     if c not in processed:
        #         if not dfs(c):
        #             return ""

        # return "".join(result[::-1])  # Reverse the result to get the correct order

        # Approach 2: Topological Sort using BFS (Kahn's Algorithm)
        # Time: O(V + E)
        # Space: O(V + E)
        # build the graph and in-degree
        graph = defaultdict(set)
        # in-degree of each character
        in_degree = defaultdict(int)
        # keep track of all characters
        chars = set("".join(words))

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(len(w1)):
                if j >= len(w2):
                    break
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # initialize queue with nodes having 0 in-degree
        queue = deque([c for c in chars if in_degree[c] == 0])
        result = []
        # bfs to process nodes in topological order
        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # check if we used all characters (no cycle)
        return "".join(result) if len(result) == len(chars) else ""


# @lc code=end
