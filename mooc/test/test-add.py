from httplib2 import Http

try:
    # For c speedups
    from simplejson import loads, dumps
except ImportError:
    from json import loads, dumps
 
 
def post_dict(url, dictionary):
    '''
    Pass the whole dictionary as a json body to the url.
    Make sure to use a new Http object each time for thread safety.
    '''
    http = Http()
    resp, content = http.request(
        uri=url,
        method='POST',
        headers={'Content-Type': 'application/json; charset=UTF-8'},
        body=dumps(dictionary),
    )
    
 
def main():
    # NOTE you would need to setup a webapp that can accept a json post to test this.
    # Perhaps ill show a quick example in a later post
 
    post_dict(
        url='http://localhost:8080/moo/data',
        dictionary={'username': 'john', 'password': 'gash'}
    )
 
if __name__ == "__main__":
    main()
