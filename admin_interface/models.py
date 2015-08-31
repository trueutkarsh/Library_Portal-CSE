from django.db import models

# Create your models here.


class Author(models.Model):#author can be of both books or rearchpaper
	first_name=models.CharField(max_length=30)#max len can be changed
	last_name=models.CharField(max_length=40)
	website=models.URLField(blank=True)#empty values means no website
	#books=models.ManyToManyField(Book,null=True)
	#researchpaper=models.ManytoManyField(Research_paper,null=True)
	

	def __unicode__(self):
		return (self.first_name +" "+ self.last_name)

class Publisher(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=20)
	state=models.CharField(max_length=20,null=True)
	country=models.CharField(max_length=40)
	website=models.URLField(blank=True)
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
	website=models.URLField(blank=True)
	edition=models.IntegerField()	
	authors=models.ManyToManyField(Author)
	publisher=models.ManyToManyField(Publisher)
	courses=models.ManyToManyField(Course,blank=True)
   #uid=models.CharField(max_length=10)-to be implemented
   #after deciding how to do it.
   #sections=models.ManyToManyField(Book) 
   
   	def __unicode__(self):
   		return self.title

		



