from django.contrib import admin
from django.contrib import admin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models

class UserAdmin(BaseUserAdmin.ModelAdmin):
    ordering = ['id']
    list_display = ['username','email']
    fieldsets  = (
        [_('Email & Password'),{'fields':('email','password')}],
        (_('Personal Info'),{'fields':('username',)}),
        (
            _('Permissions'),{'fields':('is_active','is_admin','is_staff',)}
        ),
        (_('Important Date'),{'fields':('last_login',)})
    )
    add_fieldset = (
        (None,
        {'classes':('wide',)},{'fields':('email','password1','password2')})
    )
admin.site.register(models.User,UserAdmin)