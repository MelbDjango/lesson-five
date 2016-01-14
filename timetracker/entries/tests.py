from django.test import TestCase, Client


class ViewTests(TestCase):

    def test_clients_available(self):
        c = Client()
        response = c.get('/clients/')
        self.assertEqual(response.status_code, 200)

    def test_entries_available(self):
        c = Client()
        response = c.get('/entries/')
        self.assertEqual(response.status_code, 200)

    def test_projects_available(self):
        c = Client()
        response = c.get('/projects/')
        self.assertEqual(response.status_code, 200)
