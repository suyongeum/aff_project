from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import Product
from .forms import SelectionForm
from django.http import HttpResponse

#Create your views here.

items_in_page = 24

def index(request):
    products_portion, form = which_product(request, 'index')
    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def man(request):
    products_portion, form = which_product(request, 'man')
    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def woman(request):
    products_portion, form = which_product(request, 'woman')
    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def geek(request):
    products_portion, form = which_product(request, 'geek')
    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def kids(request):
    products_portion, form = which_product(request, 'kid')
    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def pet(request):
    products_portion, form = which_product(request, 'pet')
    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def dbupdate(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
        # access DB and add one.
        object = Product.objects.get(pk=id)
        object.clicks += 1
        object.save()
    return HttpResponse('OK')

def which_product(request, which_tag):

    if which_tag is 'index':
        filtered = Product.objects.all()
    if which_tag is 'man':
        filtered = Product.objects.filter(man_tag=True)
    if which_tag is 'woman':
        filtered = Product.objects.filter(woman_tag=True)
    if which_tag is 'geek':
        filtered = Product.objects.filter(geek_tag=True)
    if which_tag is 'kid':
        filtered = Product.objects.filter(kid_tag=True)
    if which_tag is 'pet':
        filtered = Product.objects.filter(pet_tag=True)

    form = SelectionForm(request.POST or None)

    if form.is_valid():
        result = form.cleaned_data['search']
    else:
        result = ''

    if request.method == "GET":
        sort_option = request.GET.get('selection')

        if result:
            if sort_option == 'newest':
                products = filtered.filter(name__icontains=result).order_by('-datetime')
            elif sort_option == 'popular':
                products = filtered.filter(name__icontains=result).order_by('-clicks')
            elif sort_option == 'low_price':
                products = filtered.filter(name__icontains=result).order_by('price')
            elif sort_option == 'high_price':
                products = filtered.filter(name__icontains=result).order_by('-price')
            else:
                products = filtered.filter(name__icontains=result).order_by('-datetime')
        else:
            if sort_option == 'newest':
                products = filtered.order_by('-datetime')
            elif sort_option == 'popular':
                products = filtered.order_by('-clicks')
            elif sort_option == 'low_price':
                products = filtered.order_by('price')
            elif sort_option == 'high_price':
                products = filtered.order_by('-price')
            else:
                products = filtered.order_by('-datetime')
    else:
        products = filtered.order_by('-datetime')

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page

    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return products_portion, form