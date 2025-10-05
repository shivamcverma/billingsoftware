from django.contrib import admin

from myapp.models import adminlogintbl, additemstbl, customertbl

# Register your models here.
admin.site.register(adminlogintbl)
admin.site.register(additemstbl)
admin.site.register(customertbl)