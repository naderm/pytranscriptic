# Conversion of https://www.transcriptic.com/guides/0-getting-started.html

from pyscriptic.protocols import synthesize_oligo

synthesize_oligo(
    name="pri1-F",
    sequence="acgtagtcgagtctgagtcagcgtacgtag",
    purity="desalt",
    # In the guide, the scale is 20:nanomole, but the documentation does not list
    # this as a valid scale.
    # Reference: https://www.transcriptic.com/platform/#ordering_assembly
    scale="25:nanomole",
)
