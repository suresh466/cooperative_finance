from django.db import models
from members.models import Member
from loans.models import LoanIssue
# Create your models here.

class IncomeType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Income(models.Model):
    amount = models.PositiveIntegerField()
    received_from = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_num = models.ForeignKey(LoanIssue, on_delete=models.CASCADE)
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)

    def __str__(self):
        return self.income_type.name

class ExpenseType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.PositiveIntegerField()
    payed_to = models.CharField(max_length=256)
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.expense_type.name
