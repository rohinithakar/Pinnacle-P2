# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from djangobottle.app1.forms import ContactForm
from djangobottle.app1.LoginForm import LoginForm
from djangobottle.app1.createUserForm import createUserForm
from djangobottle.app1.updateUserForm import updateUserForm
from bottle import route
from json import loads, dumps
import requests
import json


def index(request):
    #return HttpResponse("Index Page")
    ctx = {}
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))


def about(request):
    r = {'msg': 'fail'}


    #r = requests.get("http://localhost:8080/moo/data/a@a.com")
    #r1 = requests.delete()
    #r2 = requests.put()
    #r3 = requests.post()

    ctx = {'login_form': login_form}
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))


def signIn(request):

    error_status = False
    login_status = False
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            request.session["contact_sent"] = True
            login_form_data = {'email': username, 'pwd': password}
            r = requests.post("http://localhost:8080/auth", data=json.dumps(login_form_data))
            code = r.status_code
            if code == 200:
                login_status = True
                ctx = {'data': r.json(), 'error_status': error_status, 'login_status': login_status, 'username': username}
                return render_to_response('index.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'login_form': login_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('login.html', ctx, context_instance=RequestContext(request))
            elif code == 401:
                error_status = True
                ctx = {'login_form': login_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('login.html', ctx, context_instance=RequestContext(request))

    else:

        login_form = LoginForm()

    ctx = {'login_form': login_form, 'error_status': error_status}
    return render_to_response('login.html', ctx, context_instance=RequestContext(request))


def createUser(request):

    error_status = False
    login_status = False
    createUser_status = False
    if request.method == "POST":
        createUser_form = createUserForm(request.POST)
        if createUser_form.is_valid():
            email = createUser_form.cleaned_data['email']
            password = createUser_form.cleaned_data['password']
            fname = createUser_form.cleaned_data['fname']
            lname = createUser_form.cleaned_data['lname']
            request.session["contact_sent"] = True
            createUser_form_data = {'email': email, 'pwd': password, 'fname': fname, 'lname': lname}
            r = requests.post("http://localhost:8080/user", data=json.dumps(createUser_form_data))
            code = r.status_code
            if code == 201:
                login_status = False
                createUser_status = True
                ctx = {'data': r.json(), 'error_status': error_status, 'createUser_status': createUser_status, 'login_status': login_status}
                return render_to_response('index.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'createUser_form': createUser_form, 'error_status': error_status, 'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))
            elif code == 409:
                error_status = True
                ctx = {'createUser_form': createUser_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))

    else:

        createUser_form = createUserForm()

    ctx = {'createUser_form': createUser_form, 'error_status': error_status}
    return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))


def updateUser(request, username):

    error_status = False
    updateUser_status = False
    if request.method == "POST":
        createUser_form = createUserForm(request.POST)
        if createUser_form.is_valid():
            email = createUser_form.cleaned_data['email']
            password = createUser_form.cleaned_data['password']
            fname = createUser_form.cleaned_data['fname']
            lname = createUser_form.cleaned_data['lname']
            request.session["contact_sent"] = True
            createUser_form_data = {'email': email, 'pwd': password, 'fname': fname, 'lname': lname}
            r = requests.post("http://localhost:8080/user", data=json.dumps(createUser_form_data))
            code = r.status_code
            if code == 201:
                createUser_status = True
                ctx = {'data': r.json(), 'error_status': error_status, 'createUser_status': createUser_status, 'login_status': login_status}
                return render_to_response('index.html', ctx, context_instance=RequestContext(request))
            elif code == 500:
                error_status = True
                ctx = {'createUser_form': createUser_form, 'error_status': error_status, 'error': 'Internal Error Occurs. Please try after sometime.'}
                return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))
            elif code == 409:
                error_status = True
                ctx = {'createUser_form': createUser_form, 'error_status': error_status, 'error': r.json()}
                return render_to_response('createUser.html', ctx, context_instance=RequestContext(request))

    else:
        r = requests.get("http://localhost:8080/user/" % username)
        data = r.json()
        print 'email from data.json()'+data.email
        print data.pwd
        print data.fName
        print data.lName

        email = data.email
        password = data.pwd
        fname = data.fName
        lname = data.lName
        user_details = [{'email': email, 'password': password, 'fname': fname, 'lname': lname}]
        updateUser_form = updateUserForm(user_details=user_details)

    ctx = {'updateUser_form': updateUser_form, 'error_status': error_status}
    return render_to_response('updateUser.html', ctx, context_instance=RequestContext(request))



def addCourse(request):

    payload = {'name': 'electrical Engineering', 'Description': 'electrical engineering course', 'createDate': 'DATE', 'status': '0'}
    r = requests.post("http://localhost:8080/course", data=json.dumps(payload))

    ctx = r.json()
    return render_to_response('??.html', ctx, context_instance=RequestContext(request))

def categoryAdd(request):
    payload = {'name' : 'electrical Engineering', 'description' : 'electrical engineering course',
               'createDate' : 'DATE', 'status' : '0'}
    r = requests.post("http://localhost:8080/category", data = json.dumps(payload))
    code = r.status_code
    ctx = {'codevalue': code}
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))

def categoryGet(request):
    r = requests.get("http://localhost:8080/category/3")
    ctx=r.json()
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))

def categoryList(request):
    r = requests.get("http://localhost:8080/category/list")
    ctx=r.json()
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))

def announcementAdd(request):
    payload = {'courseId' : 'PinnacleCourse1', 'title' : 'due date for assignment',
               'description' : 'due date is 15 may 2013', 'postDate' : 'DATE','status' : 0}
    r = requests.post("http://localhost:8080/announcements", data = json.dumps(payload))
    code = r.status_code
    ctx = {'codevalue': code}
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))

def announcementGet(request):
    r = requests.get("http://localhost:8080/announcement/Pinnacleannouncement_1")
    ctx=r.json()
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))

def announcementList(request):
    r = requests.get("http://localhost:8080/announcement/list")
    ctx=r.json()
    return render_to_response('about.html', ctx, context_instance=RequestContext(request))

def contact(request):
    success = False
    email = ""
    title = ""
    text = ""
    contact_sent = request.session.get("contact_sent", False)

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            print "Worked"    #we can write our logic when it does not set to maintain session...
        else:
            print "Does not work"    #Also write logic here--Ab

        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']

            request.session["contact_sent"] = True

    else:
        contact_form = ContactForm()

    ctx = {'contact_form': contact_form, "contact_sent": contact_sent, 'email': email, 'title': title, 'text': text,
           'success': success}

    request.session.set_test_cookie()

    return render_to_response('contact.html', ctx, context_instance=RequestContext(request))


def archive(request):
    ctx = {}
    return render_to_response('archive.html', ctx, context_instance=RequestContext(request))


def logout(request):
    error_status = False
    login_status = False
    ctx = {'error_status': error_status, 'login_status': login_status}
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))


@login_required
def profile(request):
    ctx = {}
    return render_to_response('profile.html', ctx, context_instance=RequestContext(request))

