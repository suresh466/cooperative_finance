from django.urls import path
from .views import report,income,expense
app_name = 'reports'
urlpatterns = [
    path('', report, name='reports'),
    path('income', income, name='income'),
    path('expense', expense, name='expense'),
]
