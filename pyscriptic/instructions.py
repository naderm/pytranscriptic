"""
Classes used to describe instructions that combine together to make a protocol.

Notes
-----
.. [1] https://www.transcriptic.com/platform/#instr_storage
"""

from inspect import ismethod, getmembers

from pyscriptic.storage import STORAGE_LOCATIONS
from pyscriptic.measures import check_volume, check_duration, check_speed, \
     check_length, check_temperature, check_flowrate

# Reference:
class Operation(object):
    """
    Abstract class used to describe a single operation (a.k.a instruction) used
    to build a larger protocol.

    Attributes
    ----------
    op : str
    """
    def to_dict(self):
        return dict(
            (key.rstrip("_"), getattr(self, key))
            for key, value in getmembers(
                self,
                lambda x: not ismethod(x) and x is not None,
                )
            if not key.startswith("_")
            )

# Liquid Handling
# Note: all speeds are in microliters per second
class PipetteOp(Operation):
    """
    Attributes
    ----------
    groups : list of pyscriptic.instructions.PipetteGroup

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_liquid_handling
    """
    op = "pipette"

    def __init__(self, groups):
        self.groups = groups

class PrePostMix(object):
    """
    Describes a mixing operation before a transfer commences.

    Attributes
    ----------
    volume : str
    speed : str
    repetitions : int
    """
    def __init__(self, volume, speed=None, repetitions=None):
        assert check_volume(volume)
        assert speed is None or check_flowrate(speed)

        self.volume = volume
        self.speed = speed
        self.repetitions = repetitions

class PipetteGroup(object):
    """
    Abstract class used to describe a group of pipetting operations to occur
    using a single tip.
    """
    pass

class TransferGroup(PipetteGroup):
    """
    Group used to describe a transfer operation, from one well to one well.

    Attributes
    ----------
    from_well : str
    to_well : str
    volume : str
    aspirate_speed : str
    dispense_speed : str
    mix_before : pyscriptic.instructions.PrePostMix
    mix_after : pyscriptic.instructions.PrePostMix

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_liquid_handling
    """
    op = "transfer"

    def __init__(self, from_well, to_well, volume,
                 aspirate_speed=None, dispense_speed=None,
                 mix_before=None, mix_after=None):
        assert check_volume(volume)
        assert aspirate_speed is None or check_flowrate(aspirate_speed)
        assert dispense_speed is None or check_flowrate(dispense_speed)

        self.from_ = from_well
        self.to = to_well
        self.volume = volume
        self.aspirate_speed = aspirate_speed
        self.dispense_speed = dispense_speed
        self.mix_before = mix_before
        self.mix_after = mix_after

class DistributeGroup(PipetteGroup):
    """
    Group used to describe a distribute operation, from one well to many wells.

    Attributes
    ----------
    from_well : str
    to_wells : list of dict of str, str
    aspire_speed : str
    mix_after : pyscriptic.instructions.PrePostMix

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_liquid_handling
    """
    op = "distribute"

    def __init__(self, from_well, to_wells, aspire_speed=None, mix_after=None):
        assert aspire_speed is None or check_flowrate(aspire_speed)

        self.from_ = from_well
        self.to = to_wells
        self.aspire_speed = aspire_speed
        self.mix_after = mix_after

class ConsolidateGroup(PipetteGroup):
    """
    Group used to describe a consolidate operation, from many wells to one well.

    Attributes
    ----------
    to_well : str
    from_wells : list of str
    dispense_speed : str
    mix_before : pyscriptic.instructions.PrePostMix

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_liquid_handling
    """
    op = "consolidate"

    def __init__(self, to_well, from_wells, dispense_speed=None,
                 mix_before=None):
        assert dispense_speed is None or check_flowrate(dispense_speed)

        self.to = to_well
        self.from_ = from_wells
        self.dispense_speed = dispense_speed
        self.mix_before = mix_before

class MixGroup(PipetteGroup):
    """
    Group used to describe a mix operation, all within one well.

    Attributes
    ----------
    well : str
    volume : str
    speed : str
    repetitions : int

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_liquid_handling
    """
    op = "mix"

    def __init__(self, well, volume, speed=None, repetitions=None):
        """
        Default speed is 50 microliters per second
        """
        assert check_volume(volume)
        assert speed is None or check_flowrate(speed)

        self.well = well
        self.volume = volume
        self.speed = speed
        self.repetitions = repetitions

# Covers and Sealing
class CoverOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_covers_and_seals
    """
    op = "cover"

    def __init__(self, container, lid):
        assert lid in ["standard", "universal", "low_evaporation"]

        self.object = container
        self.lid = lid

class UncoverOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_covers_and_seals
    """
    op = "uncover"

    def __init__(self, container):
        self.container = container

class SealOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_covers_and_seals
    """
    op = "seal"

    def __init__(self, container):
        self.container = container

class UnsealOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_covers_and_seals
    """
    op = "unseal"

    def __init__(self, container):
        self.container = container

# DNA Sequencing
class SangerSeqOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_sequencing
    """
    op = "sangerseq"

    def __init__(self, container, dataref):
        self.container = container
        self.dataref = dataref

# Centrifugation
class SpinOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_centrifugation
    """
    op = "spin"

    def __init__(self, container, speed, duration):
        assert speed <= 4000
        assert check_speed(speed)
        assert check_duration(duration)

        self.object = container
        self.speed = speed
        self.duration = duration

# Thermocycling
class ThermocycleOp(Operation):
    """

    Attributes
    ----------
    container : str
    volume : str
    groups : list of pyscriptic.instructions.ThermocycleGroup
    dyes : dict of str, list of str
    dataref : str
    melting : pyscriptic.instructions.MeltingStep
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_thermocycling
    """
    op = "thermocycle"

    def __init__(self, container, volume, groups, dyes=None, dataref=None, melting=None):
        assert check_volume(volume)

        self.container = container
        self.volume = volume
        self.groups = groups
        self.dyes = dyes
        self.dataref = dataref
        self.melting = melting

class ThermocycleGroup(object):
    """
    Attributes
    ----------
    cycles : int
    steps : list of pyscriptic.instructions.ThermocycleStep
    """
    def __init__(self, cycles, steps):
        self.cycles = cycles
        self.steps = steps

class ThermocycleStep(object):
    """
    Attributes
    ----------
    duration : str
    temperature : str
    read : bool
    """
    def __init__(self, duration, temperature, read=False):
        assert check_duration(duration)
        assert check_temperature(temperature)
        assert read in [True, False]

        self.duration = duration
        self.temperature = temperature
        self.read = read

class MeltingStep(object):
    """
    Optional melting step to run at the end of the protocol.

    Attributes
    ----------
    start : str
    end : str
    increment : str
    rate : str
    """
    def __init__(self, start, end, increment, rate):
        assert check_temperature(start)
        assert check_temperature(end)
        assert check_temperature(increment)
        assert check_duration(rate)

        self.start = start
        self.end = end
        self.increment = increment
        self.rate = rate

# Incubation
class IncubateOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_incubation
    """
    op = "incubate"

    def __init__(self, container, where, duration, shaking):
        assert where in STORAGE_LOCATIONS.keys()
        assert check_duration(duration)
        assert shaking in [True, False]

        self.container = container
        self.where = where
        self.duration = duration
        self.shaking = shaking

# Spectrophotometry
class AbsorbanceOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_spectroscopy
    """
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
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_spectroscopy
    """
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
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_spectroscopy
    """
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
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_electrophoresis
    """
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
class FlowCytometryOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_flow
    """
    op = "flow"

    def __init__(self):
        raise NotImplementedError

# Liquid Chromatography (Coming soon)
class HPLCOp(Operation):
    """
    High Performance Liquid Chromatography Operation

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_lc
    """
    op = "hplc"

    def __init__(self):
        raise NotImplementedError

class FPLCOp(Operation):
    """
    Fast Protein Liquid Chromatography Operation

    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_lc
    """
    op = "fplc"

    def __init__(self):
        raise NotImplementedError

# Mass Spectrometry (Coming soon)
class MassSpectrometryOp(Operation):
    """
    Notes
    -----
    .. [1] https://www.transcriptic.com/platform/#instr_mspec
    """
    op = "mspec-quad"

    def __init__(self):
        raise NotImplementedError
