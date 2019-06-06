from django.db import models

# Create your models here.

ACCOUNT_STATUS_CHOICE = (
    ('Deactivated','Deactivated'),
    ('Activated', 'Activated'),
    )

class Member(models.Model):
    mem_number = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    contact = models.CharField(max_length=10)
    status = models.CharField(choices=ACCOUNT_STATUS_CHOICE, default='Activated', max_length=11,editable=False)

    def __str__(self):
        return self.first_name

