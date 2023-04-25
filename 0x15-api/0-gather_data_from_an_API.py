#!/usr/bin/python3
"""
Gather employee data from an API
"""
import requests
from sys import argv


def display():
    """
    Request and display employee data from an API
    """
    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(api_url + "/users/{}".format(argv[1])).json()
    todo = requests.get(api_url + "/todos?userId={}".format(argv[1])).json()

    completed_tasks = []

    for tasks in todo:
        if tasks.get("completed") is True:
            completed_tasks.append(tasks.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed_tasks), len(todo)))
    for titles in completed_tasks:
        print("\t {}".format(titles))


if __name__ == "__main__":
    display()
