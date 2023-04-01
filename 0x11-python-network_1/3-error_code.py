#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} URL".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except ValueError:
        print("Error: Invalid URL")
    except error.HTTPError as e:
        print("HTTP Error: {}".format(e.code))
    except error.URLError as e:
        print("URL Error: {}".format(e.reason))
    except Exception as e:
        print("Error: {}".format(e))
