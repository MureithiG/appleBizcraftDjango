from django.shortcuts import render


def home_one(request):
    return render(request, 'index.html')


def home_two(request):
    return render(request, 'index-2.html')


def home_three(request):
    return render(request, 'index-3.html')


def home_four(request):
    return render(request, 'index-4.html')


def about_one(request):
    return render(request, 'about.html')


def about_two(request):
    return render(request, 'about2.html')
