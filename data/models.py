from django.db import models

# Create your models here.

class age_factor(models.Model):
    Age_factor=models.CharField(max_length=20)
    Min_age=models.IntegerField()
    Max_age=models.IntegerField()

class Country(models.Model):
    Country=models.CharField(max_length=20)

class State(models.Model):
    Country=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    
class District(models.Model):
    Country=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=20)

class hobby(models.Model):
    Hobby=models.CharField(max_length=20)

class hobby_factor(models.Model):
    Hobby_id=models.IntegerField()
    Hobby_factor=models.CharField(max_length=20)

class season(models.Model):
    Season_Name=models.CharField(max_length=20)

class country_season(models.Model):
    Country_id=models.CharField(max_length=20)
    State_id=models.CharField(max_length=20)
    Season_id=models.IntegerField()
    Month=models.CharField(max_length=20)
