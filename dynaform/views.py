# -*- coding: utf-8 -*-
##############################################################################
#
#    KiddosDjango,
#    Copyright (C) 2020 Loghman Barari (<https://github.com/loghmanb/KiddosDjango>).
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

from django.shortcuts import get_object_or_404, render
from django.template.response import TemplateResponse

from . import models, forms


def dynaform_data_list(request, form_name):
    dynaform = models.DynaForm.objects.get(name=form_name)
    columns = list(dynaform.structure.keys())
    rows = models.DynaFormData.objects.filter(dynaform_id=dynaform.id)
    return TemplateResponse(request, 'dynaform-data-list.html', 
                            {
                                'columns': columns, 
                                'rows': rows
                            })


def dynaform_data(request, form_name, id):
    dynaform_data_record = get_object_or_404(models.DynaFormData, pk=id)
    data = {'dynaform_data': dynaform_data_record}
    data["dynaform"] = dynaform_data_record.dynaform
    form = forms.DynaFormData(
        dynaform_data_record.dynaform.structure, 
        request.POST or None)
    if request.POST:
        if form.is_valid():
            dynaform_data_record.data = form.cleaned_data
            dynaform_data_record.save()
    else:
        form.data = dynaform_data_record.data
    data['form'] = form
    return render(request, 'dynaform-data-edit.html', data)
