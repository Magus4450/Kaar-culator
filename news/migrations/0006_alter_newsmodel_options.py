# Generated by Django 4.0.3 on 2022-03-28 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsmodel_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'ordering': ['post_date']},
        ),
    ]
