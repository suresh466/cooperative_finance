from django.urls import path

from .views import (income,expense,
                    accounting,)

app_name = 'accounting'
urlpatterns = [
        path('', accounting, name="accounting"),
        path('income/', income, name="income"),
        path('expense/', expense, name="expense"),
]
