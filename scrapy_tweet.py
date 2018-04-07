import tweepy
import sys
import csv
import time


consumer_key = "uUD5gEyrQx0CDfQ7pjzsrABjb"
consumer_secret = "Gmz3gNv5FG52Y2f2xE9Nmx1cU5EZZJrxXwr03RyVphyw4DLavl"
access_token = "1547323880-ESPqufpNIBRIbJayqtGoFhkbD2TVeC1OfsWc7fU"
access_token_secret = "30XYAnJbesYSYT6hehQzJLLRRhz2OU5BO7eTz8YJeqm7C"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


query = [u"\U0001F602",u"\U0001F600",u"\U0001F389",u"\U0001F44D",u"\U0001F4A9"]

idx = 1


search = tweepy.Cursor(api.search, q="trump -filter:retweets",lang = 'en').items(10000)
filename = 'emoji_nostream_' + str(idx) + '.csv'

with open(filename,'a',newline='\n') as f:
    writer = csv.DictWriter(f,fieldnames=['tweet','label'])
    writer.writeheader()
    for tweet in search:
        text = tweet.text
        writer.writerow({'tweet':text,'label':idx})
        