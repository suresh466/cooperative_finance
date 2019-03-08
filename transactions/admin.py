from django.contrib import admin
from .models import (SavingDeposit,SavingWithdrawal,
                     LoanIssue,)

# Register your models here.

admin.site.register(SavingDeposit)
admin.site.register(SavingWithdrawal)
admin.site.register(LoanIssue)
