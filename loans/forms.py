from django import forms
from .models import (LoanIssue,LoanPayment,)

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


