from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {}
    response = render(request, 'macro_mate/index.html', context=context_dict)
    return response
