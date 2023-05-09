#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function
should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after="temp"):
    """
    Recursive function that return titles of all hot articles
    of a given subreddit and None if no results found
    """
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'My Holbie User Agent 1.0',
    }
    if after != "temp":
        url = url + "?after={}".format(after)

    try:
        body = requests.get(url, headers=headers,
                            allow_redirects=False).json().get('data')

        after = body.get('after', None)
        for titles in body.get('children'):
            hot_list.append(titles.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
