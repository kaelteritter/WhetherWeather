from django.test import TestCase
from django.conf import settings

from ..utils import get_weather


class GetLocationWeatherTest(TestCase):
    def setUp(self):
        self.get_weather = get_weather

    def test_weather_got_by_location(self):
        result = self.get_weather(settings.OPEN_WEATHER_API_ID, 'Rome')
        self.assertEqual(result.get('cod'), 200)