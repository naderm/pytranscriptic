
from pyscriptic.containers import CONTAINERS
from pyscriptic.storage import STORAGES

class Reference:
    def __init__(self, container_id=None, new=None, store_where=None, discard=False):
        assert (container_id is not None) != (new is not None)
        assert (store_where is not None) != (discard)
        assert store_where in STORAGES.keys() + [None]
        assert new in CONTAINERS.keys() + [None]

        # XXX: Check container id?
        self.container_id = container_id
        self.new = new
        self.store = {"where": store_where}
        self.discard = discard

    # XXX: Convert to json somehow...
