#!/usr/bin/python3
"""
script to prints the titles of the first 10 hot posts
 listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """ count from afterwards """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Holbie User Agent 1.0"}

    response = requests.get(url, headers=headers).json()
    children_list = response.get("data", {}).get("children", [])

    if not children_list:
        print("None")
    else:
        for child in children_list:
            print(child["data"]["title"])

