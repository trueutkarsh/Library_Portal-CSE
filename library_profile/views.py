from django.shortcuts import render, render_to_response
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import  auth
from authentication.authenticator import ldapAuth
from forms import LibUserForm
from django.contrib.auth.decorators import login_required
from library_profile.forms import LibUserForm
from django.core.context_processors import csrf
from admin_interface.models import RequestLog,IssuedLog
from django.db.models import Q


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

    args={}
    args.update(csrf(request))
    args['form']=LibUserForm()
    return render_to_response('register/register.html',args)
                
        
@login_required
def myprofile(request):     
    
    if request.user.is_authenticated():
        username=request.user.username
        print(username)
        currentrequests=[]
        currentissued=[]
        currentrequests=RequestLog.objects.all().filter(Q(user__user__username=username))
        currentissued=IssuedLog.objects.all().filter(Q(user__user__username=username))
        args={}
        args['currentissued']=currentissued
        args['currentrequests']=currentrequests
        args['title']="Your Active Library Records"
        print("myprofile",args)
        return render(request,'profile/profile.html',args)
    else:
        redirect('/')    

@login_required
def reqdeleteconfirm(request):
    if request.method=='POST':
        deletereqs=request.POST.getlist('requestedbooks[]')
        bookstodelete=[]
        booksnotdeleted=[]
        if deletereqs :
            for req in deletereqs:
                log=RequestLog.objects.all().get(pk=req)
                if RequestLog.returnit(log) :
                    bookstodelete.append(log)
                else:
                    booksnotdeleted.append(log)

            args={}
            args.update(csrf(request))
            args['bookstodelete']=bookstodelete
            args['booksnotdeleted']=booksnotdeleted
            args['title']="Confirm Return"
            print(args)
            return render(request,'profile/reqtodeleteconfirm.html',args)
        else:
            print("no books to return")
            return redirect('/profile/')
    else:
        return redirect('/')

@login_required
def reqdeletdone(request):
    if request.method=='POST':
        deletereqs=request.POST.getlist('deletereqs[]')
        booksdeleted=[]
        booksnotdeleted=[]
        if deletereqs :
            for req in deletereqs:
                log=RequestLog.objects.all().get(pk=req)
                if RequestLog.returnit(log,False) :
                    booksdeleted.append(log)
                else:
                    booksnotdeleted.append(log)

            args={}
            args.update(csrf(request))
            args['requestsdeleted']=booksdeleted
            args['booksnotdeleted']=booksnotdeleted
            args['title']="Confirm Return"
            print(args)
            return render(request,'profile/reqtodeletedone.html',args)
        else:
            print("no books to return")
            return redirect('/profile/')
    else:
        return redirect('/')        