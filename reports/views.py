from django.shortcuts import render
from accounting.models import Income,Expense
from loans.models import LoanPayment,LoanIssue
from shares.models import ShareBuy,ShareSell
from savings.models import SavingDeposit,SavingWithdrawal
from django.db.models import Sum
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
    template = 'reports/capital.html'

    shares_buy = ShareBuy.objects.all()
    shares_buy_sum = shares_buy.aggregate(Sum('number'))['number__sum']
    shares_sell = ShareSell.objects.all()
    shares_sell_sum = shares_sell.aggregate(Sum('number'))['number__sum']

    savings_deposit = SavingDeposit.objects.all()
    savings_deposit_sum = savings_deposit.aggregate(Sum('amount'))['amount__sum']
    savings_withdrawal = SavingWithdrawal.objects.all()
    savings_withdrawal_sum= savings_withdrawal.aggregate(Sum('amount'))['amount__sum']

    loan_payment = LoanPayment.objects.all()
    loan_payment_sum= loan_payment.aggregate(Sum('principal'))['principal__sum']
    loan_issued = LoanIssue.objects.filter(status='Approved')
    loan_issued_sum= loan_issued.aggregate(Sum('principal'))['principal__sum']

    context = {
            'shares_buy_sum': shares_buy_sum,
            'shares_sell_sum': shares_sell_sum,
            'savings_deposit_sum': savings_deposit_sum,
            'savings_withdrawal_sum': savings_withdrawal_sum,
            'loan_payment_sum': loan_payment_sum,
            'loan_issued_sum': loan_issued_sum,
            'loan_issued': loan_issued,
            'title': 'Capital',
            }

    return render (request, template, context)
