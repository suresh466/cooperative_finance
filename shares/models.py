from django.db import models
from members.models import Member
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

ACCOUNT_STATUS_CHOICE = (
       	    ('Deactivated', 'Deactivated'),
            ('Activated', 'Activated'),
            )

class ShareAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    current_share = models.PositiveIntegerField()
    status = models.CharField(choices=ACCOUNT_STATUS_CHOICE, default='Deactivated', max_length=11)

    def __str__(self):
        return self.owner.first_name

class ShareBuy(models.Model):
    account = models.ForeignKey(ShareAccount, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.account.owner.first_name

class ShareSell(models.Model):
    account = models.ForeignKey(ShareAccount, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.account.owner.first_name

class ShareDelete(models.Model):
    tran_type = models.CharField(max_length=4)
    number = models.PositiveIntegerField()
    account = models.CharField(max_length=256)

    def __str__(self):
        return self.account

@receiver(post_save, sender=Member)
def create_account(sender, **kwargs):
    if kwargs['created']:
        ShareAccount.objects.create(owner=kwargs['instance'],current_share=0)


