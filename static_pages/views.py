from django.shortcuts import render

# Create your views here.

def home(request):
    template = 'static_pages/home.html'

    return render(request, template)

def about(request):
    template = 'static_pages/about.html'

    return render(request, template)

def contact(request):
    template = 'static_pages/contact.html'

    return render(request, template)

