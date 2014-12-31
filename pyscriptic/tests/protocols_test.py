
from unittest import TestCase

from pyscriptic.instructions import UncoverOp, PipetteOp, TransferGroup
from pyscriptic.protocols import UnboundProtocol

class ProtocolsTest(TestCase):
    def test_unbound_protocol_refs(self):
        instructions = [
            UncoverOp("input_plate"),
            PipetteOp([
                TransferGroup(
                    from_well="input_plate/A1",
                    to_well="pcr_plate/A1",
                    volume="4:microliter",
                    ),
            ]),
        ]
        unbound = UnboundProtocol(
            instructions=instructions,
        )
        self.assertEqual(
            unbound.refs,
            set(["input_plate", "pcr_plate"]),
        )

    def test_submit_protocol(self):
        pass

    def test_synthesize_oligo(self):
        pass

    def test_synthesize_dsdna(self):
        pass

    def test_synthesize_plasmid(self):
        pass
