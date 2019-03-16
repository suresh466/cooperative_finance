from django.urls import path

from .views import (member,member_detail,)

app_name = 'members'
urlpatterns = [
        path('', member, name='member'),
        path('<int:mem_number>/', member_detail, name='member_detail'),
]
