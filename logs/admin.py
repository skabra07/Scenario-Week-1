from django.contrib import admin
from .models import Log

# Register your models here.

class LogAdmin(admin.ModelAdmin):
    list_display = ['id','get_username','createdTime','description']

    def get_username(self, obj):
        return obj.username

    get_username.admin_order_field  = 'log__username' 
    get_username.short_description = 'User Name'  

admin.site.register(Log,LogAdmin)
