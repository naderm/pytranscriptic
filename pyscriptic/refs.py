
from pyscriptic.containers import CONTAINERS
from pyscriptic.storage import STORAGE_LOCATIONS

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

    def __init__(self, container_id=None, new=None, store_where=None, discard=False):
        assert (container_id is not None) != (new is not None)
        assert (store_where is not None) != (discard)
        assert store_where in STORAGE_LOCATIONS.keys() or store_where is None
        assert new in CONTAINERS.keys() or new is None

        # XXX: Check container id?
        self.container_id = container_id
        self.new = new
        self.store = {"where": store_where}
        self.discard = discard

    # XXX: Convert to json somehow...
