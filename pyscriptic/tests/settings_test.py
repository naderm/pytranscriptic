
from unittest import TestCase

from pyscriptic import settings

class PipetteOpTests(TestCase):
    def test_base_url(self):
        settings.BASE_URL = "base/url"
        self.assertEqual(
            settings.get_base_url(),
            "base/url",
        )

    def test_email():
        pass

    def test_key():
        pass

    def test_organization():
        pass

    def test_project():
        pass
