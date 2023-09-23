from django.http import HttpResponse
from django.shortcuts import render

from dynaform.service import DynaFormContext


def home(request) -> HttpResponse:
    context = {
        'dynaform': DynaFormContext()
    }
    return render(request, "home.html", context=context)
