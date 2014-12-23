# Conversion of https://www.transcriptic.com/guides/0-getting-started.html

from pyscriptic import settings
from pyscriptic.protocols import submit_protocol, synthesize_oligo

# Email and key can be set here, too, or read from environmental variables
settings.PROJECT = "Project_Name"
settings.ORGANIZATION = "Organization_Name"

# The guide says they are making oligos, but use the call for dsdna...
protocol = synthesize_oligo(
    name="pri1-F",
    sequence="acgtagtcgagtctgagtcagcgtacgtag",
    purity="desalt",
    # In the guide, the scale is 20:nanomole, but the documentation does not list
    # this as a valid scale.
    # Reference: https://www.transcriptic.com/platform/#ordering_assembly
    scale="25:nanomole",
)
submit_protocol(protocol, title="Synthesize pri1-F", dry_run=True)
