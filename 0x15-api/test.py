#!/usr/bin/python3

import sys
import json
import urllib.request


base_url = "https://jsonplaceholder.typicode.com"

userId = sys.argv[1]
todourl = f"{base_url}/todos?userId={userId}"
user_url = f"{base_url}/users/{userId}"


def getuser():
    response = urllib.request.urlopen(user_url)
    data = response.read()
    data_str =  data.decode('utf-8')
    user = json.loads(data_str)
    return user['name']

def getTodo():

	todo_response = urllib.request.urlopen(todourl)
	data_bytes = todo_response.read()

	data_str = data_bytes.decode('utf-8')

	todos = json.loads(data_str)

	total_todos = len(todos)
	incomplete = 0
	completed_todos = []
	for todo in todos:
		if todo['completed'] is False:
			incomplete += 1
			completed_todos.append(todo)

	return (total_todos, incomplete, completed_todos)


user = getuser()
total_todos, incomplete, completed_todos = getTodo()

print(f"Employee {user} is done with tasks({incomplete}/{total_todos}):")
for todo in completed_todos:
    print(f"\t{todo['title']}",)
