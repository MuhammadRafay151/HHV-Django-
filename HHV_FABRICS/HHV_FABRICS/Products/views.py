from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .test import database
from .Forms import TestForm


# from DB import test

# Create your views here.

def ViewProduct(request):
    t1 = database()
    Querry='''select Product.[Product Name],Designs.DesignName ,Product.[Number Of Pieces]
,Product.[Quantity in Stock],Product.[Product Price],Color.color
,x.Fabric,y.Fabric,Fabric.Fabric,Product.IsKameezFrontEmbroided,Product.IsKameezBackEmbroided
,Product.IsDupattaEmbroided,Product.IsShalwarEmbroided from Product inner join color on Color.id=Product.Color 
inner join Designs on Product.[Design Code]=Designs.DesignCode
inner join 
Fabric  on Fabric.id=Product.[Dupatta Fabric]inner join 
Fabric as x on x.id=Product.[Kameez Fabric]inner join 
Fabric as y on y.id=Product.[Shalwar Fabric]'''
    products = t1.read(Querry)
    return render(request, 'Products/ViewProducts.html',{'Products':products})


def AddProducts(request):
    t1 = database()
    color = t1.read("select * from color")
    fabrics = t1.read("select * from fabric")
    Designs = t1.read("select * from designs")
    return render(request, 'Products/AddProducts.html', {'data': color, 'fabric': fabrics, 'Designs': Designs})


def SubmitProduct(request):
    if request.method == 'POST':
        # form = Product(request.POST)
        PName = request.POST.get('PName')
        Design = request.POST.get('Design')
        NPieces = request.POST.get('NPieces')
        Qstock = request.POST.get('Qstock')
        Price = request.POST.get('Price')
        color = request.POST.get('color')
        KFabric = request.POST.get('KFabric')
        SFabric = request.POST.get('SFabric')
        DFabric = request.POST.get('DFabric')
        IsKameezFront = bool(request.POST.get('IsKameezFront', False))
        IsKameezBack = bool(request.POST.get('IsKameezBack', False))
        IsDupatta = bool(request.POST.get('IsDupatta', False))
        IsShalwar = bool(request.POST.get('IsShalwar', False))
        t1 = database()
        querry='''insert into Product([Product Name],[Design Code],[Number Of Pieces]
,[Quantity in Stock],[Product Price],Color,[Kameez Fabric],[Shalwar Fabric],
[Dupatta Fabric],IsKameezFrontEmbroided,IsKameezBackEmbroided
,IsDupattaEmbroided,IsShalwarEmbroided
) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(PName,Design,NPieces,Qstock,Price,color,KFabric,SFabric,DFabric,IsKameezFront
  ,IsKameezBack,IsDupatta,IsShalwar)
        t1.Insert(querry)
        return HttpResponseRedirect('/Products/AddProducts')


    else:
        return HttpResponseRedirect('/Products/AddProducts')


def check(request):
    t1 = database()
    data = t1.read("select * from employee")
    return HttpResponse(data[0][0])

def Form(request):
    if request.method=='POST':
        fm=TestForm(request.POST)
        if fm.is_valid():
            return HttpResponse(fm.cleaned_data['text'])
    fm=TestForm()
    return render(request,'Products/form.html',{'form':fm})
