from django.shortcuts import render
from .forms import IncomeForm,ExpenseForm
# Create your views here.

def income(request):
    template = 'accounting/form.html'

    form = IncomeForm(request.POST or None)

    if form.is_valid():
        income = form.save(commit=False)
        income.save()

    context = {
            'form': form,
            'title': 'Income',
            }

    return render (request, template, context)

def expense(request):
    template = 'accounting/form.html'

    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        expense = form.save(commit=False)
        expense.save()

    context = {
            'form': form,
            'title': "Expense",
            }
    
    return render (request, template, context)

def accounting(request):
    template = 'accounting/accounting.html'

    return render(request, template)
