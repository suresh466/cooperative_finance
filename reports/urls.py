from django.urls import path
from .views import report,income,expense,loan,capital,monthly,yearly
app_name = 'reports'
urlpatterns = [
    path('', report, name='reports'),
    path('income', income, name='income'),
    path('expense', expense, name='expense'),
    path('loans', loan, name='loan'),
    path('capital', capital, name='capital'),
    path('monthly', monthly, name='monthly'),
    path('yearly', yearly, name='yearly'),
]
