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

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse

from . import forms, models

DEFAULT_DYFORM_BASE_TEMPLATE: str = getattr(
    settings, "DEFAULT_DYFORM_BASE_TEMPLATE", "dynaform/base.html"
)


def dynaform_data_list(request: HttpRequest, dynaform_name: str) -> HttpResponse:
    """View for list of DynaForm data."""
    dynaform = models.DynaForm.objects.get(name=dynaform_name)
    columns = list(dynaform.structure.keys())
    rows = models.DynaFormData.objects.filter(dynaform_id=dynaform.id)
    return TemplateResponse(
        request,
        "dynaform/dynaform-data-list.html",
        {
            "DYFORM_BASE_TEMPLATE": DEFAULT_DYFORM_BASE_TEMPLATE,
            "columns": columns,
            "rows": rows,
        },
    )


def dynaform_data(request: HttpRequest, dynaform_name: str, pk: int) -> HttpResponse:
    """View for editing a DynaForm data item."""
    dynaform_data_record = get_object_or_404(
        models.DynaFormData, pk=pk, dynaform__name=dynaform_name
    )
    data = {
        "DYFORM_BASE_TEMPLATE": DEFAULT_DYFORM_BASE_TEMPLATE,
        "dynaform_data": dynaform_data_record,
        "dynaform": dynaform_data_record.dynaform,
        "edit": request.resolver_match.url_name == "dynaform-data-edit",
    }
    form = forms.DynaFormData(
        dynaform_data_record.dynaform.structure, request.POST or None
    )
    if request.POST:
        if data["edit"]:
            if form.is_valid():
                dynaform_data_record.data = form.cleaned_data
                dynaform_data_record.save()
        else:
            dynaform_data_record.delete()
            return redirect("dynaform-data-list", dynaform_name=dynaform_name)
    else:
        form.data = dynaform_data_record.data
    data["form"] = form
    return render(request, "dynaform/dynaform-data-edit.html", data)
