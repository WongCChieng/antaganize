from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_question_list = [1,2,3,4,5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    return HttpResponse("You're looking at question" )