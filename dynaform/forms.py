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

from typing import Any, Callable, Dict, Optional

from django.forms import Field, Form

from .const import (
    BOOLEAN_FIELD,
    DEFAULT_FIELD_CLASS,
    DEFAULT_FIELD_TO_CLASS_MAPPER,
    FIELD_REQUIRED,
    FIELD_TYPE,
    FIELD_WIDGET,
    TEXT_FIELD,
    TEXT_FIELD_WIDGET,
)


def create_form_field(
    structure: Dict,
    default_field_class: Field = DEFAULT_FIELD_CLASS,
    field2class_mapper: Optional[Dict[str, Field]] = None,
    text_field_widget: Field = TEXT_FIELD_WIDGET,
) -> Field:
    """Create form's field."""

    if field2class_mapper is None:
        field2class_mapper = DEFAULT_FIELD_TO_CLASS_MAPPER
    field_type = structure.pop(FIELD_TYPE)
    if field_type == TEXT_FIELD and structure.get(FIELD_WIDGET) is None:
        structure[FIELD_WIDGET] = text_field_widget()
    elif field_type == BOOLEAN_FIELD:
        structure[FIELD_REQUIRED] = False
    klass = field2class_mapper.get(field_type, default_field_class)
    return klass(**structure)


class DynaFormData(Form):
    """DyanForm data class."""

    def __init__(
        self,
        structure: Dict[str, Dict[str, Any]],
        *args,
        custom_create_form_field_func: Callable = None,
        **kwargs
    ):
        super(DynaFormData, self).__init__(*args, **kwargs)

        if custom_create_form_field_func is None:
            custom_create_form_field_func = create_form_field

        for field, field_stru in structure.items():
            self.fields[field] = custom_create_form_field_func(field_stru)
