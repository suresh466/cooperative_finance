from django.contrib import admin
from .models import (LoanAccount,LoanIssue,
                    LoanPayment)

# Register your models here.

admin.site.register(LoanIssue)
admin.site.register(LoanPayment)
admin.site.register(LoanAccount)
