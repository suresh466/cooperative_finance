from django.db import models
from members.models import Member

# Create your models here.

class LoanAccount(models.Model):
    owner = models.OneToOneField(Member, on_delete=models.CASCADE)
    total_principal = models.PositiveIntegerField()

    def __str__(self):
        return self.owner.first_name
