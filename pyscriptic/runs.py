
from pyscriptic import settings, submit

def run(request, title="PyTranscript Run"):
    url = "{}/{}/runs".format(
        settings.get_organization(),
        settings.get_project(),
        )
    content = {
        "title": title,
        "request": request,
        }
    run_id = submit.post_request(
        url,
        content,
        )["id"]
    return run_id

def get_run(run_id):
    url = "{}/{}/runs/{}".format(
        settings.get_organization(),
        settings.get_project(),
        run_id,
        )
    return submit.get_request(
        url,
        )

def get_run_data(run_id):
    url = "{}/{}/runs/{}/data".format(
        settings.get_organization(),
        settings.get_project(),
        run_id,
        )
    return submit.get_request(
        url,
        )

def list_runs():
    url = "{}/{}".format(
        settings.get_organization(),
        settings.get_project(),
        )
    return submit.get_request(
        url,
        )
