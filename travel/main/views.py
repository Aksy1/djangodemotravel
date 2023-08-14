from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def destination(request):
    return render(request, 'destination.html')
def elements(request):
    return render(request, 'elements.html')
def news(request):
    return render(request, 'news.html')