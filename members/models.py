from django.db import models

# Create your models here.

class Member(models.Model):
    mem_number = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

