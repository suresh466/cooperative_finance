from django.urls import path

from .views import (loan_issue,loan_payment,
                    loan_issue_transactions,loan_payment_transactions,)

app_name = 'loan_transaction'

urlpatterns = [
    path('pay/', loan_payment, name='pay'),
    path('issue/', loan_issue, name='issue'),
    path('pay/transactions', loan_payment_transactions, name='transactions'),
    path('issue/transactions', loan_issue_transactions, name='issue_transactions'),
]
