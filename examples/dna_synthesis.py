# Conversion of https://www.transcriptic.com/guides/0-getting-started.html

from pyscriptic import settings
from pyscriptic.protocols import synthesize_oligo

# Email and key can be set here, too, or read from environmental variables
settings.PROJECT = "Project Name"
settings.ORGANIZATION = "Organization Name"

# The guide says they are making oligos, but use the call for dsdna...
synthesize_oligo(
    name="pri1-F",
    sequence="acgtagtcgagtctgagtcagcgtacgtag",
    purity="desalt",
    # In the guide, the scale is 20:nanomole, but the documentation does not list
    # this as a valid scale.
    # Reference: https://www.transcriptic.com/platform/#ordering_assembly
    scale="25:nanomole",
)
