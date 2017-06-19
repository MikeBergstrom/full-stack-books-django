# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Books

def index(request):
    books = Books.objects.all()
    context = {"books": books}
    print books
    return render(request, 'books/index.html', context)

def process(request):
    if request.method == "POST":   
        Books.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
        books = Books.objects.all()
        print books
    return redirect('/')
# Create your views here.
