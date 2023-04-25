#!/usr/bin/python3
"""
Extend Python script from task0 to export data in the JSON format.
"""
import json
import requests


def all_to_json():
    """
    Export the API data into json format
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    user_list = []
    for user in users:
        user_list.append((user.get("id"), user.get("username")))

    todo = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    todo_list = []
    for tasks in todo:
        todo_list.append((tasks.get("userId"),
                          tasks.get("completed"),
                          tasks.get("title")))

    all_dict = {}
    for user in user_list:
        task_list = []
        for task in todo_list:
            if task[0] == user[0]:
                task_list.append({"username": user[1],
                                  "task": task[2],
                                  "completed": task[1]})
        all_dict[str(user[0])] = task_list

    filename = "todo_all_employees.json"

    with open(filename, 'w') as jsonfile:
        json.dump(all_dict, jsonfile)


if __name__ == "__main__":
    all_to_json()
