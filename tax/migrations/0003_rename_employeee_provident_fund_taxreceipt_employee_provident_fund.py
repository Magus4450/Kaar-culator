# Generated by Django 4.0.3 on 2022-04-27 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0002_alter_taxreceipt_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxreceipt',
            old_name='employeee_provident_fund',
            new_name='employee_provident_fund',
        ),
    ]