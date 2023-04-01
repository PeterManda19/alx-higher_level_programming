#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-requests_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # raise an error for unsuccessful requests
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

    print(response.headers.get('X-Request-Id'))
