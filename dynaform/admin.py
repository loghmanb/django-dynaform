from django.contrib import admin

from . import models


class DynaFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(models.DynaForm, DynaFormAdmin)


class DynaFormDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'dynaform', 'list_order')
    list_display_links = ('id', 'dynaform')
    search_fields = ('dynaform',)
    list_per_page = 25

admin.site.register(models.DynaFormData, DynaFormDataAdmin)
