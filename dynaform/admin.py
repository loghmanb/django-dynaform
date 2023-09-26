# -*- coding: utf-8 -*-
##############################################################################
#
#    DjangoDynaForm,
#    Copyright (C) 2023 Loghman Barari (<https://github.com/loghmanb/django-dynaform>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from django.contrib import admin

from . import models


class DynaFormAdmin(admin.ModelAdmin):
    """DynaForm admin form."""

    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25


admin.site.register(models.DynaForm, DynaFormAdmin)


class DynaFormDataAdmin(admin.ModelAdmin):
    """DynaFormData admin form."""

    list_display = ("id", "dynaform", "list_order")
    list_display_links = ("id", "dynaform")
    search_fields = ("dynaform",)
    list_per_page = 25


admin.site.register(models.DynaFormData, DynaFormDataAdmin)
