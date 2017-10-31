import django
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class ViewTest(TestCase):

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()
            cls.u1 = User.objects.create_user(username='testclient', password='password')

    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_login_and_logout(self):
        response = self.client.get('/homepage/')
        self.assertRedirects(response, '/?next=/homepage/')
        self.client.force_login(self.u1)
        response = self.client.get('/homepage/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].username, 'testclient')
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/')
