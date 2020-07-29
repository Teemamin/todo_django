from django.test import TestCase
from .models import item

# Create your tests here.
# Testdjango inherits the built-in test case class.


class TestViews(TestCase):
    # every test inside this class will be defined as
    # a method and will strt with test in the name

    def test_todo(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'todo/todo.html')
        #  using the builtin HTTP client that comes with django
        #  testing framework: we set the var response to self client
        #  get the home page,assert its ok n assert the used templt

    def test_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_edit_item_page(self):
        itm = item.objects.create(name='testing edit')
        response = self.client.get(f'/edit/{itm.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'added from test'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        itm = item.objects.create(name='testing edit')
        response = self.client.get(f'/delete/{itm.id}')
        self.assertRedirects(response, '/')
        existing_item = item.objects.filter(id=itm.id)
        self.assertEqual(len(existing_item), 0)
        # Since that item is the only one on the database wit
        #  that id and we just deleted it.We can be certain the
        #  view works by asserting whether the length of existing
        #  items is zero.

    def test_can_toggle_item(self):
        itm = item.objects.create(name='testing edit', done=True)
        response = self.client.get(f'/toggle/{itm.id}')
        self.assertRedirects(response, '/')
        updated_item = item.objects.get(id=itm.id)
        self.assertFalse(updated_item.done)
        #  created an item with a done status of true.
        #  Then call the toggle URL on its ID.
        #  After asserting that the view redirects us.
        #  We can get the item again.
        #  And  called it updated_item.
        #  then use assertFalse to check it's done status.

    def test_can_edit_item(self):
        itm = item.objects.create(name='testing edit')
        response = self.client.post(f'/edit/{itm.id}',
                                    {'name': 'updated name'})
        self.assertRedirects(response, '/')
        updated_item = item.objects.get(id=itm.id)
        self.assertEqual(updated_item.name, 'updated name')
