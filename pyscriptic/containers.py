
from pyscriptic import settings, submit

class ContainerType(object):
    """
    Lists information about a particular container type, such as a 96-well
    plate.

    Attributes
    ----------
    title : str
    wells : int
        Number of wells in the container. Wells can be referenced using either
        a 1-indexed number (i.e. 1-96) or by row and column (i.e. A1-H12).
    max_well_capacity : float
        Max volume capacity for each well, in microliters.
    well_dead_volume : float
        Well dead volume, in microliters.
    capabilities : list of str
        List of supported instructions that can be performed on this container
        type.
    """
    def __init__(self, title, wells, max_well_capacity, well_dead_volume,
                 capabilities):
        self.title = title
        self.wells = wells
        self.max_well_capacity = max_well_capacity
        self.well_dead_volume = well_dead_volume
        self.capabilities = capabilities

class ContainerProperties(object):
    """
    Lists the properties about a particular instance of a container, such as
    where that container is stored and what liquids it contains.

    Attributes
    ----------
    container_id : str
    location : str
    container_type : pyscriptic.containers.ContainerType
    well_count : int
    well_type : str
    well_depth_mm : int
    well_volume_ul : int
    well_coating : str
    sterile : bool
    device : pyscriptic.containers.ContainerDevice
    aliquots : list of pyscriptic.containers.ContainerAliquot
    """
    def __init__(self, container_id, location, container_type, well_count,
                 well_type, well_depth_mm, well_volume_ul, well_coating,
                 sterile, device, aliquots):
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

class ContainerDevice(object):
    """
    Attributes
    ----------
    device_id : str
    name : str
    make : str
    model : str
    device_class : str
    """
    def __init__(self, device_id, name, make, model, device_class):
        self.device_id = device_id
        self.name = name
        self.make = make
        self.model = model
        self.device_class = device_class

class ContainerAliquot(object):
    """
    Attributes
    ----------
    aliquot_id : str
    volume_ul : float
    concentration_um : float
    mass_mg : float
    created_by_run_id : str
    well_idx : str
    """
    def __init__(self, aliquot_id, volume_ul, concentration_um, mass_mg,
                 created_by_run_id, well_idx):
        self.aliquot_id = aliquot_id
        self.volume_ul = volume_ul
        self.concentration_um = concentration_um
        self.mass_mg = mass_mg
        self.created_by_run_id = created_by_run_id
        self.well_idx = well_idx

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

def _device_from_response(response):
    """
    Parameters
    ----------
    response : dict of str, str

    Returns
    -------
    ContainerDevice
    """
    return ContainerDevice(
        device_id=response["id"],
        name=response["name"],
        make=response["make"],
        model=response["model"],
        device_class=response["device_class"],
    )

def _aliquot_from_response(response):
    """
    Parameters
    ----------
    response : dict

    Returns
    -------
    ContainerAliquot
    """
    return ContainerAliquot(
        aliquot_id=response["id"],
        volume_ul=response["volume_ul"],
        concentration_um=response["concentration_um"],
        mass_mg=response["mass_mg"],
        created_by_run_id=response["created_by_run_id"],
        well_idx=response["well_idx"],
    )

def _container_properties_from_response(response):
    """
    Parameters
    ----------
    dict

    Returns
    -------
    ContainerProperties
    """
    assert response["container_type"] in CONTAINERS.keys()

    return ContainerProperties(
        container_id=response["id"],
        location=response["location"],
        container_type=CONTAINERS[response["container_type"]],
        well_count=response["well_count"],
        well_type=response["well_type"],
        well_depth_mm=response["well_depth_mm"],
        well_volume_ul=response["well_volume_ul"],
        well_coating=response["well_coating"],
        sterile=response["sterile"],
        device=_device_from_response(response["device"]),
        aliquots=[_aliquot_from_response(i) for i in response["aliquots"]],
    )

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
    return _container_properties_from_response(response)

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
    return [_container_properties_from_response(i) for i in response]

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
