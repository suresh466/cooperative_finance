from django.shortcuts import render
from .forms import IncomeForm,ExpenseForm
from .models import Income,Expense
# Create your views here.

def income(request):
    template = 'accounting/form.html'

    transactions = Income.objects.all()

    form = IncomeForm(request.POST or None)

    if form.is_valid():
        income = form.save(commit=False)
        income.save()

    context = {
            'form': form,
            'title': 'Income',
            'transactions': transactions,
            }

    return render (request, template, context)

def expense(request):
    template = 'accounting/form.html'
    
    transactions = Expense.objects.all()

    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        expense = form.save(commit=False)
        expense.save()

    context = {
            'form': form,
            'title': "Expense",
            'transactions': transactions,
            }
    
    return render (request, template, context)

def accounting(request):
    template = 'accounting/accounting.html'

    return render(request, template)
