#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (41.26%)
# Likes:    4143
# Dislikes: 581
# Total Accepted:    228.5K
# Total Submissions: 551.4K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
  '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user, and is able to see the 10 most recent tweets in
# the user's news feed.
# 
# Implement the Twitter class:
# 
# 
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId
# by the user userId. Each call to this function will be made with a unique
# tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs
# in the user's news feed. Each item in the news feed must be posted by users
# who the user followed or by the user themself. Tweets must be ordered from
# most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId
# started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId
# started unfollowing the user with ID followeeId.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed",
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]
# 
# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2
# tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is
# posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1
# tweet id -> [5], since user 1 is no longer following user 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 10^4
# All the tweets have unique IDs.
# At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and
# unfollow.
# A user cannot follow himself.
# 
# 
#

# @lc code=start
class Twitter:
    def __init__(self):
        # Global timestamp counter to order tweets. Each new tweet increases the timestamp.
        self.timestamp = 0
        
        # Dictionary to map each user to a list of their tweets.
        # Using defaultdict, each key (userId) will default to an empty list.
        # Each tweet is stored as a tuple (timestamp, tweetId).
        self.tweets = defaultdict(list)
        
        # Dictionary to map each user to the set of user IDs they follow.
        # Using defaultdict, each key (userId) will default to an empty set.
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet by a given user.
        
        Args:
            userId (int): The ID of the user posting the tweet.
            tweetId (int): The unique tweet ID.
        """
        # Increment the global timestamp for the new tweet.
        self.timestamp += 1
        
        # Append the new tweet as a tuple (timestamp, tweetId) to the user's tweet list.
        self.tweets[userId].append((self.timestamp, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        The news feed includes tweets posted by the user and by the users they follow.
        
        Args:
            userId (int): The ID of the user.
            
        Returns:
            List[int]: A list of tweet IDs representing the news feed.
        """
        # Ensure that the user follows themselves so their own tweets are included.
        self.following[userId].add(userId)
        
        # Use a heap to merge tweets from all followed users.
        # We use a min-heap with negative timestamps to simulate a max-heap (most recent tweets first).
        # Heap elements are tuples: (-timestamp, tweetId, uid, index)
        heap = []
        
        # Iterate through every user that the given user follows.
        for uid in self.following[userId]:
            # If the followed user has posted tweets, push their latest tweet into the heap.
            if self.tweets[uid]:
                # Get the index of the latest tweet in the list.
                index = len(self.tweets[uid]) - 1
                tweet_time, tweet_id = self.tweets[uid][index]
                # Push the tweet into the heap with a negative timestamp.
                heapq.heappush(heap, (-tweet_time, tweet_id, uid, index))
        
        result = []
        # Retrieve up to 10 tweets for the news feed.
        while heap and len(result) < 10:
            # Pop the tweet with the highest timestamp (most recent tweet).
            neg_time, tweet_id, uid, index = heapq.heappop(heap)
            result.append(tweet_id)
            
            # If there is an older tweet from the same user, push it onto the heap.
            if index > 0:
                next_time, next_tweet_id = self.tweets[uid][index - 1]
                heapq.heappush(heap, (-next_time, next_tweet_id, uid, index - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        The follower starts following the followee.
        
        Args:
            followerId (int): The ID of the follower.
            followeeId (int): The ID of the user to be followed.
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        The follower stops following the followee.
        Users cannot unfollow themselves.
        
        Args:
            followerId (int): The ID of the follower.
            followeeId (int): The ID of the user to be unfollowed.
        """
        # Ensure that the follower is not attempting to unfollow themselves.
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

