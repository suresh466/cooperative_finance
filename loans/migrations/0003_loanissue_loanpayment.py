# Generated by Django 2.1.7 on 2019-03-12 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_auto_20190308_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_num', models.CharField(max_length=255, unique=True)),
                ('principal', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanAccount')),
            ],
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.PositiveIntegerField()),
                ('loan_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanIssue')),
            ],
        ),
    ]