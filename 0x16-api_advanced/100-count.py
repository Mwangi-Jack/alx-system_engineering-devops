import requests

def recurse(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers={"User-Agent": "YourApp/1.0"}, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        posts = data['data']['children']

        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post['data']['title'].lower())  # Convert title to lowercase

        after = data['data'].get('after')

        if after:
            return recurse(subreddit, word_list, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 302:
        print(f"The subreddit '{subreddit}' is invalid or may have been removed.")
        return hot_list
    else:
        print("Failed to retrieve data from Reddit:", response.status_code)
        return hot_list

def count_words(subreddit, word_list):
    hot_articles = recurse(subreddit, word_list)

    if hot_articles is None:
        return
    word_count = {}
    for title in hot_articles:
        for word in word_list:
            if word.lower() in title:
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_count:
        print(f"{word}: {count}")
