#!/usr/bin/python3
"""Exports data in the JSON format."""
import json
import requests as r
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = r.get(url + f"users/{user_id}").json()
    user_name = user.get("username")
    todos = r.get(url + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.json", "w", newline="") as jsonfile:
        json.dump({user_id: [{
                  "task": task.get("title"),
                  "completed": task.get("completed"),
                  "username": user_name
                  } for task in todos]}, jsonfile)
