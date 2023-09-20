import unittest

from django import forms

from dynaform import const
from dynaform.forms import create_form_field


class TestCreateFormFieldMethod(unittest.TestCase):
    def test_create_form_field(self):
        structure = {
            const.FIELD_TYPE: const.CHAR_FIELD,
            }
        field = create_form_field(structure)
        self.assertIsInstance(field, forms.CharField)

    
class TestDynaForm(unittest.TestCase):
    def test_create_form(self):
        pass
