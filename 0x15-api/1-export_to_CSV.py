#!/usr/bin/python3
"""
Extend Python script from task0 to export data in the CSV format.
"""
import csv
import requests
from sys import argv


def to_cvs():
    """
    Export the API data into csv format
    """
    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(api_url + "/users/{}".format(argv[1])).json()
    todo = requests.get(api_url + "/todos?userId={}".format(argv[1])).json()

    filename = "{}.csv".format(argv[1])

    with open(filename, 'w', newline='') as csvfile:
        todo_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in todo:
            todo_writer.writerow([int(argv[1]),
                                  user.get('username'),
                                  item.get('completed'),
                                  item.get('title')])


if __name__ == "__main__":
    to_cvs()
