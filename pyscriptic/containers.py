
from collections import namedtuple

from pytranscriptic import settings, submit

# Note: All volumes are in microliters
Container = namedtuple(
    "Container",
    ["title", "max_capacity", "dead_volume", "capabilities"],
    )

CONTAINERS = {
    "96-pcr": Container(
        "96 well V-bottom (PCR) plate",
        160, 15,
        ["pipette", "sangerseq", "spin", "thermocycle", "incubate", "gel_separate"],
        ),
    "96-flat": Container(
        "96 well flat-bottom optically clear plate",
        360, 20,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "96-flat-uv": Container(
        "96 well flat-bottom UV transparent plate",
        360, 20,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "96-deep": Container(
        "96 well flat-bottom extended capacity optically opaque plate",
        2000, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "384-pcr": Container(
        "384 well V-bottom (PCR) plate",
        50, 8,
        ["pipette", "sangerseq", "spin", "thermocycle", "incubate", "gel_separate"],
        ),
    "384-flat": Container(
        "384 well flat-bottom optically clear plate",
        112, 12,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "pcr-0.5": Container(
        "0.5 mL PCR tube",
        500, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "micro-1.5": Container(
        "1.5 mL microtube",
        1500, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "micro-2.0": Container(
        "2.0 mL microtube",
        2000, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
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
