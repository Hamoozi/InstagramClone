from django.shortcuts import render

# Create your views here.


def users(request):
    return render(request, 'index.html')