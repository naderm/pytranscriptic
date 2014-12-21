# Conversion of https://www.transcriptic.com/guides/3-growth-curves.html

from pyscriptic.protocols import submit_protocol
from pyscriptic.instructions import IncubateOp, AbsorbanceOp
from pyscriptic.refs import Reference

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

submit_protocol(refs, instructions)
