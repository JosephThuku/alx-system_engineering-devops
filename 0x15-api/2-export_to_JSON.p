#!/usr/bin/python3
"""
Extend Python script from task0 to export data in the JSON format.
"""
import json
import requests
from sys import argv


def to_json():
    """
    Export the API data into json format
    """
    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(api_url + "/users/{}".format(argv[1])).json()
    todo = requests.get(api_url + "/todos?userId={}".format(argv[1])).json()

    task_list = []

    for tasks in todo:
        tasks_dict = {
            "task": tasks.get("title"),
            "completed": tasks.get("completed"),
            "username": user.get("username")
            }
        task_list.append(tasks_dict)

        json_dict = {argv[1]: task_list}

        filename = "{}.json".format(argv[1])

        with open(filename, 'w') as jsonfile:
            json.dump(json_dict, jsonfile)


if __name__ == "__main__":
    to_json()
