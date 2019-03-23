from django.shortcuts import render

# Create your views here.

def report(request):
    template = 'reports/reports.html'

    return render(request, template)
