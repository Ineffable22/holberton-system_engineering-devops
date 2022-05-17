#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script
to export data in the JSON format. """
import json
import requests
from sys import argv


def Rest_API():
    """ Get data """
    # Validates if argument is integer and has index
    try:
        ID = int(argv[1])
    except ValueError:
        print("Value Error")
        exit()
    except IndexError:
        print("Index Error")
        exit()

    # Get Method
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(ID))
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(ID))

    # Variables
    username = user.json().get('username')
    datafile = {}
    datafile[ID] = []

    # export data in JSON format
    with open("{}.json".format(ID), "w") as fo:
        for data in todo.json():
            text = data.get("title")
            task = data.get("completed")
            datafile[ID].append({
                "task": text,
                "completed": task,
                "username": username,
            })
        json.dump(datafile, fo)


if __name__ == '__main__':
    Rest_API()
