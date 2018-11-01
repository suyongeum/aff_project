from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import Product
from .forms import SelectionForm

# Create your views here.

items_in_page = 9

def index(request):

    form = SelectionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        sort_option = form.cleaned_data['selection']
        result = form.cleaned_data['search']

        if result:
            products = Product.objects.filter(name__icontains=result)
        else:
            if sort_option == 'newest':
                products = Product.objects.all().order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.all().order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.all().order_by('price')
            else:
                products = Product.objects.all().order_by('-datetime')
    else:
        products = Product.objects.all().order_by('-datetime')

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page
    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def man(request):
    form = SelectionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        sort_option = form.cleaned_data['selection']
        result = form.cleaned_data['search']

        if result:
            if sort_option == 'newest':
                products = Product.objects.filter(man_tag=True).filter(name__icontains=result).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(man_tag=True).filter(name__icontains=result).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(man_tag=True).filter(name__icontains=result).order_by('price')
            else:
                products = Product.objects.filter(man_tag=True).filter(name__icontains=result).order_by('-datetime')
        else:
            if sort_option == 'newest':
                products = Product.objects.filter(man_tag=True).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(man_tag=True).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(man_tag=True).order_by('price')
            else:
                products = Product.objects.filter(man_tag=True).order_by('-datetime')
    else:
        products = Product.objects.filter(man_tag=True).order_by('-datetime')

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page
    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def woman(request):
    form = SelectionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        sort_option = form.cleaned_data['selection']
        result = form.cleaned_data['search']

        if result:
            if sort_option == 'newest':
                products = Product.objects.filter(woman_tag=True).filter(name__icontains=result).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(woman_tag=True).filter(name__icontains=result).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(woman_tag=True).filter(name__icontains=result).order_by('price')
            else:
                products = Product.objects.filter(woman_tag=True).filter(name__icontains=result).order_by('-datetime')
        else:
            if sort_option == 'newest':
                products = Product.objects.filter(woman_tag=True).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(woman_tag=True).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(woman_tag=True).order_by('price')
            else:
                products = Product.objects.filter(woman_tag=True).order_by('-datetime')
    else:
        products = Product.objects.filter(woman_tag=True).order_by('-datetime')

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page
    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return render(request, 'first/display.html', {'products': products_portion, 'form': form})


def geek(request):
    form = SelectionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        sort_option = form.cleaned_data['selection']
        result = form.cleaned_data['search']

        if result:
            if sort_option == 'newest':
                products = Product.objects.filter(geek_tag=True).filter(name__icontains=result).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(geek_tag=True).filter(name__icontains=result).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(geek_tag=True).filter(name__icontains=result).order_by('price')
            else:
                products = Product.objects.filter(geek_tag=True).filter(name__icontains=result).order_by('-datetime')
        else:
            if sort_option == 'newest':
                products = Product.objects.filter(geek_tag=True).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(geek_tag=True).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(geek_tag=True).order_by('price')
            else:
                products = Product.objects.filter(geek_tag=True).order_by('-datetime')
    else:
        products = Product.objects.filter(geek_tag=True).order_by('-datetime')

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page
    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def kids(request):
    form = SelectionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        sort_option = form.cleaned_data['selection']
        result = form.cleaned_data['search']

        if result:
            if sort_option == 'newest':
                products = Product.objects.filter(kid_tag=True).filter(name__icontains=result).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(kid_tag=True).filter(name__icontains=result).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(kid_tag=True).filter(name__icontains=result).order_by('price')
            else:
                products = Product.objects.filter(kid_tag=True).filter(name__icontains=result).order_by('-datetime')
        else:
            if sort_option == 'newest':
                products = Product.objects.filter(kid_tag=True).order_by('-datetime')
            elif sort_option == 'popular':
                products = Product.objects.filter(kid_tag=True).order_by('-clicks')
            elif sort_option == 'price':
                products = Product.objects.filter(kid_tag=True).order_by('price')
            else:
                products = Product.objects.filter(kid_tag=True).order_by('-datetime')
    else:
        products = Product.objects.filter(kid_tag=True).order_by('-datetime')

    # Pagination is implementing
    paginator = Paginator(products, items_in_page)  # Show 25 contacts per page
    page = request.GET.get('page')
    products_portion = paginator.get_page(page)

    return render(request, 'first/display.html', {'products': products_portion, 'form': form})

def dbupdate(request):
    if request.GET.get('id'):
        id = request.GET.get('id')
        # access DB and add one.
        object = Product.objects.get(pk=id)
        object.clicks += 1
        object.save()
    return HttpResponse('OK')