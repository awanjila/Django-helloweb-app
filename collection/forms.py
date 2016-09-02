from django import forms
from django.forms import ModelForm
from collection.models import Thing

class ThingForm(ModelForm):
	class Meta:
		model=Thing
		fields =('name', 'description',)
class ContactForm(forms.Form):
	contact_name= forms.CharField()
	contact_email = forms.EmailField()
	content=forms.CharField(widget=forms.Textarea)