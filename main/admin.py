from django.contrib import admin
from .models import CustomUser, MenuItem, Category, Menu, Business
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken













class BusinessAdmin(admin.ModelAdmin):
    filter_horizontal = ('root_user_list', 'customer_user_list', 'staff_user_list')


admin.site.register(CustomUser)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(MenuItem)














