from atexit import register
from django.contrib import admin
from user.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """_summary_

    Args:
        admin (_type_): _description_
    """
    