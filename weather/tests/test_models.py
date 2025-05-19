from django.test import TestCase

from ..models import Location


class LocationModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            name='London'
        )
    
    def test_model_has_string_representation(self):
        self.assertEqual(str(self.location), 'London')

    def test_model_has_verbose_name(self):
        ...