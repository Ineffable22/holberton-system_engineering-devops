#!/usr/bin/python3
""" Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not)
"""
import requests
import re


def f_after(subreddit, hot_list="", after=""):
    """Recursive function find to length of hot_list
    Args:
        subreddit: Account to search
        hot_list: hot list of Reddit
        after: next page of API
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after is not None:
        with requests.Session() as res:
            data = res.get(url,
                           headers={'User-Agent': 'AgentMEGO'},
                           params={'after': after})
            if data.status_code != 200:
                return None
            after = data.json().get('data').get('after')
            hot_list += " ".join([
                i.get('data').get('title')
                for i in data.json().get('data').get('children')
            ]) + " "
            return f_after(subreddit, hot_list, after)
    return (hot_list)


def count_words(subreddit, word_list):
    """Returns a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given subreddit,
    the function should return None.

    Args:
        subreddit: Account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return None

    data = f_after(subreddit, "", "")
    data_list = {}
    num = 0
    for i in word_list:
        search = [char for char in i]
        re_search = ""
        for word in search:
            if word.isalpha():
                re_search += "[{}{}]".format(word.lower(), word.upper())
            else:
                re_search += word
        text = re.compile(re_search + " ")
        i = i.lower()
        num += len(text.findall(data))
        data_list[i] = num
        num = 0
    
    new_dict = ({k: v for k, v in sorted(data_list.items(), key=lambda item: item[1])})
    for a, b in new_dict.items():
        if b != 0:
            print("{}: {}".format(a, b))
