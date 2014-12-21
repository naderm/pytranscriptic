# Conversion of https://www.transcriptic.com/guides/0-getting-started.html

from pyscriptic.protocols import synthesize_oligo

synthesize_oligo(
    name="pri1-F",
    sequence="acgtagtcgagtctgagtcagcgtacgtag",
    purity="desalt",
    scale="20:nanomole",
)
