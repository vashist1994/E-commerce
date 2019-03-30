from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Product
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegistration , userUpdateForm, profileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = Product.objects.all()
    # print(products.category)
    params = {'products': products}
    print(params)
    print(type(products))
   
    return render(request,'shop/index.html',params)

def shopCategory(request):
    # return HttpResponse("we are at shop category")
    return render(request, "shop/category.html")

def prodctDetails(request):
    return render(request, "shop/single-product.html")

@login_required
def prodctCheckout(request):
    return render(request, "shop/checkout.html")
@login_required   
def shopingCart(request):
    return render(request, "shop/cart.html")
    


def confirmation(request):
    return render(request, "shop/confirmation.html")
    # return HttpResponse("we are at confirmation")


def contact(request):
    return render(request, "shop/contact.html")
    # return HttpResponse("we are at contact")

def login(request):
    return render(request, "shop/login.html")
    # return HttpResponse("we are at login")

def tracker(request):
    return render(request, "shop/tracking.html")
    # return HttpResponse("we are at tracker")

# def checkout(request):
    # return HttpResponse("we are at checkout")
def register(request):
    if request.method == 'POST':
        form = userRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to shop with us')
            return redirect('/shop/login')

    else:
       form = userRegistration() 
    return render(request, 'shop/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('/shop/profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile) 
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'shop/profile.html', context)

