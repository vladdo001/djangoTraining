from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    inlines = (BasketAdmin,)
    readonly_fields = ('date_joined', 'last_login')

