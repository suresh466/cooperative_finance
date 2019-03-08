from django.urls import path

from .views import (loan_issue,loan_payment)

app_name = 'loan_transaction'

urlpatterns = [
    path('issue/', loan_issue, name='issue'),
    path('pay/', loan_payment, name='pay'),
]
