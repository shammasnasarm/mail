# Generated by Django 2.1.2 on 2019-01-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_user_mailsave_tb_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mailsave_tb',
            name='From',
            field=models.CharField(max_length=20),
        ),
    ]
