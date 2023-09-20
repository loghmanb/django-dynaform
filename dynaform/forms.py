from django.forms import Form, Field

from .const import *


def create_form_field(
        structure, 
        default_field_class=DEFAULT_FIELD_CLASS,
        field2class_mapper=DEFAULT_FIELD_TO_CLASS_MAPPER,
        text_field_widget=TEXT_FIELD_WIDGET) -> Field:
    field_type = structure.pop(FIELD_TYPE)
    if field_type == TEXT_FIELD and structure.get(FIELD_WIDGET) is None:
        structure[FIELD_WIDGET] = text_field_widget()
    elif field_type == BOOLEAN_FIELD:
        structure[FIELD_REQUIRED] = False
    klass = field2class_mapper.get(field_type, default_field_class)
    return klass(**structure)


class DynaForm(Form):
    def __init__(self, structure, *args, **kwargs):
        super(DynaForm, self).__init__(*args, **kwargs)

        for field_stru in structure:
            field_name = field_stru.pop(FIELD_NAME)
            self.fields[field_name] = create_form_field(field_stru)
