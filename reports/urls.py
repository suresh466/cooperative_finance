from django.urls import path
from .views import report
app_name = 'reports'
urlpatterns = [
    path('', report, name='reports')
]
