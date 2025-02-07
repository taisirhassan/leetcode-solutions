#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (41.17%)
# Likes:    12517
# Dislikes: 1910
# Total Accepted:    1.3M
# Total Submissions: 3M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # Approach 1: BFS
        # # Time complexity: O(M^2 * N)
        # # Space complexity: O(M^2 * N)

        # # Convert the wordList to a set for O(1) lookup times.
        # wordSet = set(wordList)

        # # Early exit: if the endWord is not in the dictionary, no valid transformation exists.
        # if endWord not in wordSet:
        #     return 0

        # # Initialize a queue for BFS.
        # # Each element is a tuple: (current_word, transformation_length)
        # # The transformation length starts at 1 because the beginWord is counted as a step.
        # queue = deque([(beginWord, 1)])

        # # Process nodes in the queue until it's empty.
        # while queue:
        #     current_word, steps = queue.popleft()

        #     # If the current word is the target, return the number of steps.
        #     if current_word == endWord:
        #         return steps

        #     # Try changing every letter in the current word.
        #     for i in range(len(current_word)):
        #         # For each position i, try all 26 lowercase letters.
        #         for char in "abcdefghijklmnopqrstuvwxyz":
        #             # Form the new word by replacing the character at position i.
        #             new_word = current_word[:i] + char + current_word[i + 1 :]

        #             # If the new word exists in the wordSet, it's a valid transformation.
        #             if new_word in wordSet:
        #                 # Add the new word and its level (steps + 1) to the BFS queue.
        #                 queue.append((new_word, steps + 1))
        #                 # Remove the word from the set to avoid processing it again.
        #                 wordSet.remove(new_word)

        # # If we exit the loop without finding endWord, return 0.
        # return 0

        # Approach 2: Bidirectional BFS
        # Time complexity: O(M^2 * N)
        # Space complexity: O(M^2 * N)
        # Convert the wordList to a set for O(1) lookups.
        wordSet = set(wordList)

        # If the endWord is not present, no valid transformation exists.
        if endWord not in wordSet:
            return 0

        # Initialize two sets for bidirectional search.
        # Begin from the start word and the end word.
        beginSet = {beginWord}
        endSet = {endWord}

        # Remove the beginWord if it's in wordSet (although it's not required per problem statement)
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        # Initialize the transformation sequence length.
        length = 1

        # Continue until either beginSet or endSet is empty.
        while beginSet and endSet:
            # Always expand the smaller set to optimize performance.
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            # This set will hold the next level of words.
            next_level = set()

            # Process each word in the current beginSet.
            for word in beginSet:
                # Try changing every letter of the current word.
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        # Form a new word by replacing the character at position i.
                        new_word = word[:i] + char + word[i + 1 :]

                        # Check if the new word is in the opposite search frontier.
                        if new_word in endSet:
                            return length + 1

                        # If the new word is in the wordSet, add it to the next level.
                        if new_word in wordSet:
                            next_level.add(new_word)
                            # Remove to avoid future duplicates.
                            wordSet.remove(new_word)

            # Update the current search frontier to the next level.
            beginSet = next_level
            # Increment the length as we've moved one level further.
            length += 1

        # If no connection is found between the two searches, return 0.
        return 0


# @lc code=end
