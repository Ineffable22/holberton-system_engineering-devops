#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script
to export data in the CSV format. """
import csv
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

    username = user.json().get('username')

    # Print
    with open("{}.csv".format(ID), "w") as fo:
        writer = csv.writer(fo, quoting=csv.QUOTE_ALL)
        for data in todo.json():
            text = data.get("title")
            task = data.get("completed")
            writer.writerow([ID, username, task, text])


if __name__ == '__main__':
    Rest_API()
