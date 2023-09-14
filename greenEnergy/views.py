from django.shortcuts import render

def store(request):
    return render(request, 'online_store.html')

def kits(request):
    return render(request, 'kits.html')

def about(request):
    return render(request, 'about.html')
