
import requests, json

from pytranscriptic import settings

def get_request(relative_url):
    url = "{}/{}".format(
        settings.get_base_url(),
        relative_url,
        )
    response = requests.get(
        url,
        headers=settings.get_headers(),
        )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            json.dumps(response.json(), indent=2)
            )

def post_request(relative_url, content):
    url = "{}/{}".format(
        settings.get_base_url(),
        relative_url,
        )
    response = requests.post(
        url,
        content,
        headers=settings.get_headers(),
        )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            json.dumps(response.json(), indent=2)
            )
