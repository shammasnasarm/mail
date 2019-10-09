from django.contrib import admin
from .models import age_factor,Country,State,District,hobby,hobby_factor,season,country_season

# Register your models here.

admin.site.register(age_factor)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(hobby)
admin.site.register(hobby_factor)
admin.site.register(season)
admin.site.register(country_season)
