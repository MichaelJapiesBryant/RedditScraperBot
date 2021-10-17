import praw
from termcolor import colored
from keys import *
import requests
from time import sleep
import os
import tweepy
reddit = praw.Reddit(client_id=ClientID, client_secret=ClientSecret, user_agent=UserAgent, username=username, password=password)

#Define the subreddits to pull from
subs = []
path = "memes/"
for x in subs:
    subreddit = reddit.subreddit(x)
    toplatest = subreddit.top("day", limit=100)
    for i in toplatest:
        print(i.title, i.url)
        extension = i.url.rsplit('.')[-1]
        data = requests.get(i.url).content
        try:
            if os.path.isfile(path + i.title + "." + extension):
                continue
            with open(path + i.title + "." + extension , "wb") as file:
                file.write(data)
                file.close()
                print(colored("Downloaded " + i.title + " from " + x, 'green'))
                try:
                    auth = tweepy.OAuthHandler(TWTAPIKey, TWTAPIKEYSECRET)
                    auth.set_access_token(TWTACCESSTOKEN, TWTACCESSTOKENSECRET)
                    API = tweepy.API(auth)
                    media = API.media_upload(path + i.title + "." + extension)
                    sleep(600)
                    post_result = API.update_status(i.title, media_ids=[media.media_id])
                    print(colored("Tweeted", 'green'))
                    os.remove(path + i.title + "." + extension)
                    print(colored('Removed from local storage', 'yellow'))
                except:
                    print(colored("Failed to tweet", 'red'))
        except:
            print(colored("ERROR DOWNLOADING " + i.title, 'red'))
        #The sleep function is set to 2 here as the redditAPI rate limit is set to 30 requests per minute