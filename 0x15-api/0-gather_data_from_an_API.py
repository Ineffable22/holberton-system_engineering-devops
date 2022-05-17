#!/usr/bin/python3
""" This script, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress. """
import requests
from sys import argv


def Rest_API():
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
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(ID))

    name = user.json().get('name')
    tasks = 0
    true = 0
    tittles = []
    for list_ in todo.json():
        if list_.get('userId') == ID:
            tasks += 1
            if (list_.get('completed')) is True:
                true += 1
                tittles.append(list_.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, true, tasks))
    for tittle in tittles:
        print("\t {}".format(tittle))


if __name__ == '__main__':
    Rest_API()
