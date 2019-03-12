from django.shortcuts import (render, redirect,
        get_object_or_404)
from django.contrib import messages
from django.db.models import Sum

from .forms import (LoanIssueForm,LoanPaymentForm,
        LoanIssueTransactionForm,LoanPaymentTransactionForm,
        LoanApproveForm,)
                    
                    
                    
from .models import (LoanIssue,LoanPayment,)

# Create your views here.


def loan_issue(request):
    template = 'loans/loans_form.html'

    form = LoanIssueForm(request.POST or None)

    if form.is_valid():
        issue = form.save(commit=False)
        if issue.status == 'Approved':
            #adds issued principal to the users account total principal
            issue.account.total_principal += issue.principal
            issue.account.save()
        issue.save()
        messages.success(request,
                         'You have successfully issued Rs. {} only loan to the account number {}.'
                         .format(issue.principal,issue.account.owner.mem_number))
        return redirect("loan_transaction:issue")
    context = {
        'form': form,
        'title': "Issue",
    }

    return render(request, template, context)

def loan_payment(request):
    template = 'loans/loans_form.html'

    form = LoanPaymentForm(request.POST or None)

    if form.is_valid():
        payment = form.save(commit=False)
        #deducts payment principal from the selected loan issue and total principal
        payment.loan_num.principal -= payment.principal
        payment.loan_num.account.total_principal -= payment.principal
        payment.loan_num.account.save()
        payment.loan_num.save()
        payment.save()
        messages.success(request,
                         'you have successfully paid Rs. {} only loan to the account number {}.'
                         .format(payment.principal,payment.loan_num.account.owner.mem_number))
        return redirect("loan_transaction:pay")

    context = {
        'form': form,
        'title': "Pay",
    }

    return render(request, template, context)

def loan_issue_transactions(request):
    template = 'loans/loans_transactions.html'

    loans = LoanIssue.objects
    loans_sum = loans.aggregate(Sum('principal'))['principal__sum']

    context = {
        'transactions': loans,
        'transactions_sum': loans_sum,
        'title': "Issue",
    }

    return render(request, template, context)

def loan_payment_transactions(request):
    template = 'loans/loans_transactions.html'

    loans = LoanPayment.objects
    loans_sum = loans.aggregate(Sum('principal'))['principal__sum']

    context = {
        'transactions': loans,
        'transactions_sum': loans_sum,
        'title': "Payment",
    }

    return render(request, template, context)

def loan_issue_transaction(request):
    template = 'loans/loans_transactions.html'

    form = LoanIssueTransactionForm(request.POST or None)

    if form.is_valid():
        ordered_loan = form.save(commit=False)
        loans = LoanIssue.objects.filter(loan_num = ordered_loan.loan_num.loan_num)
        loans_sum = loans.aggregate(Sum('principal'))['principal__sum']
        messages.success(request,
                        'Loan Issue loans of loan number {}.'
                        .format(ordered_loan.loan_num))

        context = {
            'transactions': loans,
            'transactions_sum': loans_sum,
            'title': 'Issued',
        }
        return render(request, template, context)
    context = {
        'form':form,
        'title':"Issued",
    }

    return render(request, template, context)

def loan_payment_transaction(request):
    template = 'loans/loans_transactions.html'

    form = LoanPaymentTransactionForm(request.POST or None)

    if form.is_valid():
        ordered_loan = form.save(commit=False)
        loans = LoanPayment.objects.filter(loan_num = ordered_loan.loan_num)
        loans_sum = loans.aggregate(Sum('principal'))['principal__sum']
        messages.success(request,
                         'Loan Payment loans of loan number {}.'
                         .format(ordered_loan.loan_num))

        context = {
            'transactions': loans,
            'transactions_sum': loans_sum,
            'title': "Payment",
        }

        return render(request, template, context)

    context = {
        'form': form,
        'title': "Payment",
    }

    return render(request, template, context)

def loan_approve(request):
    template = 'loans/loans_form.html'

    form = LoanIssueTransactionForm(request.POST or None)

    if form.is_valid():
        loan = form.save(commit=False)
        if loan.loan_num.status == 'Approved':
            messages.success(
                request,
                'This loan is already approved')
            return redirect("loan_transaction:approve")

        loan_num = loan.loan_num.loan_num
        ordered_loan = get_object_or_404(LoanIssue, loan_num = loan_num)

        #checks if the post request coming through is from form_two
        if 'confirm' in request.POST:
            form_two = LoanApproveForm(request.POST, instance=ordered_loan)
        else:
            form_two = LoanApproveForm(instance=ordered_loan)

        if form_two.is_valid():
            issue = form_two.save(commit=False)
            #adds issued principal to the users total_principal of loan ac
            issue.account.total_principal += issue.principal
            issue.account.save()
            issue.save()
            messages.success(
                request,
                'You have successfully issued Rs. {} loan to the account number {}.'
                .format(issue.principal,issue.account.owner.mem_number))

            return redirect("loan_transaction:approve")

        context = {
            'form': form_two,
            'title': "confirm",
        }

        return render(request, template, context)

    context = {
        'form': form,
        'title': "approve",
    }
    return render(request, template, context)

