# Generated by Django 2.1.7 on 2019-09-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0010_auto_20190928_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanaccount',
            name='status',
            field=models.CharField(choices=[('Deactivated', 'Deactivated'), ('Activated', 'Activated')], default='Activated', max_length=11),
        ),
    ]