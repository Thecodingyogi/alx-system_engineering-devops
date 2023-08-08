#!/usr/bin/python3
"""Function to query the reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "user-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
