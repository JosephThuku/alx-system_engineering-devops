#!/usr/bin/python3
"""
script to prints the titles of the first
10 hot posts listed for
a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return top 10 hot posts from given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'My Holbie User Agent 1.0',
    }

    response = requests.get(url, headers=headers).json()
    if response.get("message") == "Not Found":
        print("None")
    else:
        children_list = response.get("data").get("children", [])
        for titles in children_list:
            print(titles.get('data').get('title'))
