
from collections import namedtuple

from pyscriptic import settings, submit

# Note: All volumes are in microliters
ContainerType = namedtuple(
    "ContainerType",
    ["title", "wells", "max_well_capacity", "well_dead_volume", "capabilities"],
    )

CONTAINERS = {
    "96-pcr": ContainerType(
        "96 well V-bottom (PCR) plate",
        96, 160, 15,
        ["pipette", "sangerseq", "spin", "thermocycle", "incubate", "gel_separate"],
        ),
    "96-flat": ContainerType(
        "96 well flat-bottom optically clear plate",
        96, 360, 20,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "96-flat-uv": ContainerType(
        "96 well flat-bottom UV transparent plate",
        96, 360, 20,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "96-deep": ContainerType(
        "96 well flat-bottom extended capacity optically opaque plate",
        96, 2000, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "384-pcr": ContainerType(
        "384 well V-bottom (PCR) plate",
        384, 50, 8,
        ["pipette", "sangerseq", "spin", "thermocycle", "incubate", "gel_separate"],
        ),
    "384-flat": ContainerType(
        "384 well flat-bottom optically clear plate",
        384, 112, 12,
        ["pipette", "sangerseq", "spin", "absorbance", "fluorescence",
         "luminescence", "incubate", "gel_separate"],
        ),
    "pcr-0.5": ContainerType(
        "0.5 mL PCR tube",
        1, 500, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "micro-1.5": ContainerType(
        "1.5 mL microtube",
        1, 1500, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    "micro-2.0": ContainerType(
        "2.0 mL microtube",
        1, 2000, 15,
        ["pipette", "sangerseq", "spin", "incubate", "gel_separate"],
        ),
    }

class ContainerProperties(object):
    """

    Attributes
    ----------
    container_id : str
    location : str
    container_type : str
    well_count : int
    well_type : str
    well_depth_mm : int
    well_volume_ul : int
    well_coating : str
    sterile : bool
    device : ...
    aliquots : ...
    """
    def __init__(self, container_id, location, container_type, well_count,
                 well_type, well_depth_mm, well_volume_ul, well_coating,
                 sterile, device, aliquots):
        assert container_type in CONTAINERS.keys()

        self.container_id = container_id
        self.location = location
        self.container_type = container_type
        self.well_count = well_count
        self.well_type = well_type
        self.well_depth_mm = well_depth_mm
        self.well_volume_ul = well_volume_ul
        self.well_coating = well_coating
        self.sterile = sterile
        self.device = device
        self.aliquots = aliquots

def get_container(container_id):
    """
    Retrieves information about a given container available within the currently
    active organization.

    Parameters
    ----------
    container_id : str

    Returns
    -------
    pyscriptic.containers.ContainerProperties

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#containers_show
    """
    url = "{}/containers/{}".format(
        settings.get_organization(),
        container_id,
        )
    response = submit.get_request(
        url,
        )
    return ContainerProperties(
        **response
        )

def list_containers():
    """
    Lists all containers available within the currently active organization.

    Returns
    -------
    list of pyscriptic.containers.ContainerProperties

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#containers_index
    """
    url = "containers"
    response = submit.get_request(
        url,
        )
    return [
        ContainerProperties(**i)
        for i in response
        ]

def mail_container(container_id, address_id, condition):
    """
    Sends a request to mail a container to a given address.

    Parameters
    ----------
    container_id : str
    address_id : str
    condition : str

    Returns
    -------
    id : str

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
    response = submit.post_request(
        url,
        content,
        )
    return response["id"]
