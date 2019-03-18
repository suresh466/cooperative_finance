from django.urls import path

from .views import (loan_issue,loan_payment,
                    loan_issue_transactions,loan_payment_transactions,
                    loan_issue_transaction,loan_payment_transaction,
                    loan_approve,loan_account,loan,
                    get_loan,)

app_name = 'loans'

urlpatterns = [
    path('', loan, name='loan'),
    path('create/', loan_account, name='create'),
    path('pay/', loan_payment, name='pay'),
    path('pay/<int:pk>', loan_payment, name='paypk'),
    path('issue/', loan_issue, name='issue'),
    path('issue/<int:pk>', loan_issue, name='issuepk'),
    path('issue/get/', get_loan, name='get_loan'),
    path('issue/approve/', loan_approve, name='approve'),
    path('pay/transactions/', loan_payment_transactions, name='transactions'),
    path('issue/transactions/', loan_issue_transactions, name='issue_transactions'),
    path('pay/transaction/', loan_payment_transaction, name='transaction'),
    path('issue/transaction/', loan_issue_transaction, name='issue_transaction'),
]
