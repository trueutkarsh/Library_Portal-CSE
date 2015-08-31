# Create your views here.
from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
from admin_interface.models import Book,Publisher,Author,Course,Research_paper
from search.forms import searchform
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
	        books =Book.objects.filter(title__icontains=book_search)

		if not errors:
			return render(request, 'search-results.html',{'books': books, 'query': book_search})
		else:
			pass	
	else:
		errors.append('You submitted an empty form')

	return render(request, 'base-search.html',{'errors': errors,'form':form})