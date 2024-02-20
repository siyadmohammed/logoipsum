from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

PRODUCTS_PER_PAGE = 5


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/author")
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect("/")


class ListProducts(ListView):
    template_name = "author.html"
    model = author1
    context_object_name = "product"
    paginate_by = 2


def author(request):
    search = request.GET.get('search', "")
    if search:
        product = author1.objects.filter(Q(AUTHOR_NAME__icontains=search) | Q(USER_NAME__icontains=search))
    else:
        product = author1.objects.all()

    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
    try:
        product = product_paginator.page(page)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    except:
        product = product_paginator.page(PRODUCTS_PER_PAGE)
    return render(request, "author.html",
                  {"product": product, 'page_obj': product, 'is_paginated': True, 'paginator': product_paginator})


class ListProducts1(ListView):
    template_name = "books.html"
    model = book1
    context_object_name = "product"
    paginate_by = 2


def books(request):
    search = request.GET.get('search', "")
    if search:
        product = book1.objects.filter(Q(BOOK_NAME__icontains=search) | Q(AUTHOR_NAME__icontains=search))
    else:
        product = book1.objects.all()

    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCTS_PER_PAGE)
    try:
        product = product_paginator.page(page)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)
    except:
        product = product_paginator.page(PRODUCTS_PER_PAGE)
    return render(request, "books.html",
                  {"product": product, 'page_obj': product, 'is_paginated': True, 'paginator': product_paginator})


def saveauthor(request):
    if request.method == "POST":
        c = author1()
        c.AUTHOR_NAME = request.POST.get("authorname")
        c.USER_NAME = request.POST.get("authorusername")
        c.EMAIL = request.POST.get("authoremail")
        c.save()
        return redirect("/author/")


def savebook(request):
    if request.method == "POST":
        d = book1()
        d.BOOK_NAME = request.POST.get("bookname")
        d.AUTHOR_NAME = request.POST.get("authorname")
        d.save()
        return redirect("/books/")


def author_count(request):
    count = author1.objects.count()
    return JsonResponse({'count': count})


def book_count(request):
    count = book1.objects.count()
    return JsonResponse({'count': count})


def editbook(request, id):
    h = book1.objects.get(id=id)
    return render(request, "editphonedata.html", {'h': h})


def viewauthorfull(request,author,id):
    p = book1.objects.filter(AUTHOR_NAME=author)
    q = author1.objects.get(SERIAL_NO=id)
    return render(request, 'authordetailedview.html',{'p':p,'q':q})


def deletebook(request, id):
    e = book1.objects.get(id=id)
    e.delete()
    return redirect("/books/")


def suggestionApi(request):
    query = request.GET.get('term', '')
    results = author1.objects.filter(AUTHOR_NAME__icontains=query).values_list('AUTHOR_NAME', flat=True)
    data = list(results)
    print(data)
    return JsonResponse(data, safe=False)




def listProductsApi(request):
    result = list(author1.objects.values())
    return render(request, "author.html", {"product": result})


def suggestionApi1(request):
    query = request.GET.get('term', '')
    results = book1.objects.filter(BOOK_NAME__icontains=query).values_list('BOOK_NAME', flat=True)
    data = list(results)
    print(data)
    return JsonResponse(data, safe=False)




def listProductsApi1(request):
    result = list(book1.objects.values())
    return render(request, "book.html", {"product": result})
