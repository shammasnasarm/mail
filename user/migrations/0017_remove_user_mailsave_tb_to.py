# Generated by Django 2.1.2 on 2019-01-21 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_user_mailsave_tb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_mailsave_tb',
            name='To',
        ),
    ]
