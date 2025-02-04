#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (60.72%)
# Likes:    10884
# Dislikes: 2124
# Total Accepted:    739.6K
# Total Submissions: 1.2M
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# You are given an array of CPU tasks, each labeled with a letter from A to Z,
# and a number n. Each CPU interval can be idle or allow the completion of one
# task. Tasks can be completed in any order, but there's a constraint: there
# has to be a gap of at least n intervals between two tasks with the same
# label.
#
# Return the minimum number of CPU intervals required to complete all tasks.
#
#
# Example 1:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
#
# Output: 8
#
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A ->
# B.
#
# After completing task A, you must wait two intervals before doing A again.
# The same applies to task B. In the 3^rd interval, neither A nor B can be
# done, so you idle. By the 4^th interval, you can do A again as 2 intervals
# have passed.
#
#
# Example 2:
#
#
# Input: tasks = ["A","C","A","B","D","B"], n = 1
#
# Output: 6
#
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
#
# With a cooling interval of 1, you can repeat a task after just one other
# task.
#
#
# Example 3:
#
#
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
#
# Output: 10
#
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle
# -> idle -> A -> B.
#
# There are only two types of tasks, A and B, which need to be separated by 3
# intervals. This leads to idling twice between repetitions of these tasks.
#
#
#
# Constraints:
#
#
# 1 <= tasks.length <= 10^4
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100
#
#
#


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Approach 1: Greedy Approach
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # # 1. Count the frequency of each task
        # task_counts = Counter(tasks)
        # # 2. Get the max frequency task among all the tasks
        # max_freq = max(task_counts.values())

        # # 3. Count the number of tasks that have the same max frequency
        # count_max = sum(1 for task, count in task_counts.items() if count == max_freq)

        # # Step 4: Calculate the number of intervals required to complete the tasks
        # intervals = (max_freq - 1) * (n + 1) + count_max

        # # 5. Return the maximum of the intervals and the total number of tasks
        # return max(intervals, len(tasks))

        # Approach 2: Using Priority Queue (Heap) and Queue
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # Step 1: Count the frequency of each task.
        task_counts = Counter(tasks)

        # Step 2: Create a max heap (using negative counts because heapq is a min-heap).
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)

        # Step 3: Initialize a queue to track tasks that are cooling down.
        # Each element is a tuple: (available_time, remaining_count)
        cooldown_queue = deque()

        # Variable to track the current time (or CPU interval)
        time = 0

        # Step 4: Process until all tasks have been scheduled (heap and queue are empty).
        while max_heap or cooldown_queue:
            # Check if any tasks in cooldown are now ready to be executed.
            if cooldown_queue and cooldown_queue[0][0] <= time:
                available_time, remaining_count = cooldown_queue.popleft()
                # Re-add the task back into the max heap.
                heapq.heappush(max_heap, remaining_count)

            if max_heap:
                # Execute the task with the highest remaining frequency.
                current_count = heapq.heappop(max_heap)
                # Increase current_count towards 0 (remember, it's negative)
                current_count += 1

                # If the task still has remaining executions, add it to the cooldown queue.
                if current_count != 0:
                    # It will be available after n intervals (i.e., at time+ n + 1).
                    cooldown_queue.append((time + n + 1, current_count))
            # If there is no task available, the CPU idles for this time unit.
            # (Note: Even if we idle, we still need to progress time.)

            # Increment the time counter.
            time += 1

        return time


# @lc code=end
