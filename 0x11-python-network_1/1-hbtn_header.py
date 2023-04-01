#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

def get_request_id(url):
    """
    Sends a request to the URL and returns the value of the X-Request-Id variable
    found in the header of the response.
    """
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            return headers.get("X-Request-Id")
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Validate input
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)

    if request_id:
        print(request_id)
