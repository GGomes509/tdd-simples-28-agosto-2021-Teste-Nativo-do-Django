from django.test import TestCase, RequestFactory
from buscar.views import home

class TestHomeUrls(TestCase):

    def setUp(self):
        self.factury = RequestFactory()

    def test_UrlsAppBuscar(self):
        request = self.factury.get('/')
        with self.assertTemplateUsed('home.html'):
            response = home(request)
            self.assertEqual(response.status_code, 200)