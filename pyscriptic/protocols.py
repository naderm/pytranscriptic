"""
Protocols build upon instructions, allowing users to list the liquid
transfer, processing, and measurement steps used to construct an entire
experiment.

Please note that this library does not perform any protocol
validations. Protocols are only validated for correctness after they are
submitted to run on Transcriptic's platform.
"""
from pyscriptic import runs

class UnboundProtocol(object):
    """
    Unbound protocols include a list of instructions, but no links between the
    container names listed in the instructions and the physical containers to
    create or available in storage on Transcriptic's platform.

    Attributes
    ----------
    instructions : list of :class:`pyscriptic.instructions.Operation`
    refs : set of str
    """
    def __init__(self, instructions):
        self.instructions = instructions
        self.refs = set(i.get_container_refs() for i in instructions)

    def bind_protocol(self, refs):
        """
        Binds a protocol to a list of references, linking an abstract
        description of an experiment to one that can run on Transcriptic's
        platform.

        Parameters
        ----------
        refs : dict of str, :class:`pyscriptic.refs.Reference`

        Returns
        -------
        :class:`pyscriptic.protocols.Protocol`
        """
        for name in self.refs:
            if name not in refs:
                raise KeyError("Missing link for container name: {}"
                               .format(name))

        return Protocol(
            refs=refs,
            instructions=self.instructions,
            )

class Protocol(object):
    """
    Protocols are composed of a list of instructions, along with a mapping of
    container names to the containers IDs available in storage.

    Attributes
    ----------
    refs : dict of str, :class:`pyscriptic.refs.Reference`
    instructions : list of :class:`pyscriptic.instructions.Operation`

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#protocols
    """
    def __init__(self, refs, instructions):
        self.refs = refs
        self.instructions = instructions

def submit_protocol(protocol, title="PyTranscript Run", dry_run=False):
    """
    Submits a protocol to run on Transcript's platform. A protocol is made up of
    a list of references, linking container names to the actual aliquots in
    storage / to be stored on completion. High-level API requests can also use
    this function by supplying the dict returned by one of the other functions
    in this module.

    Parameters
    ----------
    protocol : :class:`pyscriptic.protocols.Protocol` or dict
    title : str, optional
    dry_run : bool, optional

    Returns
    -------
    :class:`pyscryptic.runs.RunProperties`

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#protocols
    """
    return runs.run(
        protocol,
        title=title,
        dry_run=dry_run,
    )

def synthesize_oligo(name, sequence, purity, scale):
    """
    Returns a protocol to synthesizes a short oligonuclotide of < 200 bases.

    Parameters
    ----------
    name : str
    sequence : str
    purity : str
    scale : str
    dry_run : bool, optional

    Returns
    -------
    dict

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#ordering_assembly
    """
    assert all(i in "actg" for i in sequence)
    assert purity in ["desalt", "hplc", "page"]
    assert scale in ["25:nanomole", "50:nanomole", "200:nanomole",
                     "1:micromole", "10:micromole"]

    request = {
        "type": "oligo",
        "name": name,
        "data": {
            "sequence": sequence,
            "purity": purity,
            "scale": scale,
        },
    }
    return request

def synthesize_dsdna(name, sequence):
    """
    Synthesizes a longer stretch of dsDNA, up to 3 kb in size.

    Parameters
    ----------
    name : str
    sequence : str

    Returns
    -------
    dict

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#ordering_assembly
    """
    assert all(i in "actg" for i in sequence)

    request = {
        "type": "synthesize",
        "name": name,
        "data": {
            "sequence": sequence,
        },
    }
    return request

# Implementation awaiting further documentation
def synthesize_plasmid():
    """
    Not yet implemented.
    """
    raise NotImplementedError
