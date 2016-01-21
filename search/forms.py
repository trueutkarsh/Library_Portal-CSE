#define all forms here
from django import forms

def returnchoices(books):
	pass


class searchform(forms.Form):
	book_name=forms.CharField(max_length=30,required=False)
	author_name=forms.CharField(required=False)
	publisher_name=forms.CharField(required=False)
	
class issueform(forms.Form):
	#bookresult=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Select books which you want to issue.")
	def __init__(self,books,*args, **kwargs):
		super(issueform, self).__init__(*args, **kwargs)
		self.fields['bookresult']=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[(x.id,x) for x in books])
			