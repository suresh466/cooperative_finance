from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum

from .forms import SavingDepositForm,SavingWithdrawalForm
from .models import SavingDeposit

# Create your views here.

def saving_deposit_view(request):
    template = 'transactions/savings_form.html'

    form = SavingDepositForm(request.POST or None)

    if form.is_valid():
        deposit = form.save(commit=False)
        # adds deposit to the users saving account current balance
        deposit.account.current_balance += deposit.amount
        deposit.account.save()
        deposit.save()
        messages.success(request,
                         'You Have successfully Deposited Rs. {} only to the account number {}.'
                         .format(deposit.amount,deposit.account.owner.mem_number))
        return redirect("saving_transaction:deposit")

    context = {
        'form': form,
        'title': "Deposit"
    }

    return render(request, template, context)

def saving_withdraw_view(request):
    template = 'transactions/savings_form.html'

    form = SavingWithdrawalForm(request.POST or None)

    if form.is_valid():
        withdraw = form.save(commit=False)

        # checks if withdrawal amount is valid
        if(withdraw.account.current_balance >= withdraw.amount and
           withdraw.amount >= 10):
            withdraw.account.current_balance -= withdraw.amount
            withdraw.account.save()
            withdraw.save()
            messages.success(
                request,
                'You Have Withdrawn Rs. {} only from the account number {}.'
                .format(withdraw.amount,withdraw.account.owner.mem_number))

            return redirect("saving_transaction:withdraw")
        else:
            messages.error(
                request,
                "Either you are trying to withdraw Rs. less than 10 or your current balance is not sufficient"
            )

    context = {
        'form': form,
        'title': "Withdraw"
    }

    return render(request, template, context)

def saving_deposit_transactions(request):
    template = 'transactions/savings_transactions.html'

    transactions = SavingDeposit.objects
    transactions_sum = transactions.aggregate(Sum('amount'))['amount__sum']

    context = {
        'transactions': transactions,
        'transactions_sum': transactions_sum
    }

    return render(request, template, context)


