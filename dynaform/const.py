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

from typing import Dict

from django import forms

TEXT_FIELD = "text"
BOOLEAN_FIELD = "bool"
CHAR_FIELD = "char"
CHOICE_FIELD = "choice"


FIELD_NAME = "name"
FIELD_TYPE = "type"
FIELD_WIDGET = "widget"
FIELD_REQUIRED = "required"


DEFAULT_FIELD_CLASS: forms.Field = forms.CharField

TEXT_FIELD_WIDGET: forms.Field = forms.Textarea

DEFAULT_FIELD_TO_CLASS_MAPPER: Dict[str, forms.Field] = {
    CHAR_FIELD: forms.CharField,
    CHOICE_FIELD: forms.ChoiceField,
    BOOLEAN_FIELD: forms.BooleanField,
}
