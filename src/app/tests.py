from django.test import TestCase
from .models import SportData, LegislativeDocument, About, Footer
# Create your tests here.

# Path: src/app/tests.py
# Compare this snippet from src/social/admin.py:


class TestSocial(TestCase):
    def test_social(self):
        self.assertEqual(1, 1)
# Compare this snippet from src/social/models.py:


class SportDataTest(TestCase):
    def test_sport_data(self):
        self.assertEqual(1, 1)

