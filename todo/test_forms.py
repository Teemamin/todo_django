from django.test import TestCase
from .forms import itemForm


class TestItemForms(TestCase):
    def test_done_field(self):
        form = itemForm({'name': 'test to do item'})
        #  form is calln on our formitem class and
        #  instantiating to simulate a user input
        self.assertTrue(form.is_valid())

    def test_name_field(self):
        form = itemForm({'name': ''})
        self.assertFalse(form.is_valid())
        #  it will assert that the form is not valid
        self.assertIn('name', form.errors.keys())
        #  whether or not there's a name key in the dictionary
        #  of form errors.
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        #  assertequal chks to see if the form error  msg in name field is
        #  this field is required
        #  note we're using the zero index here because the form will return
        #  a list of errors on each field.And this verifies that the first item
        #  in that list is our string telling us the field is required.

    def test_fiels_explicit_in_form_metaclass(self):
        form = itemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
