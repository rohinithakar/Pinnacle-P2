import httplib2
h = httplib2.Http(".cahce")
resp, content = h.request("http://localhost:8081/moo/data/john", "GET")
print resp
print content



