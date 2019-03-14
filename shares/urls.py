from django.urls import path

from .views import (share_account,share_buy,
        share_sell,)

app_name = 'shares'
urlpatterns = [
    path('create/', share_account, name='create'),
    path('buy/', share_buy, name='buy'),
    path('sell/', share_sell, name='sell'),
]
