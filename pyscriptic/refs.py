
from pyscriptic.containers import CONTAINERS, list_containers
from pyscriptic.storage import STORAGE_LOCATIONS

_AVAILABLE_CONTAINERS_IDS = None


def _available_container_ids():
    """
    This helper function fetchs a list of all containers available to the
    currently active organization. It then stores the container IDs so that we
    can compare against them later when creating new References.

    Returns
    -------
    set of str
    """

    global _AVAILABLE_CONTAINERS_IDS

    if _AVAILABLE_CONTAINERS_IDS is not None:
        return _AVAILABLE_CONTAINERS_IDS

    _AVAILABLE_CONTAINERS_IDS = set(i.container_id for i in list_containers())
    return _AVAILABLE_CONTAINERS_IDS


class Reference(object):
    """
    Contains the information to either create or link a given container to a
    reference through a protocol via an intermediate name.

    Attributes
    ----------
    container_id : str
    new : str
    store : dict of str, str
    discard bool

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_access
    """

    def __init__(self, container_id=None, new=None, store_where=None,
                 discard=False):
        assert (container_id is not None) != (new is not None)
        assert (store_where is not None) != (discard)
        assert store_where in STORAGE_LOCATIONS.keys() or store_where is None
        assert new in CONTAINERS.keys() or new is None

        if container_id is not None:
            assert container_id in _available_container_ids()

        self.container_id = container_id
        self.new = new
        self.store = {"where": store_where}
        self.discard = discard
