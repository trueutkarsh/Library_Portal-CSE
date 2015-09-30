from django.shortcuts import render, render_to_response, redirect,HttpResponseRedirect
from django.template import RequestContext
from authenticator import ldapAuth
from django.contrib.auth.models import User,UserManager
from django.contrib import  auth



# Create your views here.


def authentication(request):
    print("13")
    context = RequestContext(request)
    if request.method == 'POST':
        print("16")
        Username = request.REQUEST["username"]
        Password = request.REQUEST["passwd"]
        
        authenticate = ldapAuth(request, Username, Password)
        if authenticate=='VALID':
            print("20")
            #user=auth.authenticate(username=Username)
            if User.objects.filter(username=Username).exists() :
                print("user exists")
                user=User.objects.all().filter(username=Username)
                user=auth.authenticate(username=Username,password='utg@IITB2014')
                #auth.login(request, user);
                #print(user)
                #return redirect('/')
            else:
                print("new user made it")
                new_user=User.objects.create_user( Username, Username+"@cse.iitb.ac.in", 'libpassword')
                profile=new_user.profile
                new_user.save()
                user=auth.authenticate(username=Username,password='utg@IITB2014')
                #user=User.objects.all().filter(username=Username)
            if user and user.is_active : 
                print("37")
                auth.login(request,user)
                if request.POST.get("next") is not "":
                    print("42")
                    if request.POST.get("next") is not "login":   
                        print(request.POST.get("next"))
                        return HttpResponseRedirect(request.POST.get("next"))
                        
               
                print("45")
                return redirect('/')
                #print(user)
                  
            else:
                print("error authentication")    
            print("36")
             
            #request.session['user']=user 
            # print(request.GET['user'],"next url")
            '''
            try:
                #print("next")
                return redirect(request.GET['next'])
                
            except:
                print("default")
                return redirect('/')
            '''   
        else:
            #return redirect('authentication.views.index')
            return render_to_response('authentication/index.html', {'logged': 4}, context)
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
        return render_to_response('authentication/index.html', {'logged': 4}, context)




def index(request):
    context = RequestContext(request)
    username = request.session.get('username')
    if username is not None:
        userType = request.session.get('userType')
        if userType == 'f':
            return redirect('/')
        else:
            return redirect('/')
    #return render_to_response('authentication/index.html', {'logged': 4}, context)
    print("75")
    return redirect('/login')

def logout(request):
    request.session.flush()
    auth.logout(request)
    return redirect("/")