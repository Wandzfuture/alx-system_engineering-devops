#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed
"""

import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'My Reddit API Client'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
