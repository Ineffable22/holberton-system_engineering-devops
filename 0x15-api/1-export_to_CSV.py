#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script
to export data in the CSV format. """
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

    # variables
    username = user.json().get('username')
    data_file = ""

    # Print
    for data in todo.json():
        text = data.get("title")
        task = data.get("completed")
        datafile += '"{}", "{}", "{}", "{}"\n'.format(ID, username, task, text)
    with open("{}.csv".format(ID), "w") as fo:
        fo.write(datafile)


if __name__ == '__main__':
    Rest_API()
