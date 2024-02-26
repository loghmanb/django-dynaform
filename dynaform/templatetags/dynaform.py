"""Dynaform htmtags."""

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

from typing import Any, Dict, Optional

from django import template
from django.forms import Form

register = template.Library()


@register.filter(name="id_for_label")
def id_for_label(form: Form, field_name: str) -> str:
    """Return id for label to use in html template."""
    return form.auto_id % field_name


@register.filter
def form_field(form: Form, field: str):
    """Render form field widget filter."""
    return form.fields[field].widget.render(field, form.data.get(field))


@register.filter
def field_label(form, field):
    """Field label filter."""
    return form.fields[field].label or field.capitalize()


@register.filter
def field_errors(form, field):
    """Field error filter."""
    return form.errors.get(field) or ""


@register.inclusion_tag("dynaform/link-to-dynaform-data-edit.html", takes_context=True)
def link_to_dynaform_data_edit(
    context: Optional[Dict],
    dynaform_data: Dict[str, Any],
    link_class: str = "",
    edit: Optional[bool] = None,
):
    """Create a link to edit the dynaform data."""

    if edit is None:
        edit = "edit" in context["request"].GET
    return {
        "form_name": dynaform_data.dynaform.name,
        "record_id": dynaform_data.id,
        "link_class": link_class,
        "edit_mode": edit,
    }


@register.inclusion_tag(
    "dynaform/link-to-dynaform-data-delete.html", takes_context=True
)
def link_to_dynaform_data_delete(
    context: Optional[Dict],
    dynaform_data: Dict[str, Any],
    link_class: str = "",
    edit: Optional[bool] = None,
):
    """Create a link to delete the dynaform data."""

    if edit is None:
        edit = "edit" in context["request"].GET
    return {
        "form_name": dynaform_data.dynaform.name,
        "record_id": dynaform_data.id,
        "link_class": link_class,
        "edit_mode": edit,
    }


@register.filter
def get_item(dictionary, key):
    """Get item filter."""
    return dictionary.get(key)
