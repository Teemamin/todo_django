from django.test import TestCase
from .models import item


class Testmodel(TestCase):
    def test_to_done_default(self):
        itm = item.objects.create(name='test model')
        self.assertFalse(itm.done)

    def test_str_return_name(self):
        itm = item.objects.create(name='test model')
        self.assertEqual(str(itm), 'test model')
        #  used self.assertEqual to confirm that this name
        #  is returned when we render this item as a string.
