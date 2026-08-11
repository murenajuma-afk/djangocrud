from django.shortcuts import render

from .forms import ProductForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def admin(request):
    return render(request, 'admin_dashboard.html')
def add_product(request):
    form=ProductForm()
    return render(request, 'add_product.html', {'form': form})

