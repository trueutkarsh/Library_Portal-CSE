from django import forms

class reqtoissueform(forms.Form):
	#bookresult=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Select books which you want to issue.")
	def __init__(self,requestlogs,*args, **kwargs):
		super(reqtoissueform, self).__init__(*args, **kwargs)
		self.fields['requestlog']=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[(x.id,x) for x in requestlogs])

class issuetoreturnform(forms.Form):
	#bookresult=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Select books which you want to issue.")
	def __init__(self,issuelogs,*args, **kwargs):
		super(issuetoreturnform, self).__init__(*args, **kwargs)
		self.fields['issuelog']=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[(x.id,x) for x in issuelogs])		