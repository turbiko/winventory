from django.shortcuts import render


def home(request):
    context = {}
    print('Home')
    return render(request, 'home/home.html', context)
