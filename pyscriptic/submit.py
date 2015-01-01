
from inspect import ismethod, getmembers
import requests
import json

from pyscriptic import settings


def pyobj_to_std_types(obj):
    """
    Recursively converts a python object to be a string, integer, list, or
    dict. Handles class instances intelligently by converting non-private,
    non-method attributes into a dict.

    Parameters
    ----------
    obj : int or str or list or dict or object

    Returns
    -------
    list or str or list or dict
    """
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, list):
        return [pyobj_to_std_types(i) for i in obj]
    elif isinstance(obj, dict):
        return {
            key: pyobj_to_std_types(val)
            for key, val in obj.items()
        }
    elif isinstance(obj, object):
        return {
            key.rstrip("_"): pyobj_to_std_types(getattr(obj, key))
            for key, value in getmembers(
                obj,
                lambda x: not ismethod(x) and x is not None,
                )
            if not key.startswith("_")
        }
    else:
        raise Exception(
            "Unable to convert type to standard type: {}".format(type(obj))
        )


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
        json.dumps(pyobj_to_std_types(content)),
        headers=_get_headers(),
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            json.dumps(response.json(), indent=2)
        )
