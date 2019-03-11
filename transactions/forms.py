from django import forms
from .models import (SavingDeposit,SavingWithdrawal,
                     LoanIssue,LoanPayment)

class SavingDepositForm(forms.ModelForm):

    class Meta:
        model = SavingDeposit
        fields = ('__all__')

class SavingWithdrawalForm(forms.ModelForm):

    class Meta:
        model = SavingWithdrawal
        fields = ('__all__')

class SavingDepositTransactionForm(forms.ModelForm):

    class Meta:
        model = SavingDeposit
        fields = ('account',)

class SavingWithdrawalTransactionForm(forms.ModelForm):

    class Meta:
        model = SavingDeposit
        fields = ('account',)

class LoanIssueForm(forms.ModelForm):
    class Meta:
        model = LoanIssue
        fields = ('__all__')

class LoanPaymentForm(forms.ModelForm):
    class Meta:
        model = LoanPayment
        fields = ('__all__')

class LoanPaymentTransactionForm(forms.ModelForm):
    class Meta:
        model = LoanPayment
        fields = ('loan_num',)

class LoanIssueTransactionForm(forms.ModelForm):
    class Meta:
        model = LoanPayment
        fields = ('loan_num',)

class LoanApproveForm(forms.ModelForm):
    class Meta:
        model = LoanIssue
        fields = ('__all__')


