#define all forms here
from django import forms


class searchform(forms.Form):
	book_name=forms.CharField(max_length=30,required=False)
	author_name=forms.CharField(required=False)
	publisher_name=forms.CharField(required=False)