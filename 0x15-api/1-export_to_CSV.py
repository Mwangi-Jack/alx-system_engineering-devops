#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{userId}",
                        timeout=10).json()['username']
    todos = requests.get(f"{base_url}/todos?userid={userId}",
                         timeout=10).json()

    with open(f"{userId}.csv", "w", encoding="utf-8") as file:
        for todo in todos:
            file.write("\"{}\", \"{}\", \"{}\", \"{}\"\n".
                       format(userId, user, todo['completed'], todo['title']))
