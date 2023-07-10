from django.shortcuts import render
from .models import Category, Store

def home(request):
    categories = Category.objects.all()
    return render(request, "home.html", {'categories': categories})


def category_page(request, slug):
    category = Category.objects.filter(slug=slug).first()
    stores = category.store_set.all()
    return render(request, "category.html", {'category': category, 'stores': stores})


def search(request):
    if request.method == 'POST':
        search_item = request.POST['search_item']
        stores = Store.objects.filter(name__contains=search_item)
    else: 
        search_item = "Not defined"
        stores = []
    return render(request, "search.html", {'search_item': search_item, 'stores': stores})
