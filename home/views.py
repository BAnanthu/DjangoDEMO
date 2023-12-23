from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
from home.models import Product


@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='signin')
def add_product(request):
    if request.method == "GET":
        return render(request, 'add_product_form.html')
    elif request.method == "POST":
        product_name = request.POST.get("name")
        product_description = request.POST.get("description")
        product_price = request.POST.get("price")
        product_category = request.POST.get("category")
        product_in_stock = request.POST.get("in_stock")
        product_image = request.FILES.get('image')

        product_obj = Product(name=product_name, description=product_description,
                              price=product_price, category=product_category,
                              in_stock=product_in_stock, image=product_image)
        product_obj.save()
        return render(request, 'add_product_form.html')
