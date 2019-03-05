from django.urls import path

from .views import saving_deposit_view

app_name = 'saving_transaction'
urlpatterns = [
    path('deposit/', saving_deposit_view, name='deposit'),
]
