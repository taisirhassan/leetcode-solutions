#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (56.79%)
# Likes:    3402
# Dislikes: 265
# Total Accepted:    349.1K
# Total Submissions: 614K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has some number of cards and she wants to rearrange the cards into
# groups so that each group is of size groupSize, and consists of groupSize
# consecutive cards.
#
# Given an integer array hand where hand[i] is the value written on the i^th
# card and an integer groupSize, return true if she can rearrange the cards, or
# false otherwise.
#
#
# Example 1:
#
#
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
#
#
# Example 2:
#
#
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
#
#
#
#
# Constraints:
#
#
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length
#
#
#
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
#
#


# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Approach 1: Sorting With Counter
        # Time: O(nlogn)
        # Space: O(n)
        # if total number of cards is not divisible by groupSize, it's impossible to form groups
        # if len(hand) % groupSize != 0:
        #     return False

        # # count the number of cards
        # card_count = Counter(hand)

        # # process cards in sorted order to always start with the smallest available card
        # for card in sorted(card_count.keys()):
        #     # if there are no cards of this value, skip
        #     if card_count[card] > 0:
        #         # frequency of the current smallest card determines how many groups start with 'card'
        #         freq = card_count[card]
        #         # try to form a group starting from 'card' to 'card + groupSize - 1'
        #         for i in range(card, card + groupSize):
        #             # if any card in the consecutive sequence does not have enough count, return False
        #             if card_count[i] < freq:
        #                 return False
        #             # decrease the frequency as these cards are now used in the groups
        #             card_count[i] -= freq

        # # all groups have been successfully formed
        # return True

        # Approach 2: Min Heap
        # Time: O(nlogm)
        # Space: O(n)
        # if total number of cards is not divisible by groupSize, it's impossible to form groups
        # if len(hand) % groupSize != 0:
        #     return False

        # # count the frequency of each card
        # card_count = Counter(hand)

        # # create a min-heap from the unique cards
        # min_heap = list(card_count.keys())
        # heapq.heapify(min_heap)

        # # process the cards while there are still cards in the heap
        # while min_heap:
        #     # get the smallest card available
        #     first = min_heap[0]

        #     # try to form a group starting from 'first'
        #     for card in range(first, first + groupSize):
        #         # if there is not enough frequency of the required card, return False
        #         if card_count[card] == 0:
        #             return False
        #         # decrement the count of the card as it's used in the current group
        #         card_count[card] -= 1

        #         # if count becomes zero, remove it from the heap.
        #         if card_count[card] == 0:
        #             # since our heap may contain stale entries, only pop the top element if it has zero count
        #             if card == min_heap[0]:
        #                 heapq.heappop(min_heap)
        #             else:
        #                 # The card's count reached zero but it is not the top element.
        #                 # We rely on the fact that when it reaches the top, its count is 0 and it will be popped.
        #                 pass

        # # All groups formed successfully
        # return True

        # Approach 3: Hash Map
        # Time: O(n)
        # Space: O(n)
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True


# @lc code=end
