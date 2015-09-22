from django.shortcuts import render, render_to_response
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import  auth
from authentication.authenticator import ldapAuth
from forms import LibUserForm
from library_profile.forms import LibUserForm
from django.contrib.redirects.models import Redirect
from django.core.context_processors import csrf

# Create your views here.
def registerlibuser(request):
    
    if request.method=='POST':
        form=LibUserForm(request.POST)
        if form.is_valid() :
            print("valid fine")
            authenticate = ldapAuth(request, form.cleaned_data['username'], form.cleaned_data['password1'])
           
            print("valid fine")
            print(authenticate)
            if authenticate=='VALID':
                #register new user
                form.save()
                print("form saved moving out")
                print("formsaved")
                return redirect('/')
                
    #form=LibUserForm()
    args={}
    args.update(csrf(request))
    args['form']=LibUserForm()
    return render_to_response('register/register.html',args)
                
        
    