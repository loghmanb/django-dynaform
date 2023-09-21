from django.db import models
from django.utils.translation import gettext_lazy as _


class DynaForm(models.Model):

    name = models.CharField(_('Name'), max_length=50, null=False)
    structure = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.name


class DynaFormData(models.Model):

    dynaform = models.ForeignKey(DynaForm, on_delete=models.CASCADE)
    data = models.JSONField()
    list_order = models.IntegerField()
