from django.db import models

# Create your models here.

class age_factor(models.Model):
    Age_factor=models.CharField(max_length=20)
    Min_age=models.IntegerField()
    Max_age=models.IntegerField()

    def __str__(self):
        return self.Age_factor

class Country(models.Model):
    Country=models.CharField(max_length=20)

    def __str__(self):
        return self.Country

class State(models.Model):
    Country=models.ForeignKey(Country,on_delete=models.CASCADE)
    State=models.CharField(max_length=20)

    def __str__(self):
        return self.State
    
class District(models.Model):
    Country=models.ForeignKey(Country,on_delete=models.CASCADE)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    District=models.CharField(max_length=20)

    def __str__(self):
        return self.District

class hobby(models.Model):
    Hobby=models.CharField(max_length=20)

    def __str__(self):
        return self.Hobby

class hobby_factor(models.Model):
    Hobby_id=models.ForeignKey(hobby,on_delete=models.CASCADE)
    Hobby_factor=models.CharField(max_length=20)

    def __str__(self):
        return self.Hobby_factor

class season(models.Model):
    Season_Name=models.CharField(max_length=20)

    def __str__(self):
        return self.Season_Name

class country_season(models.Model):
    Country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    State_id=models.ForeignKey(State,on_delete=models.CASCADE)
    Season_id=models.ForeignKey(season,on_delete=models.CASCADE)
    Month=models.CharField(max_length=20)

    def __str__(self):
        return self.Month
