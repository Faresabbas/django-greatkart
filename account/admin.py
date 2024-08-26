from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('user_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')
    search_fields = ('user_name', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
