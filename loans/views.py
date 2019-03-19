from django.shortcuts import (render, redirect,
        get_object_or_404)
from django.contrib import messages
from django.db.models import Sum

from .forms import (LoanIssueForm,LoanPaymentForm,
       GetLoanNumForm,LoanAccountForm) 
                    
                    
                    
from .models import (LoanIssue,LoanPayment,)

# Create your views here.

def loan_account(request):
    template = 'loans/loans_form.html'

    form = LoanAccountForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
            'form': form,
            'title': "Create",
            }

    return render(request, template, context)


def loan_issue(request, **kwargs):
    template = 'loans/loans_form.html'
    
    if request.method == "POST":
        form = LoanIssueForm(request.POST)
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
            return redirect("loans:issue")
    else:
        if 'pk' in kwargs:
            ac = kwargs['pk']
            form = LoanIssueForm(initial={'account':ac})
        else:
            form = LoanIssueForm()

    context = {
        'form': form,
        'title': "Issue",
    }

    return render(request, template, context)

def loan_payment(request, **kwargs):
    template = 'loans/loans_form.html'
    
    if request.method == "POST":
        form = LoanPaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            if not payment.loan_num.status == 'Approved':
                messages.success(request,
                        'This loan with loan no. {} is not approved yet.'
                        .format(payment.loan_num.loan_num,))
                return redirect("loans:pay")
        #deducts payment principal from the selected loan issue and total principal
            payment.loan_num.principal -= payment.principal
            payment.loan_num.account.total_principal -= payment.principal
            payment.loan_num.account.save()
            payment.loan_num.save()
            payment.save()
            messages.success(request,
                            'you have successfully paid Rs. {} only loan to the account number {}.'
                            .format(payment.principal,payment.loan_num.account.owner.mem_number))
            return redirect("loans:pay")

    else:
        if 'pk' in kwargs:
            loan_ac = kwargs['pk']
            form = LoanPaymentForm()
            form.fields["loan_num"].queryset = LoanIssue.objects.filter(account=loan_ac, status="Approved")
        else:
            form = LoanPaymentForm()

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

    form = GetLoanNumForm(request.POST or None)

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

    form = GetLoanNumForm(request.POST or None)

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

def get_loan(request, **kwargs):
    template = 'loans/loans_form.html'

    if 'pk' in kwargs:
        loan_ac = kwargs['pk']
        form = GetLoanNumForm(request.POST or None)
        form.fields["loan_num"].queryset = LoanIssue.objects.filter(account=loan_ac, status="Pending")
    else:
        form = GetLoanNumForm(request.POST or None)
        form.fields["loan_num"].queryset = LoanIssue.objects.filter(status="Pending")

    if form.is_valid():
        loan = form.save(commit=False)
        if loan.loan_num.status == 'Approved':
            messages.success(
                request,
                'This loan is already approved')
            if 'pk' in kwargs:
                return redirect("loans:get_loanpk", pk=kwargs['pk'])
            else:
                return redirect("loans:get_loan")

        loan_num = loan.loan_num.loan_num
        request.session['loan_num']=loan_num
        return redirect("loans:approve")
    
    context = {
        'form': form,
        'title': "approve",
    }
    return render(request, template, context)

def loan_approve(request, **kwargs):
    template = 'loans/loans_form.html'
    
    if 'pk' in kwargs:
        loan_num = kwargs['pk']
    else:
        loan_num = request.session['loan_num']

    ordered_loan = get_object_or_404(LoanIssue, loan_num = loan_num)

    if request.method == "POST":
        form = LoanIssueForm(request.POST, instance=ordered_loan)
    else:
        form = LoanIssueForm(instance=ordered_loan)

    if form.is_valid():
        issue = form.save(commit=False)
        #adds issued principal to the users total_principal of loan ac
        issue.account.total_principal += issue.principal
        issue.account.save()
        issue.save()
        messages.success(
                request,
                'You have issued')
        del request.session['loan_num']
        return redirect("loans:get_loan")

    context = {
        'form': form,
        'title': "confirm",
    }

    return render(request, template, context)

def loan(request):
    template = 'loans/loans.html'

    return render(request, template)
