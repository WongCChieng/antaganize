from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context={}
    return render(request, 'antaganize/main.html', context)

def help(request):
    context={}
    return render(request, 'antaganize/help.html', context)

def about(request):
    context={}
    return render(request, 'antaganize/about.html', context)