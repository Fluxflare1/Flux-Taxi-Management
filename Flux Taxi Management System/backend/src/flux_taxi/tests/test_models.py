# flux_taxi/tests/test_models.py
from django.test import TestCase
from .models import YourModel

class YourModelTests(TestCase):
    def test_example(self):
        instance = YourModel.objects.create(field='value')
        self.assertEqual(instance.field, 'value')
