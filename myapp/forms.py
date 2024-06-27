from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Customer, User

class dateinput(forms.DateInput):
    input_type='date'
class userreg(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password1','password2']
class customerreg(forms.ModelForm):
    dob=forms.DateField(widget=dateinput)
    class Meta:
        model=Customer
        exclude=('user',)



  



