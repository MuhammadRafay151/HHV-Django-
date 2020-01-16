from django import forms


class Product(forms.Form):
    PName = forms.CharField()
    Design = forms.IntegerField()
    NPieces = forms.IntegerField()
    Qstock = forms.IntegerField()
    Price = forms.FloatField()
    color = forms.IntegerField()
    KFabric = forms.IntegerField()
    SFabric = forms.IntegerField()
    DFabric = forms.IntegerField()
    IsKameezFront = forms.BooleanField(required=False,initial=False)
    IsKameezBack = forms.BooleanField(required=False,initial=False)
    IsDupatta = forms.BooleanField(required=False,initial=False)
    IsShalwar = forms.BooleanField(required=False,initial=False)
    Image=forms.FileField()

class TestForm(forms.Form):
    text= forms.CharField(label="INPUT",max_length=50)

