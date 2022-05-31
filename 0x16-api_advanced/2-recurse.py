#!/usr/bin/python3
""" Recursive function that queries the Reddit API """
import requests


def recurse(subreddit):
    """Returns a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given subreddit,
    the function should return None.

    Args:
        subreddit: Account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    User_Agent = 'AgentMEGO'
    header = {'User-Agent': User_Agent}
    after = ""
    total = []
    while(after is not None):
        with requests.Session() as res:
            data = res.get(url, headers=header, params={'after': after})
            if data.status_code != 200:
                print(None)
                return
            after = data.json().get('data').get('after')
        total += data.json().get('data').get('children')
    return (total)
