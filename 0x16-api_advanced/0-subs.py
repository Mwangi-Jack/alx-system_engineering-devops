#!/usr/bin/python3
"""
Qerying Reddit API to get information about
a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """fetching the number of subscribers for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers,
                            timeout=2, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
