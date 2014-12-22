
from unittest import TestCase

class ProjectTests(TestCase):
    def test_import_module(self):
        from pyscriptic.project import ProjectProperties, create_project, get_project

    def test_new_project_properties(self):
        from pyscriptic.project import ProjectProperties
        ProjectProperties(
            project_id="1234",
            title="Project Title",
            organization="Organization",
            runs=[{"id": "run1", "status": "active"}],
            )

    def test_create_project(self):
        pass

    def test_get_project(self):
        pass
