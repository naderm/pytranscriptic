# Conversion of https://www.transcriptic.com/guides/1-pcr.html

from pyscriptic.protocols import submit_protocol
from pyscriptic.instructions import *
from pyscriptic.refs import Reference

refs = {
    "input_plate": Reference(container_id="ct15jdnddeaj", store="cold_20"),
    "pcr_plate": Reference(new="96-pcr", store="cold_20"),
}

instructions = [
    UncoverOp("input_plate"),
    PipetteOp([
        TransferGroup(
            from_well="input_plate/A1", to_well="pcr_plate/A1",
            volume="4:microliter",
        ),
    ]),
    CoverOp("input_plate", lid="standard"),
    SealOp("pcr_plate"),
    ThermocycleOp("pcr_plate"),
]

submit_protocol(refs, instructions)
