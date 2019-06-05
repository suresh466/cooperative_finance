from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django import forms
from .forms import (ShareAccountForm,ShareBuyForm,
        ShareSellForm,GetShareAccountForm)

from .models import (ShareBuy,ShareSell,
        ShareAccount,)
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

def share_buy(request, **kwargs):
    template = 'shares/shares_form.html'

    if request.method == "POST":
        print("***********ok first")
        form = ShareBuyForm(request.POST)
        if form.is_valid():
            buy = form.save(commit=False)
            #adds bought share to current share of shares account
            buy.account.current_share += buy.number
            buy.account.save()
            buy.save()
            messages.success(request,
                    'You have successfully added {} share to account number {}.'
                    .format(buy.number,buy.account.owner.mem_number))

            if 'pk' in kwargs:
                return redirect("shares:buypk", pk=kwargs['pk'])
            return redirect("shares:buy")

    else:
        if 'pk' in kwargs:
            ac = kwargs['pk']
            form = ShareBuyForm()
            form.fields["account"].queryset = ShareAccount.objects.filter(id=ac)
            form.fields["account"].initial = ac
            form.fields["account"].widget = forms.HiddenInput()
        else:
            form = ShareBuyForm()

    context = {
            'form': form,
            'title': "Buy",
    }

    return render(request, template, context)


def share_sell(request, **kwargs):
    template = 'shares/shares_form.html'

    if request.method == "POST":
        form = ShareSellForm(request.POST)
        if form.is_valid():
            sell = form.save(commit=False)
            #deletes sold share from current share of shares account
            sell.account.current_share -= sell.number
            sell.account.save()
            sell.save()
            messages.success(request,
                    'You have successfully sold {} share of account number {}.'
                    .format(sell.number,sell.account.owner.mem_number))

            if 'pk' in kwargs:
                return redirect("shares:sellpk", pk=kwargs['pk'])
            return redirect("shares:sell")

    else:
        if 'pk' in kwargs:
            ac = kwargs['pk']
            form = ShareSellForm()
            form.fields["account"].queryset = ShareAccount.objects.filter(id=ac)
            form.fields["account"].initial = ac
            form.fields["account"].widget = forms.HiddenInput()
        else:
            form = ShareSellForm()

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

def share(request):
    template = 'shares/shares.html'

    return render(request, template)

def share_buy_delete(request, pk):
    template = 'shares/shares_delete.html'

    buy = get_object_or_404(ShareBuy, pk=pk)

    if request.method == "POST":
        buy.account.current_share -= buy.number
        buy.account.save()
        buy.delete_status = True
        buy.save()
        messages.success(request,
                        'You successfully deleted share_buy of account {} and number {}.'
                        .format(buy.account,buy.number))
        previous = request.POST.get('previous', None)

        return redirect(previous)

    context = {
        'item': buy,
        'type': "Buy",
    }

    return render(request, template, context)

def share_sell_delete(request, pk):
    template = 'shares/shares_delete.html'

    sell = get_object_or_404(ShareSell, pk=pk)

    if request.method == "POST":
        sell.account.current_share += sell.number
        sell.account.save()
        sell.delete_status = True
        sell.save()
        messages.success(request,
                        'You successfully deleted share_sell of account {} and number {}.'
                        .format(sell.account,sell.number))
        previous = request.POST.get('previous', None)

        return redirect(previous)

    context = {
        'item': sell,
        'type': "Sell",
    }

    return render(request, template, context)
