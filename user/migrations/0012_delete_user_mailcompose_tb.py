# Generated by Django 2.1.2 on 2019-01-18 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_user_mailcompose_tb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_mailcompose_tb',
        ),
    ]