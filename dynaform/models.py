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

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class DynaForm(models.Model):
    """DynaForm data model."""

    name = models.CharField(
        _("Name"), max_length=50, null=False, blank=False, unique=True
    )
    label = models.CharField(_("Label"), max_length=50, null=False, blank=False)
    structure = models.JSONField(default=dict)

    def clean(self):
        self.name = self.name.strip().replace(" ", "_").replace("-", "_")
        if not self.name.isidentifier():
            raise ValidationError({"name": f"'{self.name}' is NOT a valid identifier!"})

    def __str__(self) -> str:
        return f"{self.label} [{self.name}]"


class DynaFormData(models.Model):
    """DynaFormData data model."""

    dynaform = models.ForeignKey(DynaForm, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)
    list_order = models.IntegerField()
