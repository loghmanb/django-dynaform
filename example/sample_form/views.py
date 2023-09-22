from django.shortcuts import render

from dynaform.service import DynaFormContext

def home(request):
    context = {
        'dynaform': DynaFormContext()
    }
    return render(request, "home.html", context=context)
