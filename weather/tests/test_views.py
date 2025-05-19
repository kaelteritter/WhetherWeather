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