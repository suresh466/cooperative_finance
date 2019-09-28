from django.urls import path

from .views import (member,member_detail,
                   member_create)

app_name = 'members'
urlpatterns = [
        path('', member, name='member'),
        path('create/', member_create, name='create'),
        path('<str:mem_number>/', member_detail, name='member_detail'),
]
