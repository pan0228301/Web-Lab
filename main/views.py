from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.models import User
from main import forms
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib import auth

def index(request):
  if request.method == 'POST':
     login_form = forms.UserForm(request.POST)
     login_name = request.POST['username'].strip()
     login_password = request.POST['password']
     user = authenticate(username=login_name, password=login_password)
     if user is not None:
        if user.is_active:
           auth.login(request,user)
           print("Success!")
        else:
           print("Not active")
     else:
        print("login Faild")
  else:
     login_form = forms.UserForm()
     user = None
  template = get_template('index.html')
  html = template.render(context=locals(), request=request)
  return HttpResponse(html)

def logout(request):
    auth.logout(request)
    return redirect('/')

def content(request, content_id):
  template = get_template('content.html')
  html = template.render()

  return HttpResponse(html)


def run(request, lab_id):
  template = get_template('running.html')
 
  html = template.render()

  return HttpResponse(html)
