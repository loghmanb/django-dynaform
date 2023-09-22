from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class DynaForm(models.Model):

    name = models.CharField(_('Name'), max_length=50, null=False, blank=False, unique=True)
    label = models.CharField(_('Label'), max_length=50, null=False, blank=False)
    structure = models.JSONField(default=dict)

    def clean(self):
        self.name = self.name.strip().replace(" ", "_").replace("-", "_")
        if not self.name.isidentifier():
            raise ValidationError({
                "name": f"'{self.name}' is NOT a valid identifier!"
                })
        
    def __str__(self) -> str:
        return f"{self.label} [{self.name}]"


class DynaFormData(models.Model):

    dynaform = models.ForeignKey(DynaForm, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)
    list_order = models.IntegerField()
