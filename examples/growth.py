# Conversion of https://www.transcriptic.com/guides/3-growth-curves.html

from pyscriptic import settings
from pyscriptic.protocols import Protocol, submit_protocol
from pyscriptic.instructions import IncubateOp, AbsorbanceOp
from pyscriptic.refs import Reference

# Email and key can be set here, too, or read from environmental variables
settings.PROJECT = "Project Name"
settings.ORGANIZATION = "Organization Name"

refs = {
    "my_plate": Reference(container_id="ct1553vwp7p46", store_where="cold_20"),
}

incubate = IncubateOp(
    "my_plate",
    where="warm_37",
    shaking=True,
    duration="60:minute",
)

instructions = []

for i in range(5):
    instructions.append(incubate)
    absorbance = AbsorbanceOp(
        "my_plate",
        wells=["A1"],
        wavelength="600:nanometer",
        dataref=str(i), # Store the absorbance data with a different
                        # reference each round
    )
    instructions.append(absorbance)

submit_protocol(Protocol(refs, instructions))
