from django.contrib import admin
from .models import (SavingDeposit,SavingWithdrawl)

# Register your models here.

admin.site.register(SavingDeposit)
admin.site.register(SavingWithdrawl)
