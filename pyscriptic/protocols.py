
from pyscriptic import runs

def submit_protocol(refs, instructions, title="PyTranscript Run"):
    request = {
        "refs": refs,
        "instructions": instructions,
    }
    runs.run(
        request,
        title=title,
    )

def synthesize_oligo(name, sequence, purity, scale):
    assert purity in ["desalt", "hplc", "page"]
    assert scale in ["25:nanomole", "50:nanomole", "200:nanomole",
                     "1:micromole", "10:micromole"]

    title = "Synthesize {}".format(name)
    request = {
        "type": "oligo",
        "name": name,
        "data": {
            "sequence": sequence,
            "purity": purity,
            "scale": scale,
        },
    }
    runs.run(
        request,
        title=title,
    )

def synthesize_dsdna(name, sequence):
    title = "Synthesize {}".format(name)
    request = {
        "type": "synthesize",
        "name": name,
        "data": {
            "sequence": sequence,
        },
    }
    runs.run(
        request,
        title=title,
    )

# Implementation awaiting further documentation
def synthesize_plasmid():
    pass
