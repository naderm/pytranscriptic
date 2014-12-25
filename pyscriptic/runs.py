
from __future__ import print_function
import json

from pyscriptic import settings, submit, project

class RunProperties(object):
    """

    Attributes
    ----------
    run_id : str
    title : str
    status : str
    protocol : :class:`pyscriptic.protocols.Protocol`
    created_at : str
    warnings : list of dict of str, str
        Dicts each include the code and message for each error.
    errors : list of dict of str, str
        Dicts each include the code and message for each error.
    """
    def __init__(self, run_id, title, status, protocol=None,
                 created_at=None, warnings=None, errors=None):
        self.run_id = run_id
        self.title = title
        self.status = status
        self.protocol = protocol
        self.created_at = created_at
        self.warnings = warnings
        self.errors = errors

def run(request, title="PyTranscript Run", dry_run=False):
    """
    Submits a run request for the currently active project. The request should
    be in the form of a json description of the low or high-level protocol.

    Parameters
    ----------
    request : dict
    title : str, optional
    dry_run : bool, optional

    Returns
    -------
    :class:`pyscriptic.runs.RunProperties`
    """

    url = "{}/{}/runs".format(
        settings.get_organization(),
        settings.get_project(),
        )
    content = {
        "title": title,
        "request": request,
        }
    if dry_run:
        print("Posting to \"{}/{}\":".format(settings.get_base_url(), url))
        print(json.dumps(submit.pyobj_to_std_types(content), indent=2))
    else:
        response = submit.post_request(
            url,
            content,
            )
        return RunProperties(
            run_id=response["id"],
            title=response["title"],
            status=response["status"],
            warnings=response["warnings"],
            errors=response["errors"],
            )

def get_run(run_id):
    """
    Gets information about a single run within the currently active project.

    Parameters
    ----------
    run_id : str

    Returns
    -------
    :class:`pyscriptic.runs.RunProperties`
    """
    from pyscriptic.protocols import Protocol
    url = "{}/{}/runs/{}".format(
        settings.get_organization(),
        settings.get_project(),
        run_id,
        )
    response = submit.get_request(
        url,
        )
    return RunProperties(
        run_id=response["id"],
        title=response["title"],
        created_at=response["created_at"],
        status=response["status"],
        protocol=Protocol(
            refs=response["protocol"]["refs"],
            instructions=response["protocol"]["instructions"],
        ),
    )

def list_runs():
    """
    Lists all runs for the currently active project. Only returns run ids, run
    properties must be queried individually.

    Returns
    -------
    list of dict of str, str
        Includes the ids and statuses of all runs.
    """
    return project.get_project(settings.get_project()).runs
