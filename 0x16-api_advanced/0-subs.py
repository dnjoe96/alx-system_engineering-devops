#!/usr/bin/python3
""" First function for advanced API
    Get the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Function to get the number of subscribers to a sub reddit """
    base_url = "https://www.reddit.com"
    header = {'User-Agent': 'JoeAPI', 'Content-Type': 'application/json'}
    res = requests.get(base_url + f'/r/{subreddit}/about.json',
                       headers=header, allow_redirects=False)
    if res.status_code != 200:
        return 0
    num_subs = res.json().get("data").get("subscribers")
    return num_subs
