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

class GetLoanNumForm(forms.ModelForm):
    class Meta:
        model = LoanPayment
        fields = ('loan_num',)
