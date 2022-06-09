from django.contrib import admin
from .models import CustomUser,PasswordResetCode


class PasswordResetCodeAdmin(admin.ModelAdmin):
    list_display = ('user','code','created_at')
    
admin.site.register(PasswordResetCode,PasswordResetCodeAdmin)
admin.site.register(CustomUser)