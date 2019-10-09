from django.contrib import admin
from .models import user_mailcompose_tb,user_mailsave_tb,contacts_tb,user_hobby

# Register your models here.

admin.site.register(user_mailcompose_tb)
admin.site.register(user_mailsave_tb)
admin.site.register(contacts_tb)
admin.site.register(user_hobby)