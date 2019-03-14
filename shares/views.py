from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import (ShareAccountForm,ShareBuyForm,
        ShareSellForm,)

# Create your views here.

def share_account(request):
    template = 'shares/shares_form.html'

    form = ShareAccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
            'form': form,
            'title': "Create",
            }

    return render(request, template, context)

def share_buy(request):
    template = 'shares/shares_form.html'

    form = ShareBuyForm(request.POST or None)

    if form.is_valid():
        buy = form.save(commit=False)
        #adds bought share to current share of shares account
        buy.account.current_share += buy.number
        buy.account.save()
        buy.save()
        messages.success(request,
                'You have successfully added {} share to account number {}.'
                .format(buy.number,buy.account.owner.mem_number))

        return redirect("shares:buy")

    context = {
            'form': form,
            'title': "Buy",
            }

    return render(request, template, context)


def share_sell(request):
    template = 'shares/shares_form.html'

    form = ShareSellForm(request.POST or None)

    if form.is_valid():
        sell = form.save(commit=False)
        #deletes sold share from current share of shares account
        sell.account.current_share -= sell.number
        sell.account.save()
        sell.save()
        messages.success(request,
                'You have successfully sold {} share of account number {}.'
                .format(sell.number,sell.account.owner.mem_number))

        return redirect("shares:sell")

    context = {
            'form': form,
            'title': "Sell",
            }

    return render(request, template, context)


