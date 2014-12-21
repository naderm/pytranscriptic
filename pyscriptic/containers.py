
from collections import namedtuple

from pytranscriptic import settings, submit

# Note: All volumes are in microliters
ContainerProperties = namedtuple(
    "ContainerProperties",
    ["title", "max_capacity", "dead_volume", "capabilities"],
    )

CONTAINERS = {
    "96-pcr": ContainerProperties(
        "96 well V-bottom (PCR) plate",
        160, 15,
        ["pipette", "sangerseq", "spin", "thermocycle", "incubate", "gel_separate"],
        ),
    "96-flat": ContainerProperties(
        "96 well flat-bottom optically clear plate",
        360, 20,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "96-flat-uv": ContainerProperties(
        "96 well flat-bottom UV transparent plate",
        360, 20,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "96-deep": ContainerProperties(
        "96 well flat-bottom extended capacity optically opaque plate",
        2000, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "384-pcr": ContainerProperties(
        "384 well V-bottom (PCR) plate",
        50, 8,
        ["pipette", "sangerseq", "spin", "thermocycle", "incubate", "gel_separate"],
        ),
    "384-flat": ContainerProperties(
        "384 well flat-bottom optically clear plate",
        112, 12,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "pcr-0.5": ContainerProperties(
        "0.5 mL PCR tube",
        500, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "micro-1.5": ContainerProperties(
        "1.5 mL microtube",
        1500, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "micro-2.0": ContainerProperties(
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
