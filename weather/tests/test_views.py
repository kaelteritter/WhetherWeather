from django.test import Client, TestCase


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_weather_pops_up(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        data = {'name': 'Minsk'}
        response = self.client.get('/', data=data)
        self.assertIsNotNone(response.context.get('weather'))

    def test_custom_404_returned_when_no_result(self):
        response = self.client.get('/?name=bugaga')
        self.assertTrue(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')