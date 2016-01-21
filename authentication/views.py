from django.shortcuts import render, render_to_response, redirect,HttpResponseRedirect
from django.template import RequestContext
from authenticator import ldapAuth
from django.contrib.auth.models import User,UserManager
from django.contrib import  auth
from django.core.urlresolvers import *


# Create your views here.


def authentication(request):
    print("13")
    context = RequestContext(request)
    if request.method == 'POST':
        print("16")
        Username = request.POST["username"]
        Password = request.POST["passwd"]
        authenticate = ldapAuth(request, Username, Password)
        if authenticate=='VALID':
            print("20")
            if User.objects.filter(username=Username).exists() :
                print("user exists")               
                user=User.objects.all().filter(username=Username)
                user=auth.authenticate(username=Username,password='libpassword')
            else:
                print("new user made it")
                new_user=User.objects.create_user( Username, Username+"@cse.iitb.ac.in", 'libpassword')
                profile=new_user.profile
                new_user.save()
                user=auth.authenticate(username=Username,password='libpassword')
            if user and user.is_active :
                print("37")

                auth.login(request, user)
                if request.user.is_authenticated():
                    print(str(request.session.get('username'))+"nice work")
                request.session['username']=Username
                #print(request.GET['next'])
                return redirect('/search/')
            else:
                print("error authentication") 
            return render_to_response('authentication/index.html', {'logged': 4,'ecomment':"worong username or password"}, context)   
            print("36")
             
        else:
            return render_to_response('authentication/index.html', {'logged': 4,'ecomment':"worong username or password"}, context)
    else:       
        return render_to_response('authentication/index.html', {'logged': 4}, context)




def index(request):
    context = RequestContext(request)
    #username = request.session.get('username')
    if request.user.is_authenticated():
        #request.session['username']=request.user.username
        userType = request.session.get('userType')
        if userType == 'f':
            return redirect('/search/')
        else:
            return redirect('/search/')
    #return render_to_response('authentication/index.html', {'logged': 4}, context)
    print("75")
    return redirect('/login/')

def logout(request):
    request.session.flush()
    auth.logout(request)
    return redirect("/login/")