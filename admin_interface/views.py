#write views here to show both requestlog and issue log
# Create your views here.
from django.shortcuts import render, render_to_response,redirect
from django.http import  HttpResponse
from django.shortcuts import render
from admin_interface.models import *
from admin_interface.forms import * 
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
# Create your views here.


def reqtoissue(request):

    if request.method=='POST':
        reqlogs=reqtoissueform(RequestLog.objects.all())
        args={}
        args['form']=reqlogs
        args.update(csrf(request))
        return render(request, 'admin/log/reqtoissue.html',args)
    else:
        return redirect('/admin/')  

def reqtoissueconfirm(request):

    if request.method=='POST':
  
        requestlogs=request.POST.getlist('requestlog')  
        booksissued=[]
        booksnotissued=[] 
        print("books below") 
        if  requestlog :
            for req in requestlogs:
                log=RequestLog.objects.all().get(pk=req)
                if IssuedLog.addtolog(log) :
                    booksissued.add(log)
                else:
                    booksnotissued.add(log)

            args={}
            args.update(csrf(request))
            args['booksissued']=booksissued
            args['booksnotissued']=booksnotissued 
            return render(request,'admin/log/reqtoissueconfirm.html',args)      
        else:
            print("no books to issue")
            return redirect('/admin/itor/')     
    else:
        return redirect('/admin/')  



def reqtoissuedone(request):

    if request.method=="POST":
        booksissued=request.POST.getlist('booksissued')
        args={}
        args.update(csrf(request))
        args['booksissued']=booksissued     
        return render(request,'admin/log/reqtoissuedone.html',args)
    else :
        return redirect('/admin/')
            



def issuetoreturn(request):

    if request.method=='POST':
        issuelogs=issuetoreturnform(IssuedLog.objects.all())
        args={}
        args['form']=issuelogs
        args.update(csrf(request))
        return render(request, 'admin/log/issuelog.html',args)
    else:
        return redirect('/admin/')

def issuetoreturnconfirm(request):

    if request.method=='POST':
        issuelogs=request.POST.getlist('issuelog')  
        booksreturned=[]
        booksnotreturned=[] 
        if  requestlog :
            for req in issuelogs:
                log=IssuedLog.objects.all().get(pk=req)
                if IssuedLog.returnit(log) :
                    booksreturned.add(log)
                else:
                    booksnotreturned.add(log)

            args={}
            args.update(csrf(request))
            args['booksreturned']=booksreturned
            args['booksnotreturned']=booksnotreturned 
            return render(request,'admin/log/issuetoreturnconfirm.html',args)       
        else:
            print("no books to issue")
            return redirect('/admin/itor/')     
    else:
        return redirect('/admin/')  

def issuetoreturndone(request):
    if request.method=="POST":
        booksreturned=request.POST.getlist('booksissued')
        args={}
        args.update(csrf(request))
        args['booksissued']=booksissued     
        return render(request,'admin/log/issuetoreturndone.html',args)
    else :
        return redirect('/admin/')