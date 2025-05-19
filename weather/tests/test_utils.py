from django.test import TestCase
from django.conf import settings

from ..utils import get_weather


class GetLocationWeather(TestCase):
    def setUp(self):
        self.get_weather = get_weather

    def test_weather_got_by_location(self):
        result = self.get_weather('Rome', settings.OPEN_WEATHER_API_ID)
        self.assertEqual(result.get('cod'), 200)