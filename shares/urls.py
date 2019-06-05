from django.urls import path

from .views import (share_account,share_buy,
        share_sell,share_buy_transactions,
        share_sell_transactions,share_buy_transaction,
        share_sell_transaction,share,
        share_buy_delete,share_sell_delete,)

app_name = 'shares'
urlpatterns = [
    path('', share, name='share'),
    path('create/', share_account, name='create'),
    path('buy/', share_buy, name='buy'),
    path('buy/<int:pk>/', share_buy, name='buypk'),
    path('buy/<int:pk>/delete/', share_buy_delete, name='buy_delete'),
    path('sell/', share_sell, name='sell'),
    path('sell/<int:pk>/', share_sell, name='sellpk'),
    path('sell/<int:pk>/delete', share_sell_delete, name='sell_delete'),
    path('buy/transactions/', share_buy_transactions, name='transactions'),
    path('sell/transactions/', share_sell_transactions, name='sell_transactions'),
    path('buy/transaction/', share_buy_transaction, name='transaction'),
    path('sell/transaction/', share_sell_transaction, name='sell_transaction'),
]
