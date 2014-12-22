
from pyscriptic import settings, submit

class DataProperties(object):
    """
    Attributes
    ----------
    id : str
    device_class : str
    device_id : str
    dimensionality : int
    size : int
    data : list
    """
    def __init__(self, data_id, device_class, device_id, dimensionality,
                 size, data):
        self.data_id = data_id
        self.device_class = device_class
        self.device_id = device_id
        self.dimensionality = dimensionality
        self.size = size
        self.data = data

def get_run_data(run_id):
    """
    Get data generated by a given run.

    Parameters
    ----------
    run_id : str

    Returns
    -------
    pyscriptic.data.DataProperties
    """
    url = "{}/{}/runs/{}/data".format(
        settings.get_organization(),
        settings.get_project(),
        run_id,
        )
    response = submit.get_request(
        url,
        )
    return DataProperties(
        data_id=response["id"],
        device_class=response["device_class"],
        device_id=response["device_id"],
        dimensionality=response["dimensionality"],
        size=response["size"],
        data=response["data"],
        )

# Get monitoring data (Coming soon)
