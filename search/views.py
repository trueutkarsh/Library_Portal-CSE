# Create your views here.
from django.shortcuts import render, render_to_response,redirect
from django.http import  HttpResponse
from django.shortcuts import render
from admin_interface.models import Book,Publisher,Author,Course,Research_paper
from search.forms import searchform,issueform
from django.db.models import Q
from django.contrib import  auth
from django.contrib.auth.models import User,UserManager
from authentication.authenticator import ldapAuth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.conf.global_settings import LOGIN_URL
# Create your views here.
def searchit(request):
    
    errors=[]
    form=searchform()

    if request.method == 'POST' :
        

            form = searchform(request.POST)
            #message = 'You searched for: %r' % request.GET['book_name']
            #the search engine can be changed in futre to make it more specific
            # examples if onty author has been put give all books by that author
            #similar for publisher
            if form.is_valid():
                book_search=form.cleaned_data['book_name']
                author_search=form.cleaned_data['author_name']
                pub_search=form.cleaned_data['publisher_name']
            #print(book_search,author_search,pub_search)
            #in future edit errors here
            #change here
            
            if book_search!="":
                #empty book name search with authors
                books=Book.objects.all().filter(title__icontains=book_search)
                if author_search!="":
                    books.filter(Q(authors__last_name__contains=author_search) | Q(authors__first_name__contains=author_search))
                    #if publisher_name
                    if pub_search!="":
                        books.filter(Q(publisher__name__contains=pub_search) )

                else:
                    if pub_search!="":
                        books.filter(Q(publisher__name__contains=pub_search) )
                    else:
                        pass    
            else :
                    
                if author_search !="":
                    books=Book.objects.all().filter(Q(authors__last_name__contains=author_search) | Q(authors__first_name__contains=author_search))
                else:
                    if pub_search!="":
                        books=Book.objects.all().filter(Q(publisher__name__contains=pub_search) )
                    else:
                        errors.append("Please fill atleast one entry")
                
            if not errors:
                print("form made")
                iform=issueform(books)
                #iform.fields['bookresult'].choices=[(x.title) for x in books]
                #print(iform)
                args={}
                args['form']=iform
                args['query']=book_search
                args['loggedin']=False
                args.update(csrf(request))
                if not request.user.is_anonymous():
                    args['loggedin']=True
                    args['username']=request.user.username
                return render(request, 'search/search-results.html',{'form': iform , 'query': book_search,'books':books})
            else:
                return render(request, 'search/base-search.html',{'errors': errors,'form':form})    
    else:
        errors.append('You submitted an empty form')

    return render(request, 'search/base-search.html',{'errors': errors,'form':form})

#new fuctio  
@login_required 
def issuebook(request):

    if request.method == 'POST':
        print("85-her")
        
       
        user=User.objects.all().get(username=request.session['username']) 
            #redirect them to login page
        print("89")
            
        '''
        Username = request.REQUEST["username"]
        Password = request.REQUEST["passwd"]
    
        authenticate = ldapAuth(request, Username, Password)
        if authenticate=='VALID':
            if not User.objects.filter(username=Username).exists() : 
                user=User.objects.create_user( Username, Username+"@cse.iitb.ac.in", 'libpassword')
                user.save()
                #user=User.objects.all().get(username = Username)
                  
        else:
            return render_to_response('search/search-results.html', {'ecomments':'Sorry,Wrong username or password','loggedin':False})
        
        user=auth.authenticate(username=Username,password='libpassword')              
        auth.login(request, user)
        request.session['user']=user   
    '''    
    
        #    user=request.user                     
        profile=user.profile   
        bookstoissue=request.POST.getlist('bookresult')   
        print("books below") 
        print(bookstoissue)        
        if  bookstoissue :
            booksissued=[]
            booksnotissued=[]
            for book in bookstoissue:
                booktoissue=Book.objects.all().get(title=book)
                print(booktoissue)
                if not booktoissue.issued :
                    
                    booktoissue.issued=True
                    booktoissue.issuer=profile
                    booktoissue.save()
                    booksissued.append(booktoissue)
                else:
                    booksnotissued.append(booktoissue)
            args={}
            args['booksissued']=booksissued
            args['booksnotissued']=booksnotissued
            args['username']=user.username
            args['loggedin']=True
            print(args)
            return render(request,'search/issue.html',args)                        
        else:
            print("no books to issue")
            return redirect('/')
   
    else:
        #ask dheeru why this one
        print("118")
        return redirect('/')
        
    
    
