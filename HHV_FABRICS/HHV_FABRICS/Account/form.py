from django import forms
class Login(forms.Form):
    UserName=forms.CharField(max_length=30)
    Password=forms.CharField(max_length=50)
#,widget=forms.TextInput(attrs={'class': 'form-control'})
#add classes to widget