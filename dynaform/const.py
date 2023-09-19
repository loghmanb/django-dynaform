from django import forms


TEXT_FIELD = "text"
BOOLEAN_FIELD = "bool"
CHAR_FIELD = "char"
CHOICE_FIELD = "choice"


FIELD_NAME = "name"
FIELD_TYPE = "type"
FIELD_WIDGET = "widget"
FIELD_REQUIRED = "required"


DEFAULT_FIELD_CLASS = forms.CharField

TEXT_FIELD_WIDGET = forms.Textarea

DEFAULT_FIELD_TO_CLASS_MAPPER = {
    CHAR_FIELD: forms.CharField,
    CHOICE_FIELD: forms.ChoiceField,
    BOOLEAN_FIELD: forms.BooleanField,
}
