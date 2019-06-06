from django.urls import path

from .views import (loan_issue,loan_payment,
                    loan_issue_transactions,loan_payment_transactions,
                    loan_issue_transaction,loan_payment_transaction,
                    loan_approve,loan_account,loan,
                    get_loan,loan_issue_delete,
                    loan_payment_delete,get_loan_account)

app_name = 'loans'

urlpatterns = [
    path('', loan, name='loan'),
    path('get', get_loan_account, name='get_loan_account'),
    path('de|activate/', loan_account, name='de|activate'),
    path('pay/', loan_payment, name='pay'),
    path('pay/<int:pk>/', loan_payment, name='paypk'),
    path('pay/<int:pk>/delete', loan_payment_delete, name='payment_delete'),
    path('issue/', loan_issue, name='issue'),
    path('issue/<int:pk>/', loan_issue, name='issuepk'),
    path('issue/<int:pk>/delete', loan_issue_delete, name='issue_delete'),
    path('issue/get/', get_loan, name='get_loan'),
    path('issue/get/<int:pk>/', get_loan, name='get_loanpk'),
    path('issue/approve/', loan_approve, name='approve'),
    path('issue/approve/<int:loan_num>/', loan_approve, name='approveloan_num'),
    path('pay/transactions/', loan_payment_transactions, name='transactions'),
    path('issue/transactions/', loan_issue_transactions, name='issue_transactions'),
    path('pay/transaction/', loan_payment_transaction, name='transaction'),
    path('issue/transaction/', loan_issue_transaction, name='issue_transaction'),
]
