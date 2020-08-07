from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','password','user_name','user_tel')

admin.site.register(User,UserAdmin)