
import requests, json

from pyscriptic import settings

def _get_headers():
    """
    Gets all headers needed to access Transcriptic's services.

    Returns
    -------
    dict of str, str
    """
    return {
        "X-User-Email": settings.get_email(),
        "X-User-Token": settings.get_key(),
        "Content-Type": "application/json",
        "Accept": "application/json",
        }

def get_request(relative_url):
    """
    Sends a GET request (along will all necessary headers) to Transcript's
    servers to a url relative to the base url of the service. Returns the json
    response from the server.

    Parameters
    ----------
    relative_url : str

    Returns
    -------
    str
    """
    url = "{}/{}".format(
        settings.get_base_url(),
        relative_url,
        )
    response = requests.get(
        url,
        headers=_get_headers(),
        )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            json.dumps(response.json(), indent=2)
            )

def post_request(relative_url, content):
    """
    Sends a POST request (along will all necessary headers) to Transcript's
    servers to a url relative to the base url of the service. Also sends
    content, a payload that should be in json format, and returns the json
    response.

    Parameters
    ----------
    relative_url : str
    content : str

    Returns
    -------
    str
    """
    url = "{}/{}".format(
        settings.get_base_url(),
        relative_url,
        )
    response = requests.post(
        url,
        content,
        headers=_get_headers(),
        )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            json.dumps(response.json(), indent=2)
            )
