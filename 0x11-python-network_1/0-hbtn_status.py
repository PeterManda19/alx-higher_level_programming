#!/usr/bin/python3
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        content = body.decode('utf-8')
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)
        print('\t- utf8 content:', content)
