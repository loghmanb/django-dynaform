class DynaForm(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(_('Name'), max_length=50, null=False)
    structure = models.JSONField()

    def __str__(self) -> str:
        return self.name


class DynaFormData(models.Model):
    class Meta:
        abstract = True

    dynaform_id = models.IntegerField()
    data = models.JSONField()
    list_order = models.IntegerField()
