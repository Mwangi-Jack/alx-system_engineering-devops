#!/usr/bin/python3
"""
Querying Reddit API to print the title of
hot posts
"""

import requests


def top_ten(subreddit):
    """Qerying API to print title of posts"""

    url = f'http://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, timeout=2,
                            params={"limit": 10}, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']

        for post in posts:
            print(post['data']['title'])

    elif response.status_code == 302:
        print(None)

    else:
        print(None)
