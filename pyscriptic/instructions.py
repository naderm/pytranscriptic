
from pyscriptic.storage import STORAGES
from pyscriptic.measures import check_volume, check_duration, check_speed, \
     check_length, check_temperature, check_matter, check_flowrate

# Reference: https://www.transcriptic.com/platform/#instructions
class Operation:
    def to_dict(self):
        return dict(
            (key.rstrip("_"), getattr(self, key))
            for key in dir(self)
            if not key.startswith("_") and getattr(self, key) is not None
            )

# Liquid Handling
# Note: all speeds are in microliters per second
class PipetteOp(Operation):
    op = "pipette"
    def __init__(self, groups):
        self.groups = groups

class PrePostMix:
    def __init__(self, volume, speed=None, repetitions=None):
        assert check_volume(volume)
        assert speed is None or check_flowrate(speed)

        self.volume = volume
        self.speed = speed
        self.repetitions = repetitions

class TransferGroup(Operation):
    op = "transfer"

    def __init__(self, from_well, to_well, volume,
                 aspirate_speed=None, dispense_speed=None,
                 mix_before=None, mix_after=None):
        assert check_volume(volume)
        assert aspirate_speed is None or check_speed(aspirate_speed)
        assert dispense_speed is None or check_speed(dispense_speed)

        self.from_ = from_well
        self.to = to_well
        self.volume = volume
        self.aspirate_speed = aspirate_speed
        self.dispense_speed = dispense_speed
        self.mix_before = mix_before
        self.mix_after = mix_after

class DistributeGroup(Operation):
    op = "distribute"

    def __init__(self, from_well, to_wells, aspire_speed=None):
        assert aspire_speed is None or check_speed(aspire_speed)

        self.from_ = from_well
        self.to = to_wells
        self.aspire_speed = aspire_speed

class ConsolidateGroup(Operation):
    op = "consolidate"

    def __init__(self, to_well, from_wells, dispense_speed=None,
                 mix_before=None):
        assert dispense_speed is None or check_speed(dispense_speed)

        self.to = to_well
        self.from_ = from_wells
        self.dispense_speed = dispense_speed
        self.mix_before = mix_before

class MixGroup(Operation):
    op = "mix"

    def __init__(self, well, volume, speed=None, repetitions=None):
        """
        Default speed is 50 microliters per second
        """
        assert check_volume(volume)
        assert speed is None or check_speed(speed)

        self.well = well
        self.volume = volume
        self.speed = speed
        self.repetitions = repetitions

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

    def __init__(self, container, volume, groups, dyes=None, dataref=None, melting=None):
        assert check_volume(volume)

        self.container = container
        self.volume = volume
        self.groups = groups
        self.dyes = dyes
        self.dataref = dataref
        self.melting = melting

class ThermocycleGroup:
    def __init__(self, cycles, steps):
        self.cycles = cycles
        self.steps = steps

class ThermocycleStep:
    def __init__(self, duration, temperature, read=False):
        assert check_duration(duration)
        assert check_temperature(temperature)
        assert read in [True, False]

        self.duration = duration
        self.temperature = temperature
        self.read = read

# Incubation
class IncubateOp(Operation):
    op = "incubate"

    def __init__(self, container, where, duration, shaking):
        assert where in STORAGES.keys()
        assert check_duration(duration)
        assert shaking in [True, False]

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
        assert check_length(wavelength)

        self.object = container
        self.wells = wells
        self.wavelength = wavelength
        self.num_flashes = num_flashes
        self.dataref = dataref

class FluorescenceOp(Operation):
    op = "fluorescence"

    def __init__(self, container, wells, excitation, emission, dataref,
                 num_flashes=None):
        assert check_length(excitation)
        assert check_length(emission)

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
        assert check_duration(duration)

        self.objects = wells
        self.matrix = matrix
        self.ladder = ladder
        self.duration = duration
        self.dataref = dataref

# Flow Cytometry (Coming Soon)

# Liquid Chromatography (Coming soon)

# Mass Spectrometry (Coming soon)
