from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea



class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = (
        'email',
        'user_name',
        'identifiant',
        'first_name',
        'last_name',
    )
    list_filter = (
        'institut',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    ordering = (
        '-start_date',
        'first_name',
        '-last_login',
        'last_name',
        'user_name',
        'institut'
    )
    list_display = (
        'email',
        'user_name',
        'first_name',
        'last_name',
        'identifier',
        'institut',
        'department',
        "start_date",
        'last_login',
        'about',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'user_name',
                'password'
            ),
        }),
        ('Affiliation',{
            'fields':(
                'institut',
                'department'
            )
        }),
        ('Permissions',{
            'fields':(
                'is_staff',
                'is_active',
                'is_superuser'
            )
        }),
        ('Personal',{
            'fields':(
                'first_name',
                'last_name',
                'about',
            )
        })
    )
    formfield_overrides = {
        NewUser.about: {'widget':Textarea(attrs={'rows':10,'cols':40})}
    }
    add_fieldsets = (
        (None,{
            'classes' : ('wide',),
            'fields':(
                'email',
                'user_name',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'about',
                'institut',
                'department',
                'is_staff',
                'is_active',
                'is_superuser',
                ),
        }),
    )

    

admin.site.register(NewUser,UserAdminConfig)

