from django import template


register = template.Library()

def id_for_label(form, field_name):
    return form.auto_id % field_name


register.filter('id_for_label', id_for_label)


def form_field(form, field):
    return form.fields[field].widget.render(field, form.data.get(field))


register.filter('form_field', form_field)


def field_label(form, field):
    return form.fields[field].label or field.capitalize()


register.filter('field_label', field_label)


def field_errors(form, field):
    return form.errors.get(field) or ''


register.filter('field_errors', field_errors)


@register.inclusion_tag('link_to_dynaform_data_edit.html', takes_context=True)
def link_to_dynaform_data_edit(context, dynaform_data):
    return {
        'form_name': dynaform_data.dynaform.name,
        'record_id': dynaform_data.id,
        'edit_mode': 'edit' in context["request"].GET,
    }


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)