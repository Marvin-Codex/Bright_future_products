from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import OrderForm


def home(request):
    sort_option = request.GET.get('sort', 'latest')
    category_filter = request.GET.get('category')
    
    if sort_option == 'latest':
        products = Product.objects.all().order_by('date_added')
    elif sort_option == 'category':
        if category_filter:
            products = Product.objects.filter(category_id=category_filter)
        else:
            products = Product.objects.all().order_by('category')
    else:
        products = Product.objects.all()
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'sort_option': sort_option,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def make_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'products/make_order.html', {'form': form, 'product': product})

