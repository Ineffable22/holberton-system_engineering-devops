#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script
to export data in the JSON format. """
import json
import requests


def Rest_API():
    """ Get data """
    # export data in JSON format
    ID = 1
    datafile = {}
    while True:
        # Get Method
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(ID))
        todo = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(ID))
        if user.status_code != 200:
            break

        # Variables
        username = user.json().get('username')

        datafile[ID] = []
        for data in todo.json():
            text = data.get("title")
            task = data.get("completed")
            datafile[ID].append({
                "username": username,
                "task": text,
                "completed": task,
            })
        ID += 1
    with open("todo_all_employees.json", "w") as fo:
        json.dump(datafile, fo)


if __name__ == '__main__':
    Rest_API()
