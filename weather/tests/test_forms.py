from django.test import TestCase

from ..models import Location

from ..forms import LocationForm


class LocationFormTest(TestCase):
    def test_location_is_created_by_name(self):
        data = {'name': 'Moscow'}
        location = LocationForm(data)
        location.save()
        self.assertEqual(Location.objects.count(), 1)