#!/usr/bin/python3
"""
Module for a function that queries the Reddit API recursively.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API & returns a list containing the titles
    of all hot articles for a given subreddit. If no results are found for the
    given subreddit, the function returns None.

    Parameters:
    subreddit (str): The subreddit to query.
    hot_list (list): The list of hot article titles (default is None).
    after (str): The ID of the last retrieved post for pagination

    Returns:
    list: A list of hot article titles or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'My Reddit API'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after']:
            hot_list = recurse(subreddit, hot_list,
                               data['data']['after'])
        return hot_list
    else:
        return None
