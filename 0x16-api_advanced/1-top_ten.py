#!/usr/bin/python3
"""
Querying Reddit API to print the title of
hot posts
"""

import requests


def top_ten(subreddit):
    """Getting the first 10 post titlees"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 10}
    header = {"User-Agent": "YourApp/1.0"}

    response = requests.get(url,timeout=5,headers=header,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for i, post in enumerate(data['data']['children']):
            print(post['data']['title'])
            if i == 9:
                break

    elif response.status_code == 302:
        print('None')
    else:
        print('None')
