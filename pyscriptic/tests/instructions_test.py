
from unittest import TestCase

from pyscriptic.instructions import PipetteOp, TransferGroup, PrePostMix
from pyscriptic.submit import pyobj_to_std_types

class PipetteOpTests(TestCase):
    def setUp(self):
        self.mix = PrePostMix(
            volume="5:microliter",
            speed="0.5:microliter/second",
            repetitions=10,
        )

    def test_transfer(self):
        op = PipetteOp(
            groups=[
                TransferGroup(
                    from_well="plate/A1",
                    to_well="plate/A2",
                    volume="20:microliter",
                    aspirate_speed="1:microliter/second",
                    dispense_speed="2:microliter/second",
                    mix_before=self.mix,
                    mix_after=self.mix,
                ),
            ],
        )
        self.assertEqual(
            pyobj_to_std_types(op),
            {
                "op": "pipette",
                "groups": [{
                    "transfer": [{
                        "from": "plate/A1",
                        "to": "plate/A2",
                        "volume": "20:microliter",
                        "aspirate_speed": "1:microliter/second",
                        "dispense_speed": "2:microliter/second",
                        "mix_after": {
                            "volume": "5:microliter",
                            "speed": "0.5:microliter/second",
                            "repetitions": 10,
                        },
                        "mix_before": {
                            "volume": "5:microliter",
                            "speed": "0.5:microliter/second",
                            "repetitions": 10,
                        },
                    }]
                }],
            },
        )

    def test_distribute(self):
        pass

    def test_consolidate(self):
        pass

    def test_mix(self):
        pass
