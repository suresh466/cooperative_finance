from django.urls import path

from .views import (loan_issue,)

app_name = 'loan_transaction'

urlpatterns = [
    path('issue/', loan_issue, name='issue'),
]
