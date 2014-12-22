# Conversion of https://www.transcriptic.com/guides/1-pcr.html

from pyscriptic.protocols import Protocol, submit_protocol
from pyscriptic.instructions import UncoverOp, CoverOp, SealOp, ThermocycleOp, \
     ThermocycleStep, ThermocycleGroup, PipetteOp, TransferGroup
from pyscriptic.refs import Reference

refs = {
    "input_plate": Reference(container_id="ct15jdnddeaj", store_where="cold_20"),
    "pcr_plate": Reference(new="96-pcr", store_where="cold_20"),
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
    ThermocycleOp(
        "pcr_plate",
        # Note: The volume is not given in the original guide
        volume="4:microliter",
        groups=[
            ThermocycleGroup(
                cycles=1,
                steps=[
                    ThermocycleStep(duration="30:second", temperature="98:celsius"),
                ],
            ),
            ThermocycleGroup(
                cycles=35,
                steps=[
                    ThermocycleStep(duration="10:second", temperature="98:celsius"),
                    ThermocycleStep(duration="55:second", temperature="72:celsius"),
                ],
            ),
            ThermocycleGroup(
                cycles=1,
                steps=[
                    ThermocycleStep(duration="420:second", temperature="72:celsius"),
                    ThermocycleStep(duration="600:second", temperature="12:celsius"),
                ],
            ),
        ],
    ),
]

submit_protocol(Protocol(refs, instructions))
