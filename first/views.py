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

def which_product(request, menu):

    if menu is 'index':
        filtered = Product.objects.all()
    if menu is 'man':
        filtered = Product.objects.filter(man_tag=True)
    if menu is 'woman':
        filtered = Product.objects.filter(woman_tag=True)
    if menu is 'geek':
        filtered = Product.objects.filter(geek_tag=True)
    if menu is 'kid':
        filtered = Product.objects.filter(kid_tag=True)
    if menu is 'pet':
        filtered = Product.objects.filter(pet_tag=True)

    # Initial form value. Should be here because of CSRF verification
    form = SelectionForm(request.POST or None)
    form.is_valid()

    # Until this point there are three parameters
    # menu: showing which menu is being selected
    # sort_option: showing which option is being selected
    # search_str: showing a string used for searching result

    if request.method == "GET":
        sort_option = request.GET.get('selection')
        products = sort_products(sort_option, filtered)
    else: # request.method == "POST": It is for search option
        sort_option = request.POST.get('selection')
        search_str = request.POST.get('search')
        products = filter_products(sort_option, search_str, filtered)
        # print('menu:', menu)
        # print('sort_option:', sort_option)
        # print('search_str:', search_str)

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page
    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return products_portion, form

def sort_products(sort_option, filtered):
    if sort_option == 'new':
        products = filtered.order_by('-datetime')
    elif sort_option == 'popular':
        products = filtered.order_by('-clicks')
    elif sort_option == 'low_price':
        products = filtered.order_by('price')
    elif sort_option == 'high_price':
        products = filtered.order_by('-price')
    else:
        products = filtered.order_by('-datetime')
    return products

def filter_products(sort_option, search_str, filtered):
    if sort_option == 'new':
        products = filtered.filter(name__icontains=search_str).order_by('-datetime')
    elif sort_option == 'popular':
        products = filtered.filter(name__icontains=search_str).order_by('-clicks')
    elif sort_option == 'low_price':
        products = filtered.filter(name__icontains=search_str).order_by('price')
    elif sort_option == 'high_price':
        products = filtered.filter(name__icontains=search_str).order_by('-price')
    else:
        products = filtered.filter(name__icontains=search_str).order_by('-datetime')

    return products