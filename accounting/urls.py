from django.urls import path

from .views import (income,expense,
                    accounting,income_delete,
                    expense_delete,
                    )

app_name = 'accounting'
urlpatterns = [
        path('', accounting, name="accounting"),
        path('income/', income, name="income"),
        path('expense/', expense, name="expense"),
        path('income/<int:pk>/delete/', income_delete, name="income_delete"),
        path('expense/<int:pk>/delete/', expense_delete, name="expense_delete"),
]
