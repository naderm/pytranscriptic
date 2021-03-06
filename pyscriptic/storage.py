"""
Describes the list of storage options available for containers.

Notes
-----
.. [1] https://www.transcriptic.com/platform/#instr_storage
"""


class StorageType(object):
    """
    Attributes
    ----------
    description : str
    """
    def __init__(self, description):
        self.description = description


STORAGE_LOCATIONS = {
    "ambient": StorageType(
        "may vary between 19.5 degC and 22 degC",
    ),
    "warm_37": StorageType(
        "may vary between 36 degC and 38 degC, optionally shaking",
    ),
    "cold_4": StorageType(
        "may vary between 3 degC and 5 degC",
    ),
    "cold_20": StorageType(
        "may vary between -22 degC and -18 degC",
    ),
    "cold_80": StorageType(
        "may vary between -84 degC and -76 degC",
    ),
}
