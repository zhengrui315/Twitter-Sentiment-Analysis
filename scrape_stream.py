import tweepy
import sys
import csv
import time
import json

consumer_key = "uUD5gEyrQx0CDfQ7pjzsrABjb"
consumer_secret = "Gmz3gNv5FG52Y2f2xE9Nmx1cU5EZZJrxXwr03RyVphyw4DLavl"
access_token = "1547323880-ESPqufpNIBRIbJayqtGoFhkbD2TVeC1OfsWc7fU"
access_token_secret = "30XYAnJbesYSYT6hehQzJLLRRhz2OU5BO7eTz8YJeqm7C"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




class MyListener(tweepy.StreamListener):
    """
    set a time limit for the stream
    """

    def __init__(self, time_limit=10, label=0):
        self.start_time = time.time()
        self.limit = time_limit
        self.label = label
        super(MyListener, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            t = json.loads(data)
            with open('emoji_' + str(self.label) + '.csv', 'a', newline='\n') as f:
                if not t['text'].startswith('RT'):
                    writer = csv.DictWriter(f, fieldnames=['tweet', 'label'])
                    writer.writerow({'tweet': t['text'], 'label': self.label})
            return True
        else:
            return False

    def on_error(self, status_code):
        if status_code == 420 or status_code == 429:
            print('rate limit error: status code is ', status_code)
            return False


class MyListener_notimelimit(tweepy.StreamListener):
    """
    there is no time limit, the stream will be stopped by hand
    """

    def __init__(self, label=0):
        self.label = label
        super(MyListener_notimelimit, self).__init__()

    def on_data(self, data):
        t = json.loads(data)
        with open('emoji_' + str(self.label) + '.csv', 'a', newline='\n') as f:
            if not t['text'].startswith('RT'):
                writer = csv.DictWriter(f, fieldnames=['tweet', 'label'])
                writer.writerow({'tweet': t['text'], 'label': self.label})
        return True

    def on_error(self, status_code):
        if status_code == 420 or status_code == 429:
            print('rate limit error: status code is ', status_code)
            return False


def scrape_emoji(query,idx,time_limit=0,first=False):
    """
    (1) time_limit indicates the length of running time,
    (2) first denotes whether it is the first time to run, because if False, don't write the header
    """
    if first:
        filename = 'emoji_' + str(idx) + '.csv'
        with open(filename,'w',newline='\n') as f:
            writer = csv.DictWriter(f,fieldnames=['tweet','label'])
            writer.writeheader()
    # if there is NO time limit
    if time_limit==0:
        twitterStream = tweepy.Stream(auth, MyListener_notimelimit(label=idx))
    # if there is time limit
    else:
        twitterStream = tweepy.Stream(auth, MyListener(time_limit=time_limit,label=idx))
    twitterStream.filter(track=[query[idx]], languages = ["en"], stall_warnings = True, async=True)


if __name__ == “__main__”:
    query = [u"\U0001F602", u"\U0001F600", u"\U0001F389", u"\U0001F44D", u"\U0001F4A9"]
    scrape_emoji(query, idx=4, time_limit=0, first_time=True)