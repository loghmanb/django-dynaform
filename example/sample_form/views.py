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

from django.http import HttpRequest, HttpResponse
from django.template import Context, Template

from dynaform.service import DynaFormContext

from .models import Templates


def home(request: HttpRequest) -> HttpResponse:
    """Homepage."""
    context = Context({"dynaform": DynaFormContext(), "request": request})
    template_str = Templates.objects.get(name="home").template
    template = Template(template_str)
    return HttpResponse(template.render(context))
