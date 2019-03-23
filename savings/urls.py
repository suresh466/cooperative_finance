from django.urls import path

from .views import (saving_deposit,saving_withdrawal,
        saving_deposit_transactions,saving_withdrawal_transactions,
        saving_deposit_transaction,saving_withdrawal_transaction,
        saving_account,saving,
        saving_deposit_delete,)

app_name = 'savings'
urlpatterns = [
    path('', saving, name='saving'),
    path('create/', saving_account, name='create'),
    path('deposit/', saving_deposit, name='deposit'),
    path('deposit/<int:pk>/', saving_deposit, name='depositpk'),
    path('deposit/<int:pk>/delete/', saving_deposit_delete, name='deposit_delete'),
    path('withdraw/', saving_withdrawal, name='withdraw'),
    path('withdraw/<int:pk>/', saving_withdrawal, name='withdrawpk'),
    path('deposit/transactions/', saving_deposit_transactions, name='transactions'),
    path('withdraw/transactions/', saving_withdrawal_transactions, name='withdraw_transactions'),
    path('deposit/transaction/', saving_deposit_transaction, name='transaction'),
    path('withdraw/transaction/', saving_withdrawal_transaction, name='withdraw_transaction'),
]
