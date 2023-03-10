from django.contrib import admin

from .models import *


# class userProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email')
#     list_display_links = ('id', 'username')
#     search_fields = ('username', 'content')


class CreditAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')
    search_fields = ('name', 'status')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    # search_fields = ('name')


# admin.site.register(userProfile, userProfileAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(Status, StatusAdmin)