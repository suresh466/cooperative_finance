from django.urls import path

from .views import (saving_deposit_view, saving_withdraw_view,
                    saving_deposit_transactions,saving_withdraw_transactions,
                    saving_deposit_transaction,)

app_name = 'saving_transaction'
urlpatterns = [
    path('deposit/', saving_deposit_view, name='deposit'),
    path('withdraw/', saving_withdraw_view, name='withdraw'),
    path('deposit/transactions/', saving_deposit_transactions, name='transactions'),
    path('withdraw/transactions/', saving_withdraw_transactions, name='withdraw_transactions'),
    path('deposit/transaction/', saving_deposit_transaction, name='transaction'),
    path('withdraw/transaction/', saving_deposit_transaction, name='withdraw_transaction'),
]
