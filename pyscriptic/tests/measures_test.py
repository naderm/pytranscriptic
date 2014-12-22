
from unittest import TestCase

from pyscriptic import measures

class CheckTests(TestCase):
    def test_check_volume(self):
        self.assertTrue(measures.check_volume("1:nanoliter"))
        self.assertTrue(measures.check_volume("0.5:microliter"))
        self.assertTrue(measures.check_volume("10:milliliter"))

        self.assertFalse(measures.check_volume("a:nanoliter"))
        self.assertFalse(measures.check_volume("1:femtoliter"))
        self.assertFalse(measures.check_volume("1:liter"))

    def test_check_duration(self):
        pass

    def test_check_speed(self):
        pass

    def test_check_length(self):
        pass

    def test_check_temperature(self):
        pass

    def test_check_matter(self):
        pass

    def test_check_flowrate(self):
        pass
