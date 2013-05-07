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

def getCourse(courseId):
    mooc_url = __getMoocUrl(courseId)
    return __makeGetRequest(mooc_url + "course/"+courseId)


def makePostRequest(url, data=None, **kwargs):
    return __makePostRequest(default_mooc_url + url, data=data, **kwargs)

def makeGetRequest(url, **kwargs):
    return __makeGetRequest(default_mooc_url + url, **kwargs)

def makePutRequest(url, data=None, **kwargs):
    return __makePutRequest(default_mooc_url + url, data=data, **kwargs)

def makeDeleteRequest(url, **kwargs):
    return __makeDeleteRequest(default_mooc_url + url, **kwargs)


def getMoocList():
    return mooc_map

# Get course list from default mooc or from mooc with moocId
def getCourseList(teamName=None):
    if teamName == None:
        return makeGetRequest("course/list")
    else:
        if mooc_map[teamName] == None:
            return makeGetRequest("course/list")
        else:
            return __makeGetRequest(mooc_map[teamName] + "course/list")

def getCategory(categoryId):
    mooc_url = __getMoocUrl(categoryId)
    return __makeGetRequest(mooc_url + "category/"+categoryId)

# Get category list from default mooc or from mooc with moocId
def getCategoryList(teamName=None):
    if teamName == None:
        return makeGetRequest("category/list")
    else:
        if mooc_map[teamName] == None:
            return makeGetRequest("category/list")
        else:
            return __makeGetRequest(mooc_map[teamName] + "category/list")


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



def __getMoocUrl(objectId):
    if objectId==None:
        return default_mooc_url
    if mooc_map == None:
        __generateMoocMap()
    moocId = __getMoocIdFromId(objectId)
    if mooc_map[moocId]==None:
        return default_mooc_url
    else:
        return mooc_map[moocId]

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