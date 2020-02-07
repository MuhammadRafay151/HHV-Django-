from django import forms
class Login(forms.Form):
    UserName=forms.CharField(max_length=30)
    Password=forms.CharField(max_length=50)
#,widget=forms.TextInput(attrs={'class': 'form-control'})
#add classes to widget
class Signup(forms.Form):
    Name=forms.CharField(max_length=20)
    Contact=forms.CharField(max_length=12)
    UserName=forms.CharField(max_length=30)
    Password=forms.CharField(max_length=30)
    Image=forms.FileField()