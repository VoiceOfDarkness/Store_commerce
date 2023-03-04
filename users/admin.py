from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerfication, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [BasketAdmin]


@admin.register(EmailVerfication)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration']
    fields = ['code', 'user', 'expiration', 'created']
    readonly_fields = ['created']
