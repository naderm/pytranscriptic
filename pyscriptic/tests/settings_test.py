
from unittest import TestCase

from pyscriptic import settings

class PipetteOpTests(TestCase):
    def test_base_url(self):
        settings.BASE_URL = "base/url"
        self.assertEqual(
            settings.get_base_url(),
            "base/url",
        )

    def test_email(self):
        settings.TRANSCRIPTIC_EMAIL = "me@example.com"
        self.assertEqual(
            settings.get_email(),
            "me@example.com",
        )

    def test_key(self):
        settings.TRANSCRIPTIC_KEY = "SuPeRsEcReT"
        self.assertEqual(
            settings.get_key(),
            "SuPeRsEcReT",
        )

    def test_organization(self):
        settings.ORGANIZATION = "org"
        self.assertEqual(
            settings.get_organization(),
            "org",
        )

    def test_project(self):
        settings.PROJECT = "proj"
        self.assertEqual(
            settings.get_project(),
            "proj",
        )
