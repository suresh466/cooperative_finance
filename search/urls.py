from django.urls import path

from .views import (search,member_result,
                    loan_result,)

app_name = "search"
urlpatterns = [
        path('', search, name='search'),
        path('members/result', member_result, name='member_results'),
        path('loans/result', loan_result, name='loan_results'),
]
