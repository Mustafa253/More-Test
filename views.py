from django.shortcuts import render
from .models import PythonType, Product, Review
from .forms import ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')

def getTypes(request):
    types_list=PythonType.objects.all()
    context={'types_list' : types_list }
    return render(request, 'pythonclubapp/types.html', context=context)

def getProducts(request):
    products_list=Product.objects.all()
    return render(request, 'pythonclubapp/products.html',{'products_list' : product_list})

def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    reviewcount=Review.objects.filter(product=id).count()
    reviews=Review.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'pythonclubapp/productdetails.html', context=context)

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'pythonclubapp/newproduct.html', {'form' : form})

def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'TechReviewApp/newreview.html', {'form' : form})


@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'TechReviewApp/newproduct.html', {'form' : form})

@login_required
def newReview(request):
     form=ReviewForm
     if request.method=='POST':
          form=ReviewForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ReviewForm()
     else:
          form=ReviewForm()
     return render(request, 'pythonclubapp/newreview.html', {'form' : form})

def loginMessage(request):
     return render(request, 'pythonclubapp/loginmessage.html'


def logoutMessage(request):
     return render(request, 'pythonclubapp/logoutmessage.html')


    
