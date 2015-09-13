# Create your views here.
from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
from admin_interface.models import Book,Publisher,Author,Course,Research_paper
from search.forms import searchform
from django.db.models import Q
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
	        print(book_search,author_search,pub_search)
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
			return render(request, 'search-results.html',{'books': books, 'query': book_search})
		else:
			return render(request, 'base-search.html',{'errors': errors,'form':form})	
	else:
		errors.append('You submitted an empty form')

	return render(request, 'base-search.html',{'errors': errors,'form':form})