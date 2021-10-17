import praw
import datetime as dt
reddit = praw.Reddit(client_id='', client_secret='', user_agent='', username='', password='')

subreddit = reddit.subreddit('Dankmemes')
toplatest = subreddit.top(limit=100)

for i in toplatest:
    print(i.title, i.id)