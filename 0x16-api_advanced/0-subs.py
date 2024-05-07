#!/usr/bin/python3
"""
Qerying Reddit API to get information about
a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function queries the RedditAPI and returns the
    number of subscribers for the provided subreddit
    """
    headers = {"User-Agent": "MyApp/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 302:
        return 0
    else:
        return 0
