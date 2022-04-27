#!/usr/bin/python3
""" Second function for advanced API """
import requests


def top_ten(subreddit):
    """ Function to get the top ten hot topic """
    base_url = "https://www.reddit.com"
    header = {'User-Agent': 'JoeAPI', 'Content-Type': 'application/json'}
    param = {"limit": "10"}
    res = requests.get(base_url + f'/r/{subreddit}/hot.json',
                       headers=header, params=param,
                       allow_redirects=False)
    if res.status_code != 200:
        print("None")
    else:
        hot_list = res.json().get("data").get("children")
        hot_titles = [post.get("data").get("title") for post in hot_list]
        print(*hot_titles, sep='\n')
