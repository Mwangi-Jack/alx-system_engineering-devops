#!/usr/bin/python3

import csv
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{userId}",
                        timeout=10).json()['username']
    todos = requests.get(f"{base_url}/todos?userid={userId}",
                         timeout=10).json()

    with open(f"{userId}.csv", "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        # csv_writer.writerow(todos[0].keys())

        for todo in todos:
            # csv_writer.writerow(todo.values())
            file.write("\"{}\", \"{}\", \"{}\", \"{}\"\n".
                       format(userId, user, todo['completed'], todo['title']))
