#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves hot posts from a specified subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot posts from.
        hot_list (list): A list to store the titles of hot posts.
        after (str, optional): The ID of the last retrieved post.

    Returns:
        list: A list of titles of hot posts, or None if subreddit is invalid
              or there is an error with the request.
    """
    headers = {'User-Agent': 'My Reddit API Client'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post['data']['title'] for post in
                         data['data']['children']])
        if data['data']['after']:
            recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    else:
        return None
