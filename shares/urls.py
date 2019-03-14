from django.urls import path

from .views import (share_account,share_buy,
        share_sell,share_buy_transactions,
        share_sell_transactions,share_buy_transaction,
        share_sell_transaction,)

app_name = 'shares'
urlpatterns = [
    path('create/', share_account, name='create'),
    path('buy/', share_buy, name='buy'),
    path('sell/', share_sell, name='sell'),
    path('buy/transactions/', share_buy_transactions, name='transactions'),
    path('sell/transactions/', share_sell_transactions, name='sell_transactions'),
    path('buy/transaction/', share_buy_transaction, name='transaction'),
    path('sell/transaction/', share_sell_transaction, name='sell_transaction'),
]
