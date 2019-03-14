from django import forms
from .models import (ShareAccount,ShareBuy,
        ShareSell,)

class ShareAccountForm(forms.ModelForm):

    class Meta:
        model = ShareAccount
        fields = ('__all__')

class ShareBuyForm(forms.ModelForm):

    class Meta:
        model = ShareBuy
        fields = ('__all__')

class ShareSellForm(forms.ModelForm):

    class Meta:
        model = ShareSell
        fields = ('__all__')

