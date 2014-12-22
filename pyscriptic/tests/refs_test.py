
from unittest import TestCase

class RefsTests(TestCase):
    def test_import_module(self):
        from pyscriptic.refs import Reference

    def test_new_reference(self):
        from pyscriptic.refs import Reference
        from pyscriptic.containers import CONTAINERS
        from pyscriptic.storage import STORAGE_LOCATIONS

        for name in CONTAINERS.keys():
            Reference(
                new=name,
                discard=True,
            )

        for name in STORAGE_LOCATIONS.keys():
            Reference(
                new="96-pcr",
                store_where=name,
                )
