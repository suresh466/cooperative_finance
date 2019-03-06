from django import forms
from .models import SavingDeposit,SavingWithdrawal

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

class SavingWithdrawTransactionForm(forms.ModelForm):

    class Meta:
        model = SavingDeposit
        fields = ('account',)


