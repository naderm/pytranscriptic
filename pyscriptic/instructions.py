
# Reference: https://www.transcriptic.com/platform/#instructions
# XXX: Class Operation?

# Liquid Handling
# Note: all speeds are in microliters per second
def mix_op(volume, speed=None, repetitions=None):
    pass

def transfer_op(from_well, to_well, volume,
                aspiration_speed=None, dispense_speed=None,
                mix_before=None, mix_after=None):
    pass

def distribute_op(from_well, to_wells, aspire_speed=None):
    pass

def consolidate_op(to_well, from_wells, dispense_speed=None,
                   mix_before=None):
    pass

def mix_well_op(well, volume, speed=None, repetitions=None):
    """
    Default speed is 50 microliters per second
    """
    pass

# Covers and Sealing
def cover_op():
    pass

def uncover_op():
    pass

def seal_op():
    pass

def unseal_op():
    pass

# DNA Sequencing
def sangerseq_op():
    pass

# Centrifugation
def spin_op(object, speed, duration):
    assert speed <= 4000
    pass

# Thermocycling
def thermocycle_op(object, volume):
    pass

# Incubation
def incubation_op():
    pass

# Spectrophotometry
def absorbance_op():
    pass

def fluorescence_op():
    pass

def luminscence_op():
    pass

# Gel Electrophoresis
def gel_separate_op():
    pass

# Flow Cytometry (Coming Soon)

# Liquid Chromatography (Coming soon)

# Mass Spectrometry (Coming soon)
