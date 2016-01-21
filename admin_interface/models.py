from django.db import models
from django.template.defaultfilters import default
from library_profile.models import libprofile
from django.db.models.fields.related import OneToOneField
import datetime

# Create your models here.


class Author(models.Model):#author can be of both books or rearchpaper
	first_name=models.CharField(max_length=30)#max len can be changed
	last_name=models.CharField(max_length=40,blank=True,null=True)
	website=models.URLField(null=True,blank=True)#empty values means no website
	#books=models.ManyToManyField(Book,null=True)
	#researchpaper=models.ManytoManyField(Research_paper,null=True)
	

	def __unicode__(self):
		return (self.first_name +" "+ self.last_name)

class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50,blank=True,null=True)
	city=models.CharField(max_length=20,blank=True,null=True)
	state=models.CharField(max_length=20,blank=True,null=True)
	country=models.CharField(max_length=40,blank=True,null=True)
	website=models.URLField(null=True,blank=True)
	#books=models.ManyToManyField(Book)

	def __unicode__(self):
		return self.name


class Course(models.Model):
	id=models.CharField(max_length=5,primary_key=True)
	name=models.CharField(max_length=50)
	#books=models.ManyToManyField(Book)

	def __unicode__(self):
		return	(self.id+self.name)


'''#can be implemented if such data can be collected
class section(models.Model):
	heading=models.CharField(max_length=50)
	#books=models.ManyToManyField(Book)

	def __unicode__(self):
		return heading
'''
class Research_paper(models.Model):
	title=models.CharField(max_length=100)
	authors=models.ManyToManyField(Author)

	def __unicode__(self):
		return self.title

class Book(models.Model):
	title=models.CharField(max_length=100)
	website=models.URLField(null=True,blank=True)
	edition=models.IntegerField(blank=True,null=True)	
	authors=models.ManyToManyField(Author,blank=True,null=True)
	publisher=models.ManyToManyField(Publisher,blank=True,null=True)
	courses=models.ManyToManyField(Course,blank=True)
	state=models.IntegerField(default=1)#1=not requested or booked ,2=requested ,3=booked
	issuer=models.ForeignKey(libprofile,blank=True,null=True,default=None)
   #uid=models.CharField(max_length=10)-to be implemented
   #after deciding how to do it.
   #sections=models.ManyToManyField(Book) 
   
   	def __unicode__(self):
   		return self.title 
   	
   	def issue(self,lib_profile):
   		if lib_profile !=None:			
	   		if self.state==1:
	   		 	self.state=2
	   		  	self.issuer=lib_profile
	   		  	return True
	   	  	else:
	   	  		pass
	   	return False
	   	  		
   	def returnbook(self):
   		self.state=1
   		self.issuer=None
   		
   		
class RequestLog(models.Model):
	book=models.ForeignKey(Book)
	user=models.ForeignKey(libprofile)
	date=models.DateTimeField(auto_now=True)		


		

	def __unicode__(self):
		return self.book.title 
	@staticmethod	
	def addtolog(ibook,userprofile):

		if ibook!=None and userprofile != None :
			if ibook.state==2 and not RequestLog.objects.filter(book=ibook.id).exists():
				ilog=RequestLog(book=ibook,user=userprofile)
				ilog.save()
				return True;

		return False		
	def returnit(self):							
		ibook=Book.objects.get(pk=self.book)
		if ibook!=None :
			if ibook.state==2:
				ibook.state=1
				ibook.save()
				RequestLog.remove(self)
				return True;
		return False		


class IssuedLog(models.Model): # this will have log of all the books
	book=models.ForeignKey(Book)
	user=models.ForeignKey(libprofile)
	date=models.DateTimeField(auto_now=True)	



	def __unicode__(self):
		return self.book.title 

	def __init__():
		pass
	@staticmethod	
	def addtolog(rlog):
		ibook=Book.objects.get(pk=rlog.book)
		if ibook!=None :
			if ibook.state==3 and not IssuedLog.objects.filter(book=bookid).exists():
				ilog=IssuedLog(book=rlog.book,user=rlog.user)
				ilog.save()				
				RequestLog.remove(rlog)
				return True
		return False;
				
	def returnit(self):							
		ibook=Book.objects.get(pk=self.book)
		if ibook!=None :
			if ibook.state==3:
				ibook.state=1
				ibook.save()
				RequestLog.remove(self)				



