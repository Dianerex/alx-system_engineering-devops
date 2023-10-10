#!/usr/bin/python3
"""Module for task 2"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""

import requests

def get_hot_posts(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API and returns all hot posts of the subreddit.

    :param subreddit: The name of the subreddit to retrieve hot posts from.
    :param hot_list: A list to store hot post titles.
    :param count: The count of posts to skip.
    :param after: The 'after' parameter for pagination.
    :return: A list of hot post titles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Your-User-Agent"}  # Replace with your own User-Agent.

    response = requests.get(url, params={"count": count, "after": after}, headers=headers, allow_redirects=False)

    if response.status_code >= 400:
        print(f"Error: Request failed with status code {response.status_code}")
        return None

    data = response.json()
    hot_posts = [child['data']['title'] for child in data['data']['children']]

    if not data['data']['after']:
        return hot_list + hot_posts
    else:
        return get_hot_posts(subreddit, hot_list + hot_posts, data['data']['count'], data['data']['after'])

if __name__ == "__main__":
    subreddit = "python"  # Replace with the subreddit you want to query.
    hot_posts = get_hot_posts(subreddit)

    if hot_posts:
        for i, post in enumerate(hot_posts, start=1):
            print(f"{i}. {post}")
    else:
        print("No hot posts found.")
