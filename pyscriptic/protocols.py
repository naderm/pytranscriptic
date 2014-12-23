
from pyscriptic import runs

class Protocol(object):
    """
    Attributes
    ----------
    refs : list of pyscriptic.refs.Reference
    instructions : list of pyscriptic.instructions.Operation
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
    protocol : pyscriptic.protocols.Protocol or dict
    title : str, optional
    dry_run : bool, optional

    Returns
    -------
    pyscryptic.runs.RunProperties

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
