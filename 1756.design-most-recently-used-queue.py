#
# @lc app=leetcode id=1756 lang=python3
#
# [1756] Design Most Recently Used Queue
#
# https://leetcode.com/problems/design-most-recently-used-queue/description/
#
# algorithms
# Medium (75.91%)
# Likes:    309
# Dislikes: 25B
# Total Accepted:    21.6K
# Total Submissions: 28K
# Testcase Example:  '["MRUQueue","fetch","fetch","fetch","fetch"]\n[[8],[3],[5],[2],[8]]'
#
# Design a queue-like data structure that moves the most recently used element
# to the end of the queue.
#
# Implement the MRUQueue class:
#
#
# MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
# int fetch(int k) moves the k^th element (1-indexed) to the end of the queue
# and returns it.
#
#
#
# Example 1:
#
#
# Input:
# ["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
# [[8], [3], [5], [2], [8]]
# Output:
# [null, 3, 6, 2, 2]
#
# Explanation:
# MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to
# [1,2,3,4,5,6,7,8].
# mRUQueue.fetch(3); // Moves the 3^rd element (3) to the end of the queue to
# become [1,2,4,5,6,7,8,3] and returns it.
# mRUQueue.fetch(5); // Moves the 5^th element (6) to the end of the queue to
# become [1,2,4,5,7,8,3,6] and returns it.
# mRUQueue.fetch(2); // Moves the 2^nd element (2) to the end of the queue to
# become [1,4,5,7,8,3,6,2] and returns it.
# mRUQueue.fetch(8); // The 8^th element (2) is already at the end of the queue
# so just return it.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2000
# 1 <= k <= n
# At most 2000 calls will be made to fetch.
#
#
#
# Follow up: Finding an O(n) algorithm per fetch is a bit easy. Can you find an
# algorithm with a better complexity for each fetch call?
#


# @lc code=start
class MRUQueue:

    # Approach 1: Brute Force
    # Time Complexity: O(n)
    # Space Complexity: O(n) for fetch due to pop and append
    def __init__(self, n: int):
        # list of 1-indexed n elements
        # self.queue = list(range(1, n + 1))

        # Approach 2: Square Root Decomposition
        # Time Complexity: O(sqrt(n))
        # Space Complexity: O(n)

        self.block_size = int(math.sqrt(n)) or 1  # block size
        self.blocks = []  # list of blocks

        # Create blocks from 1 to n. Each block has block_size elements
        nums = list(range(1, n + 1))
        for i in range(0, n, self.block_size):
            self.blocks.append(nums[i : i + self.block_size])

    def fetch(self, k: int) -> int:

        # index = k - 1  # 0-indexed

        # element = self.queue[index]  # get the element

        # self.queue.pop(index)  # remove the element from curr position

        # self.queue.append(element)  # append the element to the end
        # return element  # return the fetched element

        k -= 1

        # Find the block that contains the k-th element.
        for block in self.blocks:
            if k < len(block):
                # Remove the element from this block.
                element = block.pop(k)
                # Append the element to the last block.
                self.blocks[-1].append(element)

                return element
            else:
                # Move to the next block.
                k -= len(block)


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
# @lc code=end
