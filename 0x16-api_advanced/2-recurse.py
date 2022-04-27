#!/usr/bin/python3
""" Third function for advanced API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Function to get recursive hot list """
    base_url = "https://www.reddit.com"
    header = {'User-Agent': 'JoeAPI', 'Content-Type': 'application/json'}
    param = {"limit": "10"}
    url = base_url + f'/r/{subreddit}/hot.json'
    if after:
        url += f"?after={after}"
    res = requests.get(url, headers=header, params=param,
                       allow_redirects=False)

    if res.status_code != 200:
        return None
    else:
        posts = res.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if res.json().get('data').get('after'):
            return recurse(
                subreddit,
                after=res.json().get('data').get('after'),
                hot_list=hot_list
            )
        return hot_list
