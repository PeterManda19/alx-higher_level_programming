#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raises an error for HTTP errors (4xx and 5xx)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
