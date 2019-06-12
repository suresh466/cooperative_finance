from django.db import models
from members.models import Member
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

STATUS_CHOICE = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        )

ACCOUNT_STATUS_CHOICE = (
       	('Deactivated', 'Deactivated'),
        ('Activated', 'Activated'),
        )

DELETE_STATUS_CHOICE = (
        ('False', 'False'),
        ('True', 'True'),
        )

class LoanAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    total_principal = models.PositiveIntegerField()
    status = models.CharField(choices=ACCOUNT_STATUS_CHOICE, default='Deactivated', max_length=11)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.first_name

class LoanIssue(models.Model):
    account = models.ForeignKey(LoanAccount, on_delete=models.CASCADE)
    loan_num = models.CharField(unique=True, max_length=255)
    principal = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICE, default='Pending', max_length=15)
    delete_status = models.CharField(choices=DELETE_STATUS_CHOICE, default='False', max_length=5, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account.owner.first_name

class LoanPayment(models.Model):
    loan_num = models.ForeignKey(LoanIssue, on_delete=models.CASCADE)
    principal = models.PositiveIntegerField()
    delete_status = models.CharField(choices=DELETE_STATUS_CHOICE, default='False', max_length=5, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.loan_num.account.owner.first_name

@receiver(post_save, sender=Member)
def create_account(sender, **kwargs):
    if kwargs['created']:
        LoanAccount.objects.create(owner=kwargs['instance'],total_principal=0)


