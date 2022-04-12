from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage


def view_index(request):
    """
    main page
    """
    if request.method == 'POST':
        print("-----------------")
        print(request.FILES)
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            return render(request, 'antaganize/main.html',{'form':form,'file_url': file_url})
    else:
        form = ImageForm()

    return render(request, 'antaganize/main.html',{'form':form})

def view_help(request):
    """
    help page
    """
    context={}
    return render(request, 'antaganize/help.html', context)

def view_about(request):
    context={}
    return render(request, 'antaganize/about.html', context)