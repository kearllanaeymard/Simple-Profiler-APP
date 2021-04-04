from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = [
        'user_fname',
        'user_lname',
        'user_email',
        'user_position',
    ]

    list_display = [
        'image_tag',
        'user_fname',
        'user_lname',
        'user_email',
        'user_position',
        'pub_date',
    ]

admin.site.register(User, UserAdmin)

admin.site.site_header = 'ADMIN DASHBOARD'
admin.site.site_title = 'Profiler App Admin'
admin.site.index_title = 'Welcome to the Admin Area'