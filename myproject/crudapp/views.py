from django.shortcuts import render,redirect
from .forms import ProductForm,RegisterForm
from .models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
def index(request):
    return render(request, 'index.html')
#R-read-fetch data from db and display in admin dashboard
@login_required(login_url='login')
@user_passes_test(lambda u:u.is_staff,login_url='login')
def admin(request):
    products = Product.objects.all()
    return render(request, 'admin_dashboard.html', {'products': products})
#create-add data to db using forms
@user_passes_test(lambda u:u.is_staff,login_url='login')
@login_required(login_url='login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm()
    return render(request, 'add_product.html', {'form': form})
#D-elete data from db
@user_passes_test(lambda u:u.is_staff,login_url='login')
@login_required(login_url='login')
def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products')
#U-update data in db
@user_passes_test(lambda u:u.is_staff,login_url='login')
@login_required(login_url='login')
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
        return render(request, 'add_product.html', {'form': form})
#registering user
def register_user(request):
    form=RegisterForm(request.POST)
    if form.is_valid():
        form.save()#save user to db
        return redirect('index')
    else:
        form=RegisterForm()
    return render(request, 'register.html', {'form': form})
def login_user(request):
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if user.is_staff:
                return redirect('products')
            else:
                return redirect('user')
    else:
            form=AuthenticationForm()
    return render(request, 'login.html', {'form':form})
@login_required(login_url='login')
def user_dashboard(request):
    products=Product.objects.all()
    return render(request, 'users/user_dashboard.html',{'products':products})
#logout user
def logout_user(request):
    logout(request)
    return redirect('login')
