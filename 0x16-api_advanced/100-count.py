#!/usr/bin/python3
""" Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not)
"""
import requests


def f_after(subreddit, hot_list, after=""):
    """Recursive function find to length of hot_list
    Args:
        subreddit: Account to search
        hot_list: hot list of Reddit
        after: next page of API
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after is not None:
        data = requests.get(url,
                            headers={'User-Agent': 'AgentMEGO'},
                            params={'after': after})
        if data.status_code != 200:
            return None
        after = data.json().get('data').get('after')
        JSON = data.json().get('data').get('children')
        for value in JSON:
            hot_list.append(value.get('data').get('title'))
        return f_after(subreddit, hot_list, after)
    return (hot_list)


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(
        d.items(), key=lambda x: x[1], reverse=reverse))


def count_words(subreddit, word_list):
    """Returns a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given subreddit,
    the function should return None.

    Args:
        subreddit: Account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return None

    data = f_after(subreddit, [], "")
    data = " ".join(data)
    data = data.split(" ")

    data_list = {}
    num = 0

    for i in word_list:
        """
        search = [char for char in i]
        re_search = ""
        for word in search:
            if word.isalpha():
                re_search += "[{}{}]".format(word.lower(), word.upper())
            else:
                re_search += word
        for val in data:
            text = re.compile("\\W" + re_search + "\\W")
            if text.findall(val) != []:
        num += 1
        """
        for val in data:
            i = i.lower()
            if val.lower() == i:
                num += 1
        if i in data_list.keys():
            data_list[i] = data_list[i] + num
        else:
            data_list[i] = num
        num = 0

    new_data = data_list
    tmp_key = ""
    tmp_value = 0
    char1 = []
    char2 = []
    x = 0
    newnew = {}
    new_data = sort_dict_by_value(new_data, True)
    for key, value in new_data.items():
        if value == 0:
            continue
        newnew[key] = value
        if value == tmp_value:
            char1 = [char for char in key]
            char2 = [charr for charr in tmp_key]
            c1 = ord(char1[x])
            c2 = ord(char2[x])
            c3 = 0
            while (c1 and c2):
                c1 = ord(char1[x])
                c2 = ord(char2[x])
                if c1 < c2:
                    c3 = 0
                    break
                elif c1 > c2:
                    c3 = 1
                    break
                x += 1
            if c3 == 0:
                del newnew[tmp_key]
                newnew[key] = value
                newnew[tmp_key] = tmp_value
                tmp_key = tmp_key
                tmp_value = tmp_value
                continue
        tmp_key = key
        tmp_value = value

    for a, b in newnew.items():
        print("{}: {}".format(a, b))
