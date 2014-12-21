
from pyscriptic.containers import CONTAINERS
from pyscriptic.storage import STORAGES

class Reference:
    def __init__(container_id=None, new=None, store=None, discard=False):
        assert (container_id is not None) != (new is not None)
        assert (store is not None) != (discard)
        assert store in STORAGES.keys() + [None]
        assert new in CONTAINERS.keys() + [None]
        # XXX: Check container id?
        self.container_id = container_id
        self.new = new
        self.store = store
        self.discard = discard

    # XXX: Convert to json somehow...
