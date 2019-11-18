from django.contrib import admin

# Register your models here.


from . import models
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = (
        'user',

        'description',

    )
def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Profile, ProfileAdmin)