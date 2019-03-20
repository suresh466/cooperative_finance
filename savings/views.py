from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django import forms

from .forms import (SavingDepositForm,SavingWithdrawalForm,
        GetSavingAccountForm,SavingAccountForm,)
                    
from .models import (SavingDeposit,SavingWithdrawal,
        SavingAccount,)

# Create your views here.

def saving_account(request):
    template = 'savings/savings_form.html'

    form = SavingAccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
            'form':form,
            'title': "create",
            }

    return render(request, template, context)


def saving_deposit(request, **kwargs):
    template = 'savings/savings_form.html'

    if request.method == 'POST':
        form = SavingDepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            # adds deposit to the users saving account current balance
            deposit.account.current_balance += deposit.amount
            deposit.account.save()
            deposit.save()
            messages.success(request,
                         'You Have successfully Deposited Rs. {} only to the account number {}.'
                         .format(deposit.amount,deposit.account.owner.mem_number))
            if 'pk' in kwargs:
                return redirect("savings:depositpk", pk=kwargs['pk'])
            return redirect("savings:deposit")
    else:
        if 'pk' in kwargs:
            ac=kwargs['pk']
            form = SavingDepositForm()
            form.fields["account"].queryset = SavingAccount.objects.filter(id=ac)
            form.fields["account"].initial = ac
            form.fields["account"].widget = forms.HiddenInput() 
        else:
             form = SavingDepositForm()
    context = {
            'form': form,
            'title': "Deposit"
    }

    return render(request, template, context)

def saving_withdrawal(request, **kwargs):
    template = 'savings/savings_form.html'

    if request.method == "POST":
        form = SavingWithdrawalForm(request.POST)
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

                if 'pk' in kwargs:
                    return redirect("savings:withdrawpk", pk=kwargs['pk'])
                return redirect("savings:withdraw")
            else:
                messages.error(
                    request,
                    "Either you are trying to withdraw Rs. less than 10 or your current balance is not sufficient"
                )
    else:
        if 'pk' in kwargs:
            ac = kwargs['pk']
            form = SavingWithdrawalForm()
            form.fields["account"].queryset = SavingAccount.objects.filter(id=ac)
            form.fields["account"].initial = ac
            form.fields["account"].widget = forms.HiddenInput() 
        else:
            form = SavingWithdrawalForm()

    context = {
        'form': form,
        'title': "Withdraw"
    }

    return render(request, template, context)

def saving_deposit_transactions(request):
    template = 'savings/savings_transactions.html'

    savings = SavingDeposit.objects
    savings_sum = savings.aggregate(Sum('amount'))['amount__sum']

    context = {
        'transactions': savings,
        'transactions_sum': savings_sum,
        'title': "Deposit",
    }

    return render(request, template, context)

def saving_withdrawal_transactions(request):
    template = 'savings/savings_transactions.html'

    savings = SavingWithdrawal.objects
    savings_sum = savings.aggregate(Sum('amount'))['amount__sum']

    context = {
        'transactions': savings,
        'transactions_sum': savings_sum,
        'title': "Withdrawal",
    }

    return render(request, template, context)

def saving_deposit_transaction(request):
    template = 'savings/savings_transactions.html'

    form = GetSavingAccountForm(request.POST or None)

    if form.is_valid():
        ordered_account = form.save(commit=False)
        savings = SavingDeposit.objects.filter(account = ordered_account.account)
        savings_sum = savings.aggregate(Sum('amount'))['amount__sum']
        messages.success(request,
                         'Deposit savings of savings account number {}.'
                         .format(ordered_account.account.owner.mem_number))
        context = {
            'transactions': savings,
            'transactions_sum': savings_sum,
            'title': "Deposit",
        }

        return render(request, template, context)

    context = {
        'form': form,
        'title': "Deposit",
    }

    return render(request, template, context)

def saving_withdrawal_transaction(request):
    template = 'savings/savings_transactions.html'

    form = GetSavingAccountForm(request.POST or None)

    if form.is_valid():
        ordered_account = form.save(commit=False)
        savings = SavingWithdrawal.objects.filter(account = ordered_account.account)
        savings_sum = savings.aggregate(Sum('amount'))['amount__sum']
        messages.success(request,
                         'Withdrawal ransactions of savings account number {}.'
                         .format(ordered_account.account.owner.mem_number))

        context = {
            'transactions':savings,
            'transactions_sum':savings_sum,
            'title': "Withdrawal",
        }

        return render(request, template, context)
    context = {
        'form':form,
        'title': "Withdrawal",
    }

    return render(request, template, context)

def saving(request):
    template = 'savings/savings.html'

    return render(request, template)
