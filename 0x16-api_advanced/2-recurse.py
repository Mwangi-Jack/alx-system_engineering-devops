#!/usr/bin/python3
"""
Using a recursive function
"""

import requests


def recurse(subreddit, hot_list=[]):
    """method to get post titles"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 100}

    response = requests.get(url, headers={'User-Agent': 'MyApp/1.0'},
                            params=params, timeout=5, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            return None

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data'].get('after')

        if after:
            return recurse(subreddit, hot_list)
        else:
            return hot_list

    elif response.status_code == 302:
        return None
