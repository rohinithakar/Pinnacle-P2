__author__ = 'rohini'

import requests
from requests.exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError
)
'''
Use the method over here instead of requests.post, requests.get
'''
default_mooc = "http://localhost:8080/"

def makePostRequest(url, data=None, **kwargs):
    try:
        response = requests.post(default_mooc + url, data=data, **kwargs)
    except ConnectionError:
        print "Could not connect to remote host"
        response=None
    return response

def makeGetRequest(url, **kwargs):
    return requests.get(default_mooc + url, **kwargs)

def makePutRequest(url, data=None, **kwargs):
    return requests.put(default_mooc + url, data=data, **kwargs)

def makeDeleteRequest(url, **kwargs):
    return requests.delete(default_mooc + url, **kwargs)
