__author__ = 'rohini'

import requests
from requests.exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError
)
from models import MoocInstance
'''
Use the method over here instead of requests.post, requests.get
'''
default_mooc_url = "http://localhost:8080/"
mooc_map = None

def makePostRequest(url, data=None, **kwargs):
    return __makePostRequest(default_mooc_url + url, data=data, **kwargs)

def makeGetRequest(url, **kwargs):
    return __makeGetRequest(default_mooc_url + url, **kwargs)

def makePutRequest(url, data=None, **kwargs):
    return __makePutRequest(default_mooc_url + url, data=data, **kwargs)

def makeDeleteRequest(url, **kwargs):
    return __makeDeleteRequest(default_mooc_url + url, **kwargs)


def getMoocList():
    __generateMoocMap()
    return mooc_map

def getCourse(courseId,teamName=None):
    mooc_url = __getMoocUrl(teamName)
    return __makeGetRequest(mooc_url + "course/"+courseId)

# Get course list from default mooc or from mooc with moocId
def getCourseList(teamName=None):
    mooc_url = __getMoocUrl(teamName)
    return __makeGetRequest(mooc_url + "course/list")

def getCategory(categoryId,teamName=None):
    mooc_url = __getMoocUrl(teamName)
    return __makeGetRequest(mooc_url + "category/"+categoryId)


# Get category list from default mooc or from mooc with moocId
def getCategoryList(teamName=None):
    mooc_url = __getMoocUrl(teamName)
    print "url: " + mooc_url
    return __makeGetRequest(mooc_url + "category/list")

'''
Helper methods that are private
'''
## This is real makeGetRequest
def __makeGetRequest(url, **kwargs):
    try:
        response = requests.get( url, **kwargs)
    except ConnectionError:
        print "Could not connect to remote host"
        response=None
    return response


def __makePostRequest(url, data=None, **kwargs):
    try:
        response = requests.post(url, data=data, **kwargs)
    except ConnectionError:
        print "Could not connect to remote host"
        response=None
    return response

def __makePutRequest(url, data=None, **kwargs):
    try:
        response = requests.put(url, data=data, **kwargs)
    except ConnectionError:
        print "Could not connect to remote host"
        response=None
    return response


def __makeDeleteRequest(url, **kwargs):
    try:
        response = requests.delete(url, **kwargs)
    except ConnectionError:
        print "Could not connect to remote host"
        response=None
    return response



def __getMoocUrl(teamName=None):
    if teamName==None:
        return default_mooc_url
    __generateMoocMap()
    if mooc_map[teamName]==None:
        return default_mooc_url
    else:
        return mooc_map[teamName]

# This populates mooc_map if it is none
def __generateMoocMap():
    moocs = MoocInstance.objects.all()
    global default_mooc_url
    global mooc_map
    mooc_map = {}
    for mooc in moocs:
        if mooc.default == True:
            default_mooc_url = __formatMoocUrl(mooc.url)
        mooc_map[mooc.team_name] = __formatMoocUrl(mooc.url)


# This method adds a '/' at the end of mooc url if it does not contain '/'
def __formatMoocUrl( url ):
    if not url.endswith('/'):
        return url + '/'
    else:
        return url

def __getMoocIdFromId(ObjectId):
    '''
    # This should be the real code
    mooc_id = ObjectId.split(':')[0]
    '''
    mooc_id = 'Pinnacle'
    return mooc_id