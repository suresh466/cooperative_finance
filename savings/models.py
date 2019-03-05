from django.db import models
from members.models import Member

# Create your models here.

class SavingAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    current_balance = models.PositiveIntegerField()

    def __str__(self):
        return self.owner.first_name
