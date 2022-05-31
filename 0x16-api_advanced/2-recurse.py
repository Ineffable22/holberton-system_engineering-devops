#!/usr/bin/python3
""" Recursive function that queries the Reddit API """
import requests


def f_after(subreddit, hot_list=[], after=""):
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
        hot_list += data.json().get('data').get('children')
        f_after(subreddit, hot_list, after)
    return (hot_list)


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given subreddit,
    the function should return None.

    Args:
        subreddit: Account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return None

    return f_after(subreddit, hot_list, "")
