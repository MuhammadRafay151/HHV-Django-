from django import forms


class Product(forms.Form):
    PName = forms.CharField()
    Design = forms.NumberInput()
    NPieces = forms.NumberInput
    Qstock = forms.NumberInput
    Price = forms.FloatField()
    color = forms.NumberInput()
    KFabric = forms.NumberInput()
    SFabric = forms.NumberInput()
    DFabric = forms.NumberInput()
    IsKameezFront = forms.BooleanField()
    IsKameezBack = forms.BooleanField()
    IsDupatta = forms.BooleanField()
    IsShalwar = forms.BooleanField()

class TestForm(forms.Form):
    text= forms.CharField(label="INPUT",max_length=50)

