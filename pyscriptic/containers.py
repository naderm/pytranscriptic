
from collections import namedtuple

from pyscriptic import settings, submit

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
    """
    Retrieves information about a given container available within the currently
    active organization.

    Parameters
    ----------
    container_id : str

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#containers_show
    """
    url = "{}/containers/{}".format(
        settings.get_organization(),
        container_id,
        )
    return submit.get_request(
        url,
        )

def list_containers():
    """
    Lists all containers available within the currently active organization.

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#containers_index
    """
    url = "containers"
    return submit.get_request(
        url,
        )

def mail_container(container_id, address_id, condition):
    """
    Sends a request to mail a container to a given address.

    Parameters
    ----------
    container_id : str
    address_id : str
    condition : str

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_storage
    """
    assert condition in ["ambient", "dry_ice"]
    url = "{}/containers/{}/mail".format(
        settings.get_organization(),
        container_id,
        )
    content = {
        "address": address_id,
        "condition": condition,
        }
    return submit.post_request(
        url,
        content,
        )
