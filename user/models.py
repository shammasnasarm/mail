from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_details(models.Model):
    User_id=models.ForeignKey(User,on_delete=models.CASCADE)
    DOB=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=20)
    Phone_No=models.IntegerField()

                                               
class user_hobby(models.Model):
    Username=models.CharField(max_length=20)
    Hobby=models.CharField(max_length=20)
    

class user_mailcompose_tb(models.Model):
    From=models.ForeignKey(User,on_delete=models.CASCADE)
    To=models.IntegerField()
    Subject=models.CharField(max_length=20)
    Content=models.CharField(max_length=500)
    Date=models.CharField(max_length=20)
    File=models.FileField()
    Status=models.CharField(max_length=20)

class user_mailsave_tb(models.Model):
    User_id=models.IntegerField()
    Mail_id=models.ForeignKey(user_mailcompose_tb,on_delete=models.CASCADE)




class contacts_tb(models.Model):
    User_id=models.IntegerField()
    Contact_id=models.IntegerField()
    Date=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    
