'''
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. 
Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. 

Each item in the news feed must be posted by users who the user followed or by the user herself. 

Tweets must be ordered from most recent to least recent.

follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
'''


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follow_map = {}
        self.user_tweets = {}
        self.tweet_count = 1

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((tweetId, self.tweet_count))
        self.tweet_count += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        user_ids = [userId]
        if userId in self.follow_map:
            user_ids += list(self.follow_map[userId])
        tweets = []
        for user_id in user_ids:
            if user_id in self.user_tweets:
                tweets += self.user_tweets[user_id][-1:-11:-1]
                if tweets > 10:
                    tweets.sort(key=lambda x:x[1], reverse=True)
                tweets = tweets[:10]
        result = []
        for tweet_id, c in tweets:
            result.append(tweet_id)

        return result




    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()
        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.follow_map:
            return False
        self.follow_map[followerId].remove(followeeId)



#Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

a = [(5, 1), (6, 2)]
a.sort(key=lambda x:x[1])
print a