# Generated by Django 2.1.7 on 2019-06-12 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0007_auto_20190612_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savingaccount',
            old_name='date_update',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='savingdeposit',
            old_name='date_update',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='savingwithdrawal',
            old_name='date_update',
            new_name='date_updated',
        ),
    ]
