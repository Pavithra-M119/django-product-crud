from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

def productInformation(request):
    product=Product.objects.all()
    return render(request,'product.html',{'product':product})

def insertproduct(request):
    form=ProductForm()
    if (request.method=='POST'):
        form=ProductForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('listemp')
    return render(request,'product_form.html',{'form':form})

def deletePage(request, i):
    if request.method == 'POST':
        product = Product.objects.get(productNumber=i)
        product.delete()
        return redirect('listemp')
    return render(request, 'delete.html', {'productNumber': i})



















