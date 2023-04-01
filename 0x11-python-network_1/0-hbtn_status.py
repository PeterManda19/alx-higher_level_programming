#!/usr/bin/python3

# Import the 'request' module from the 'urllib' package
from urllib import request

# Check if this script is being run as the main program
if __name__ == "__main__":
    try:
        # Use a 'with' statement to open a connection to the URL and assign the response to 'response'
        with request.urlopen("https://intranet.hbtn.io/status") as response:
            
            # Read the response and assign it to 'response'
            response = response.read()
            
            # Print the type of the response to the console with formatting
            print("Body response:")
            print("\t- type: {}".format(type(response)))
            
            # Print the content of the response to the console with formatting
            print("\t- content: {}".format(response))
            
            # Print the utf-8 encoded content of the response to the console with formatting
            print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
    
    except Exception as e:
        print(f"Error: {e}")
        