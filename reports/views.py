from django.shortcuts import render
from accounting.models import Income,Expense
# Create your views here.

def report(request):
    template = 'reports/reports.html'

    return render(request, template)

def income(request):
    template = 'reports/income.html'

    incomes = Income.objects.all()

    context = {
            'items': incomes,
            'title': "Income",
            }

    return render(request, template, context)

def expense(request):
    template = 'reports/expense.html'

    expenses = Expense.objects.all()

    context = {
            'items': expenses,
            'title': "Expense",
            }

    return render(request, template, context)
