from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from authenticator import ldapAuth
from django.contrib.auth.models import User,UserManager
from django.contrib import  auth



# Create your views here.


def authentication(request):
    context = RequestContext(request)
    if request.method == 'POST':
        Username = request.REQUEST["username"]
        Password = request.REQUEST["passwd"]
        
        authenticate = ldapAuth(request, Username, Password)
        if authenticate=='VALID':
            #user=auth.authenticate(username=Username)
            if User.objects.filter(username=Username).exists() :
                print("user exits")
                user=User.objects.all().filter(username=Username)
                print(user)
                return redirect('/search')
            else:
                new_user=User.objects.create_user( Username, Username+"@cse.iitb.ac.in", None)
                profile=new_user.profile
                new_user.save()
                user=auth.authenticate(username=Username)
                print(user)
                return redirect('/search')
        else:
            return redirect('authentication.views.index')
        '''
        if user is not None:
            profile=user.profile
            return redirect('/search')
        elif not User.objects.filter(username=Username).exists() :
            #user does not exists   
            
            
            if authenticate == 'VALID':
                #user is a cse user make him register
                return redirect('/register')
            else:
                return render_to_response('authentication/index.html', {'logged': False}, context)
        else:
            
            return render_to_response('authentication/index.html', {'logged': False}, context)
         '''    
    else:
        #ask dheeru why this one
        return redirect('authentication.views.index')




def index(request):
    context = RequestContext(request)
    username = request.session.get('username')
    if username is not None:
        userType = request.session.get('userType')
        if userType == 'f':
            return redirect('/search')
        else:
            return redirect('/search')
    return render_to_response('authentication/index.html', {'logged': 4}, context)

def logout(request):
    request.session.flush()
    return redirect("/")