
from unittest import TestCase

from pyscriptic.instructions import PipetteOp, TransferGroup, PrePostMix

class PipetteOpTests(TestCase):
    def setUp(self):
        self.mix = PrePostMix(
            volume="5:microliter",
            speed="1:microliter/second",
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
                    dispense_speed="1:microliter/second",
                    mix_before=self.mix,
                    mix_after=self.mix,
                ),
            ],
        )

    def test_distribute(self):
        pass

    def test_consolidate(self):
        pass

    def test_mix(self):
        pass
