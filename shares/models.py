from django.db import models
from members.models import Member
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class ShareAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    current_share = models.PositiveIntegerField()

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

@receiver(post_save, sender=Member)
def create_account(sender, **kwargs):
    ShareAccount.objects.create(owner=kwargs['instance'],current_share=0)


