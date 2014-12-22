
from unittest import TestCase

from pyscriptic.instructions import PipetteOp, PrePostMix, TransferGroup, \
     DistributeGroup, ConsolidateGroup, MixGroup
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
        op = PipetteOp(
            groups=[
                DistributeGroup(
                    to_wells=[
                        dict(well="plate/A2", volume="10:microliter",
                             aspirate_speed="1:microliter/second"),
                        dict(well="plate/A3", volume="15:microliter",
                             aspirate_speed="3:microliter/second"),
                    ],
                    from_well="plate/A1",
                    aspirate_speed="2:microliter/second",
                    mix_after=self.mix,
                ),
            ],
        )
        self.assertEqual(
            pyobj_to_std_types(op),
            {
                "op": "pipette",
                "groups": [{
                    "distribute": [{
                        "from": "plate/A1",
                        "to": [
                            {
                                "well": "plate/A2",
                                "volume": "10:microliter",
                                "aspirate_speed": "1:microliter/second",
                            },
                            {
                                "well": "plate/A3",
                                "volume": "15:microliter",
                                "aspirate_speed": "3:microliter/second",
                            },
                        ],
                        "aspirate_speed": "2:microliter/second",
                        "mix_after": {
                            "volume": "5:microliter",
                            "speed": "0.5:microliter/second",
                            "repetitions": 10,
                        },
                    }]
                }],
            },
        )

    def test_consolidate(self):
        op = PipetteOp(
            groups=[
                ConsolidateGroup(
                    from_wells=[
                        dict(well="plate/A2", volume="10:microliter",
                             aspirate_speed="1:microliter/second"),
                        dict(well="plate/A3", volume="15:microliter",
                             aspirate_speed="3:microliter/second"),
                    ],
                    to="plate/A1",
                    dispense_speed="2:microliter/second",
                    mix_before=self.mix,
                ),
            ],
        )
        self.assertEqual(
            pyobj_to_std_types(op),
            {
                "op": "pipette",
                "groups": [{
                    "consolidate": [{
                        "to": "plate/A1",
                        "from": [
                            {
                                "well": "plate/A2",
                                "volume": "10:microliter",
                                "aspirate_speed": "1:microliter/second",
                            },
                            {
                                "well": "plate/A3",
                                "volume": "15:microliter",
                                "aspirate_speed": "3:microliter/second",
                            },
                        ],
                        "dispense_speed": "2:microliter/second",
                        "mix_before": {
                            "volume": "5:microliter",
                            "speed": "0.5:microliter/second",
                            "repetitions": 10,
                        },
                    }]
                }],
            },
        )

    def test_mix(self):
        op = PipetteOp(
            groups=[
                MixGroup(
                    well="plate/A1",
                    volume="20:microliter",
                    speed="1:microliter/second",
                    repetitions=10,
                ),
            ],
        )
        self.assertEqual(
            pyobj_to_std_types(op),
            {
                "op": "pipette",
                "groups": [{
                    "mix": [{
                        "well": "plate/A1",
                        "volume": "20:microliter",
                        "speed": "1:microliter/second",
                        "repetitions": 10,
                    }]
                }],
            },
        )
