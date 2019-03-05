from django import forms
from .models import SavingDeposit,SavingWithdrawl

class SavingDepositForm(forms.ModelForm):

    class Meta:
        model = SavingDeposit
        fields = ('__all__')

class SavingWithdrawlForm(forms.ModelForm):

    class Meta:
        model = SavingWithdrawl
        fields = ('__all__')


