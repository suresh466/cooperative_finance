from django.urls import path

from .views import saving_deposit_view, saving_withdraw_view

app_name = 'saving_transaction'
urlpatterns = [
    path('deposit/', saving_deposit_view, name='deposit'),
    path('withdraw/', saving_withdraw_view, name='withdraw'),
]
