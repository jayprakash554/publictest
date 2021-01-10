from django import forms
from .models import Myupload
class Profile_Form(forms.ModelForm):
	class Meta:
		model = Myupload
		fields = ['username','picture']
        