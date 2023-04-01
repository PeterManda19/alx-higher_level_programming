#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""

import sys
import requests

# Define the URL as a variable
URL = "http://0.0.0.0:5000/search_user"


if __name__ == "__main__":
    # Get the letter from the command line arguments or set it to an empty string
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    # Send the POST request with the payload to the URL
    response = requests.post(URL, data=payload)

    # Check if the response is successful, otherwise raise an error
    response.raise_for_status()

    # Parse the response as JSON
    json_response = response.json()

    # Check if the JSON response is empty, otherwise print the user ID and name
    if json_response:
        print(f"[{json_response['id']}] {json_response['name']}")
    else:
        print("No result")
