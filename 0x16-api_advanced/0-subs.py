#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'My Reddit API Client'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
