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
        if request.method=="GET":
            reqlogs=RequestLog.objects.all()
            args={}
            args['requests']=reqlogs
            #args['form']=RequestLog.objects.all()
            args['title']="All the currrent requests"
            args.update(csrf(request))
            print(args)
            return render(request, 'admin/log/requestslog.html',args)
        else:
            return redirect('/admin/')

def reqtoissueconfirm(request):
    print("hell")
    if request.method=="POST":
        requestlogs=request.POST.getlist('requestlog[]')
        booksissued=[]
        booksnotissued=[]
        print("books below",requestlogs)
        
        if  requestlogs :
            for req in requestlogs:
                log=RequestLog.objects.all().get(pk=req)
                if IssuedLog.addtolog(log) :
                    booksissued.append(log)
                else:
                    booksnotissued.append(log)

            args={}
            args.update(csrf(request))
            args['booksissued']=booksissued
            args['booksnotissued']=booksnotissued
            args['title']="Confirm Issue"
            print(args)
            return render(request,'admin/log/reqtoissueconfirm.html',args)
        else:
            print("no books to issue")
            return redirect('/admin/rtoi/')
    else:
        print("hola")
        return redirect('/admin/')



def reqtoissuedone(request):

    if request.method=="POST":
        booksconfirmed=request.POST.getlist('booksconfirmed[]')
        print(booksconfirmed)
        booksissued=[]
        booksnotissued=[]
        if booksconfirmed :
            for req in booksconfirmed:
                log=RequestLog.objects.all().get(pk=req)

                if IssuedLog.addtolog(log,False) : #save it
                    booksissued.append(log)
                else:
                    print("Some error occured")
                    booksnotissued.append(log)   


        args={}
        args.update(csrf(request))
        args['booksissued']=booksissued
        args['booksnotissued']=booksnotissued
        args['title']="Issued"

        return render(request,'admin/log/reqtoissuedone.html',args)
    else :
        return redirect('/admin/')




def issuetoreturn(request):

    if request.method=='GET':
        issuelogs=IssuedLog.objects.all()
        args={}
        args['requests']=issuelogs
        args['title']="Books to be returned"
        args.update(csrf(request))
        print(args)
        return render(request, 'admin/log/issuelog.html',args)
    else:
        return redirect('/admin/')

def issuetoreturnconfirm(request):

    if request.method=='POST':
        issuelogs=request.POST.getlist('issuelog[]')
        booksreturned=[]
        booksnotreturned=[]
        if  issuelogs :
            for req in issuelogs:
                log=IssuedLog.objects.all().get(pk=req)
                if IssuedLog.returnit(log) :
                    booksreturned.append(log)
                else:
                    booksnotreturned.append(log)

            args={}
            args.update(csrf(request))
            args['booksreturned']=booksreturned
            args['booksnotreturned']=booksnotreturned
            args['title']="Confirm Return"

            return render(request,'admin/log/issuetoreturnconfirm.html',args)
        else:
            print("no books to issue")
            return redirect('/admin/itor/')
    else:
        return redirect('/admin/')

def issuetoreturndone(request):
    if request.method=="POST":
        booksconfirmed=request.POST.getlist('booksconfirmed[]')
        booksreturned=[]
        booksnotreturned=[]

        if booksconfirmed :
            for req in booksconfirmed:
                log=IssuedLog.objects.all().get(pk=req)
                if IssuedLog.returnit(log,False) : #remove it
                    booksreturned.append(log)
                else:
                    print("Some error occured")
                    booksnotreturned.append(log)   

        args={}
        args.update(csrf(request))
        args['title']="Return Done"
        args['booksreturned']=booksreturned
        args['booksnotreturned']=booksnotreturned
        print('admin/log/issuetoreturndone.html',args)
        return render(request,'admin/log/issuetoreturndone.html',args)
    else :
        return redirect('/admin/')
