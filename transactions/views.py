from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SavingDepositForm,SavingWithdrawlForm

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
        messages.success(request, 'You Have successfully Deposited Rs. {} only to the account number {}.'
                         .format(deposit.amount,deposit.account.owner.mem_number))
        return redirect("saving_transaction:deposit")

    context = {
        'form': form,
        'title': "Deposit"
    }

    return render(request, template, context)
