from django.shortcuts import render
from accounting.models import Income,Expense
from loans.models import LoanPayment,LoanIssue
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

def loan(request):
    template = 'reports/loans.html'

    loans_rec = LoanPayment.objects.all()
    loans_issued = LoanIssue.objects.filter(status='Approved')

    context = {
            'items': loans_rec,
            'issued_items': loans_issued,
            'title': 'Loans',
            }

    return render(request, template, context)

def capital(request):
    pass
