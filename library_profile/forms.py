from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LibUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=('username','password1','password2')
    
    def save(self,commit=True):
        user = super(LibUserForm, self).save(commit=False)
        user.email=user.username+"@cse.iitb.ac.in"
        
        if commit:
            user.save()
        return user   

        