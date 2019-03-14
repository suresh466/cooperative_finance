from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum

from .forms import (ShareAccountForm,ShareBuyForm,
        ShareSellForm,GetShareAccountForm)

from .models import (ShareBuy,ShareSell,)
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

def share_buy_transactions(request):
    template = 'shares/shares_transactions.html'

    shares = ShareBuy.objects
    shares_sum = shares.aggregate(Sum('number'))['number__sum']

    context = {
            'transactions': shares,
            'transactions_sum': shares_sum,
            'title': "Buys",
            }

    return render(request, template, context)

def share_sell_transactions(request):
    template = 'shares/shares_transactions.html'

    shares = ShareSell.objects
    shares_sum = shares.aggregate(Sum('number'))['number__sum']

    context = {
            'transactions': shares,
            'transaxtions_sum': shares_sum,
            'title': "Sells",
            }

    return render(request, template, context)

def share_buy_transaction(request):
    template = 'shares/shares_transactions.html'

    form = GetShareAccountForm(request.POST or None)

    if form.is_valid():
        ordered_account = form.save(commit=False)
        shares = ShareBuy.objects.filter(account = ordered_account.account)
        shares_sum = shares.aggregate(Sum('number'))['number__sum']
        messages.success(request,
                'Buys of share account number {}.'
                .format(ordered_account.account.owner.mem_number))

        context = {
                'transactions': shares,
                'transactions_sum': shares_sum,
                'title': "Buys",
                }

        return render(request, template, context)

    context = {
            'form': form,
            'title': "Buys",
            }

    return render(request, template, context)

def share_sell_transaction(request):
    template = 'shares/shares_transactions.html'

    form = GetShareAccountForm(request.POST or None)

    if form.is_valid():
        ordered_account = form.save(commit=False)
        shares = ShareSell.objects.filter(account = ordered_account.account)
        shares_sum = shares.aggregate(Sum('number'))['number__sum']
        messages.success(request,
                'Sells of share account number {}.'
                .format(ordered_account.account.owner.mem_number))

        context = {
                'transactions': shares,
                'transactions_sum': shares_sum,
                'title': "Sells",
                }

        return render(request, template, context)

    context = {
            'form': form,
            'title': "Sells",
            }

    return render(request, template, context)


