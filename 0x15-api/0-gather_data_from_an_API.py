#!/usr/bin/python3
"""Script that return information about an employee's TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(url + f"users/{user_id}").json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    user_name = user["name"]

    number_of_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
                                                          user_name,
                                                          num_completed_tasks,
                                                          number_of_tasks))
    for task in completed_tasks:
        print(f"\t{task['title']}")
