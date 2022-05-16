#!/usr/bin/python3
""" This script, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress. """
import requests
from sys import argv

if __name__ == '__main__':
    # try:
    ID = argv[1]
    # except IndexError:
    # print("Insert Index")
    # exit(-1)
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(ID))
    name = user.json().get('name')
    tasks = 0
    true = 0
    tittles = []
    for list_ in todo.json():
        if list_.get('userId') == int(ID):
            tasks += 1
            if (list_.get('completed')) is True:
                true += 1
                tittles.append(list_.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, true, tasks))
    for tittle in tittles:
        print("\t " + tittle)
