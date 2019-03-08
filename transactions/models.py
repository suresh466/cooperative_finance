from django.db import models
from savings.models import SavingAccount
from loans.models import LoanAccount

# Create your models here.

class SavingDeposit(models.Model):
    account = models.ForeignKey(SavingAccount, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.account.owner.first_name

class SavingWithdrawal(models.Model):
    account = models.ForeignKey(SavingAccount, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.account.owner.first_name

class LoanIssue(models.Model):
    account = models.ForeignKey(LoanAccount, on_delete=models.CASCADE)
    principal = models.PositiveIntegerField()

    def __str__(self):
        return self.account.owner.first_name

class LoanPayment(models.Model):
    account = models.ForeignKey(LoanAccount, on_delete=models.CASCADE)
    principal = models.PositiveIntegerField()

    def __str__(self):
        return self.account.owner.first_name

