from django.db import models
from members.models import Member

# Create your models here.

STATUS_CHOICE = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    )


class LoanAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    total_principal = models.PositiveIntegerField()

    def __str__(self):
        return self.owner.first_name

class LoanIssue(models.Model):
    account = models.ForeignKey(LoanAccount, on_delete=models.CASCADE)
    loan_num = models.CharField(unique=True, max_length=255)
    principal = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICE, default='Pending', max_length=15)

    def __str__(self):
        return self.account.owner.first_name

class LoanPayment(models.Model):
    loan_num = models.ForeignKey(LoanIssue, on_delete=models.CASCADE)
    principal = models.PositiveIntegerField()

    def __str__(self):
        return self.loan_num.account.owner.first_name


