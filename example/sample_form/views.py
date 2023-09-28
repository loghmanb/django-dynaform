from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from dynaform.service import DynaFormContext


def home(request: HttpRequest) -> HttpResponse:
    """Homepage."""
    context = {"dynaform": DynaFormContext()}
    return render(request, "home.html", context=context)
