
from pyscriptic import settings, submit

class ProjectProperties(object):
    """

    Attributes
    ----------
    title : str
    organization : str
    runs : list of dict of str, str
    """
    def __init__(self, title, organization, runs=None):
        if runs is None:
            runs = []
        self.title = title
        self.organization = organization
        self.runs = runs

def create_project(project_id):
    """
    Creates a new project within the currently active organization.

    Parameters
    ----------
    project_id : str

    Returns
    -------
    pyscriptic.project.ProjectProperties
    """
    url = "{}".format(
        settings.get_organization(),
        )
    content = {
        "name": project_id,
        }
    response = submit.post_request(
        url,
        content,
        )
    return ProjectProperties(
        title=response["title"],
        organization=response["organization"]["id"],
        )
