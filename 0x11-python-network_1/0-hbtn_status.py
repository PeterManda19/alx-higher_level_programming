#!/usr/bin/python3

# Import the 'requests' library
import requests

# Define the URL to request
url = "https://intranet.hbtn.io/status"

# Send a GET request to the URL
response = requests.get(url)

# Check if the response status code is OK (200)
if response.status_code == requests.codes.ok:
    # Print the type and content of the response
    print("Body response:")
    print(f"\t- type: {type(response.content)}")
    print(f"\t- content: {response.content}")
    
    # Print the utf-8 encoded content of the response
    print(f"\t- utf8 content: {response.text}")
else:
    # Raise an exception if the server returns an error status code
    response.raise_for_status()
