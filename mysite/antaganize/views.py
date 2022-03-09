from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


def view_index(request):
    """
    main page
    """
    context={}
    return render(request, 'antaganize/main.html', context)

def view_help(request):
    """
    help page
    """
    context={}
    return render(request, 'antaganize/help.html', context)

def view_about(request):
    context={}
    return render(request, 'antaganize/about.html', context)