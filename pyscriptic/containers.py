
import requests, json

from pytranscriptic import settings, submit

# key: type-code
# value: [max_capacity (microliter), dead_volume (microliter), capabilities]
CONTAINERS = {
    "96-pcr": [160, 15, []],
    "96-flat": [360, 20, []],
    "96-flat-uv": [360, 20, []],
    "96-deep": [2000, 15, []],
    "384-pcr": [50, 8, []],
    "384-flat": [112, 12, []],
    "pcr-0.5": [500, 15, ["pipette", "sangerseq", "spin", "incubate",
                          "gel_separate"]],
    "micro-1.5": [1500, 15, ["pipette", "sangerseq", "spin", "incubate",
                             "gel_separate"]],
    "micro-2.0": [2000, 15, ["pipette", "sangerseq", "spin", "incubate",
                             "gel_separate"]]
    }

def get_container(container_id):
    url = "{}/containers/{}".format(
        settings.get_organization(),
        container_id,
        )
    return submit.get_request(
        url,
        )

def list_containers():
    url = "containers"
    return submit.get_request(
        url,
        )
