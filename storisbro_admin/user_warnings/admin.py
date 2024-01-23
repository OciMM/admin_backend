from django.contrib import admin
from .models import GetFullUserModel, WarningToUser, CustomUser

@admin.register(GetFullUserModel)
class GetFullUserModel(admin.ModelAdmin):
    list_display = ['id']
    
admin.site.register(WarningToUser)
admin.site.register(CustomUser)