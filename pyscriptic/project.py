
from pyscriptic import settings, submit

def create_project(project_id):
    """
    Creates a new project within the currently active organization.

    Parameters
    ----------
    project_id : str
    """
    url = "{}".format(
        settings.get_organization(),
        )
    content = {
        "name": project_id,
        }
    submit.post_request(
        url,
        content,
        )
