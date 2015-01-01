
from pyscriptic import settings, submit


class ProjectProperties(object):
    """

    Attributes
    ----------
    project_id : str
    title : str
    organization : str
    runs : list of dict of str, str
    """
    def __init__(self, project_id, title, organization, runs=None):
        if runs is None:
            runs = []
        self.project_id = project_id
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
    :class:`pyscriptic.project.ProjectProperties`

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#projects_creating
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
        project_id=response["project_id"],
        title=response["title"],
        organization=response["organization"]["id"],
    )


def get_project(project_id):
    """
    Lists all information about a given project.

    Parameters
    ----------
    project_id : str

    Returns
    -------
    :class:`pyscriptic.project.ProjectProperties`

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#projects_get
    """
    url = "{}/{}".format(
        settings.get_organization(),
        project_id,
    )
    response = submit.get_request(
        url,
    )
    return ProjectProperties(
        project_id=response["project_id"],
        title=response["title"],
        organization=response["organization"]["id"],
        runs=response["runs"],
    )
