
from unittest import TestCase

class RunsTests(TestCase):
    def test_import_module(self):
        from pyscriptic.runs import RunProperties, run, list_runs, get_run

    def test_new_run_properties(self):
        from pyscriptic.runs import RunProperties
        RunProperties(
            run_id="1234",
            title="Run Title",
            status="active",
            )

    def test_run(self):
        pass

    def test_list_runs(self):
        pass

    def test_get_run(self):
        pass
