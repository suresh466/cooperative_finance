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

def _income():
    incomes = Income.objects.all()
    return incomes

def income(request):
    template = 'reports/income.html'

    context = {
        'items_income': _income(),
        'title_income': 'Income',
        }

    return render(request, template, context)

def _expense():
    expenses = Expense.objects.all()
    return expenses

def expense(request):
    template = 'reports/expense.html'

    context = {
            'items_expenses': _expense(),
            'title_expenses': "Expense",
            }

    return render(request, template, context)

def _loan():
    loans_rec = LoanPayment.objects.all()
    loans_issued = LoanIssue.objects.filter(status='Approved')
    return {'loans_rec': loans_rec, 'loans_issued': loans_issued}

def loan(request):
    template = 'reports/loans.html'

    loan = _loan()

    context = {
            'items_loans': loan.get("loans_rec","none"),
            'issued_items_loans': loan.get("loans_issued","none"),
            'title_loans': 'Loans',
            }

    return render(request, template, context)

def _capital():

    shares_buy = ShareBuy.objects.all()
    shares_sell = ShareSell.objects.all()
    shares_buy_sum = shares_buy.aggregate(Sum('number'))['number__sum']
    shares_sell_sum = shares_sell.aggregate(Sum('number'))['number__sum']

    savings_deposit = SavingDeposit.objects.all()
    savings_withdrawal = SavingWithdrawal.objects.all()
    savings_deposit_sum = savings_deposit.aggregate(Sum('amount'))['amount__sum']
    savings_withdrawal_sum= savings_withdrawal.aggregate(Sum('amount'))['amount__sum']

    loan_payment = LoanPayment.objects.all()
    loan_issued = LoanIssue.objects.filter(status='Approved')
    loan_payment_sum= loan_payment.aggregate(Sum('principal'))['principal__sum']
    loan_issued_sum= loan_issued.aggregate(Sum('principal'))['principal__sum']

    return {'shares_buy_sum': shares_buy_sum, 'shares_sell_sum': shares_sell_sum,
	'savings_deposit_sum': savings_deposit_sum, 'savings_withdrawal_sum':savings_withdrawal_sum,
	'loan_payment_sum': loan_payment_sum,'loan_issued_sum': loan_issued_sum,
  	 }



def capital(request):
    template = 'reports/capital.html'

    capital = _capital()

    context = {
            'shares_buy_sum_capital': capital.get('shares_buy_sum','none'),
            'shares_sell_sum_capital': capital.get('shares_sell_sum','none'),
            'savings_deposit_sum_capital': capital.get('savings_deposit_sum','none'),
            'savings_withdrawal_sum_capital': capital.get('savings_withdrawal_sum','none'),
            'loan_payment_sum_capital': capital.get('loan_payment_sum','none'),
            'loan_issued_sum_capital': capital.get('loan_issued_sum','none'),
            'title_capital': 'Capital',
            }

    return render (request, template, context)

def monthly(request):
    template = 'reports/yearly.html'

    loan = _loan()
    capital = _capital()

    context = {
        'title_yearly': 'Monthly',
        'items_income': _income(),
        'title_income': 'Income',
        'items_expenses': _expense(),
        'title_expenses': 'Expense',
        'items_loans': loan.get('loans_rec','none'),
        'issued_items_loans': loan.get('loans_issued','none'),
        'title_loans': 'Loans',
        'shares_buy_sum_capital': capital.get('shares_buy_sum','none'),
        'shares_sell_sum_capital': capital.get('shares_sell_sum','none'),
        'savings_deposit_sum_capital': capital.get('savings_deposit_sum','none'),
        'savings_withdrawal_sum_capital': capital.get('savings_withdrawal_sum','none'),
        'loan_payment_sum_capital': capital.get('loan_payment_sum','none'),
        'loan_issued_sum_capital': capital.get('loan_issued_sum','none'),
        'title_capital': 'Capital',
        }

    return render(request, template, context)


def yearly(request):
    template = 'reports/yearly.html'

    loan = _loan()
    capital = _capital()

    context = {
        'title_yearly': 'Yearly',
        'items_income': _income(),
        'title_income': 'Income',
        'items_expenses': _expense(),
        'title_expenses': 'Expense',
        'items_loans': loan.get('loans_rec','none'),
        'issued_items_loans': loan.get('loans_issued','none'),
        'title_loans': 'Loans',
        'shares_buy_sum_capital': capital.get('shares_buy_sum','none'),
        'shares_sell_sum_capital': capital.get('shares_sell_sum','none'),
        'savings_deposit_sum_capital': capital.get('savings_deposit_sum','none'),
        'savings_withdrawal_sum_capital': capital.get('savings_withdrawal_sum','none'),
        'loan_payment_sum_capital': capital.get('loan_payment_sum','none'),
        'loan_issued_sum_capital': capital.get('loan_issued_sum','none'),
        'title_capital': 'Capital',
        }

    return render(request, template, context)
