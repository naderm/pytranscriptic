
from pyscriptic import settings, submit

def create_project(project_id):
    url = "{}".format(
        settings.get_organization(),
        )
    content = {
        "name": project_id,
        }
    return submit.post_request(
        url,
        content,
        )
