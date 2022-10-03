from django.urls import path
from django.shortcuts import render
from django.contrib import admin
from user.models import User

# Register your models here.
admin.site.site_header = "Custome Admin Action"
admin.site.site_title = "Custome Admin Action"
admin.site.index_title = "Welcome to Custome Admin Action"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """_summary_

    Args:
        admin (_type_): _description_
    """
    model = User
    fields = [("full_name","email"),"phone"]
    list_display = ("full_name","email","phone")
    search_fields = ['full_name','email']
    actions = ['set_phone','get_url']
    ordering = ['full_name','email']
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        # if request.user.username[0].upper() != 'J':
        #     if 'get_url' in actions:
        #         del actions['get_url']
        return actions
    
    def set_phone(self, request, queryset):
        queryset.update(phone = 000000000)

    
    def get_url(self, request, queryset):
        tmpl = 'index.html'
        return render(request, tmpl)
    