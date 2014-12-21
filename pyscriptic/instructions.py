
from pyscriptic.storage import STORAGES
# Reference: https://www.transcriptic.com/platform/#instructions
class Operation:
    pass

# Liquid Handling
# Note: all speeds are in microliters per second
class PrePostMix:
    def __init__(self, volume, speed=None, repetitions=None):
        pass

class TransferOp(Operation):
    op = "transfer"

    def __init__(self, from_well, to_well, volume,
                 aspiration_speed=None, dispense_speed=None,
                 mix_before=None, mix_after=None):
        pass

class DistributeOp(Operation):
    op = "distribute"

    def __init__(self, from_well, to_wells, aspire_speed=None):
        pass

class ConsolidateOp(Operation):
    op = "consolidate"

    def __init__(self, to_well, from_wells, dispense_speed=None,
                 mix_before=None):
        pass

class MixOp(Operation):
    op = "mix"

    def __init__(self, well, volume, speed=None, repetitions=None):
        """
        Default speed is 50 microliters per second
        """
        pass

# Covers and Sealing
class CoverOp(Operation):
    op = "cover"

    def __init__(self, container, lid):
        assert lid in ["standard", "universal", "low_evaporation"]
        self.object = container
        self.lid = lid

class UncoverOp(Operation):
    op = "uncover"

    def __init__(self, container):
        self.container = container

class SealOp(Operation):
    op = "seal"

    def __init__(self, container):
        self.container = container

class UnsealOp(Operation):
    op = "unseal"

    def __init__(self, container):
        self.container = container

# DNA Sequencing
class SangerSeqOp(Operation):
    op = "sangerseq"

    def __init__(self, container, dataref):
        self.container = container
        self.dataref = dataref

# Centrifugation
class SpinOp(Operation):
    op = "spin"

    def __init__(self, container, speed, duration):
        assert speed <= 4000
        self.object = container
        self.speed = speed
        self.duration = duration

# Thermocycling
class ThermocycleOp(Operation):
    op = "thermocycle"

    def __init__(self, container, volume):
        self.container = container
        self.volume = volume

# Incubation
class IncubateOp(Operation):
    op = "incubate"

    def __init__(container, where, duration, shaking):
        assert where in STORAGES.keys()
        self.container = container
        self.where = where
        self.duration = duration
        self.shaking = shaking

# Spectrophotometry
class AbsorbanceOp(Operation):
    op = "absorbance"

    def __init__(self, container, wells, wavelength, dataref,
                 num_flashes=None):
        """
        Wavelength in nanometers
        num_flashes default is 25
        """
        self.object = container
        self.wells = wells
        self.wavelength = wavelength
        self.num_flashes = num_flashes
        self.dataref = dataref

class FluorescenceOp(Operation):
    op = "fluorescence"

    def __init__(self, container, wells, excitation, emission, dataref,
                 num_flashes=None):
        self.object = container
        self.wells = wells
        self.excitation = excitation
        self.emission = emission
        self.num_flashes = num_flashes
        self.dataref = dataref

class LuminescenceOp(Operation):
    op = "luminescence"

    def __init__(self, container, wells, dataref):
        """
        Measures all emissions in the range of 380 nm to 600 nm.
        """
        self.object = container
        self.wells = wells
        self.dataref = dataref

# Gel Electrophoresis
class GelSeparateOp(Operation):
    op = "gel_sperate"

    def __init__(self, wells, matrix, ladder, duration, dataref):
        assert matrix in ["agarose(96,2.0%)",
                          "agarose(48,4.0%)",
                          "agarose(48,2.0%)",
                          "agarose(12,1.2%)",
                          "agarose(8,0.8%)",]
        assert ladder in ["ladder1", "ladder2"]
        self.objects = wells
        self.matrix = matrix
        self.ladder = ladder
        self.duration = duration
        self.dataref = dataref

# Flow Cytometry (Coming Soon)

# Liquid Chromatography (Coming soon)

# Mass Spectrometry (Coming soon)
