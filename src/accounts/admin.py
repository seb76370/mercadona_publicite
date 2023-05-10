from .models import UsersAccount
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UsersAccountInline(admin.StackedInline):
    model = UsersAccount


class UserAdminCustom(UserAdmin):
    inlines = [UsersAccountInline]

admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)