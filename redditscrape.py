import praw
from keys import *
import datetime as dt
import requests
from time import sleep
reddit = praw.Reddit(client_id=ClientID, client_secret=ClientSecret, user_agent=UserAgent, username=username, password=password)

#Define the subreddits to pull from
subs = ['dankmemes', 'okbuddyretard','okboomerretard','memes','comedyheaven']
path = "memes/"
for x in subs:
    subreddit = reddit.subreddit(x)
    toplatest = subreddit.top("day", limit=100)
    for i in toplatest:
        print(i.title, i.url)
        extension = i.url.rsplit('.')[-1]
        data = requests.get(i.url).content
        try:
            with open(path + i.title + "." + extension , "wb") as file:
                file.write(data)
                file.close()
        except:
            print("ERROR DOWNLOADING " + i.title)
        #The sleep function is set to 2 here as the redditAPI rate limit is set to 30 requests per minute
        sleep(2.5)
        print("Downloaded " + i.title + "from " + x)