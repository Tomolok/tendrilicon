import praw
from cred import *

reddit = praw.Reddit(client_id=my_id,
                     client_secret=my_key,
                     user_agent=my_user)

for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)

