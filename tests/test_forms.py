"""Test forms."""

import unittest

from django import forms

from dynaform import const
from dynaform.forms import DynaFormData, create_form_field


class TestCreateFormFieldMethod(unittest.TestCase):
    """Test create form field."""

    def test_create_char_field(self):
        """Test char field."""
        structure = {
            const.FIELD_TYPE: const.CHAR_FIELD,
            const.FIELD_REQUIRED: False,
        }
        field = create_form_field(structure)
        self.assertIsInstance(field, forms.CharField)
        self.assertFalse(field.required)

    def test_create_boolean_field(self):
        """Test boolean field."""
        structure = {
            const.FIELD_TYPE: const.BOOLEAN_FIELD,
        }
        field = create_form_field(structure)
        self.assertIsInstance(field, forms.BooleanField)
        self.assertFalse(field.required)


class TestDynaForm(unittest.TestCase):
    """Test DynaForm."""

    def test_create_form_for_dynaform_data(self):
        """Test create form for dynaform data."""
        structure = {
            "name": {const.FIELD_TYPE: const.CHAR_FIELD},
            "is_active": {const.FIELD_TYPE: const.BOOLEAN_FIELD},
        }
        dynaform_data = DynaFormData(structure, None)
        self.assertEqual(len(dynaform_data.fields), 2)
        self.assertIsInstance(dynaform_data.fields["name"], forms.CharField)
        self.assertIsInstance(dynaform_data.fields["is_active"], forms.BooleanField)

    def test_custom_create_field(self):
        """Test custom create form fields."""
        structure = {
            "name": {"type": "string"},
        }

        def custom_create_field(stru):
            new_stru = {}
            for f, d in stru.items():
                new_stru[f] = {}
                if d["type"] == "string":
                    new_stru[f][const.FIELD_TYPE] = const.CHAR_FIELD
            return create_form_field(new_stru)

        dynaform_data = DynaFormData(structure, None)
        self.assertEqual(len(dynaform_data.fields), 1)
        self.assertIsInstance(dynaform_data.fields["name"], forms.CharField)
