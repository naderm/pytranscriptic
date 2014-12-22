
def _check_measurement(measurement, allowed_units):
    """
    Checks a measurement to ensure it's quantity is a number and its units are
    of allowed units.

    Parameters
    ----------
    measurement : str
    allowed_units : list of str
    """
    quantity, unit = measurement.split(":", 1)
    return unit in allowed_units and \
      quantity.isdigit()

def check_volume(volume):
    """
    Checks that a volume has a correct quantity and allowed units.

    Parameters
    ----------
    volume : str
    """
    return _check_measurement(
        volume,
        ["nanoliter", "microliter", "milliliter"],
        )

def check_duration(duration):
    """
    Checks that a duration has a correct quantity and allowed units.

    Parameters
    ----------
    duration : str
    """
    return _check_measurement(
        duration,
        ["millisecond", "second", "minute", "hour"],
        )

def check_speed(speed):
    """
    Checks that a speed has a correct quantity and allowed units.

    Parameters
    ----------
    speed : str
    """
    return _check_measurement(
        speed,
        ["rpm"],
        )

def check_length(length):
    """
    Checks that a length has a correct quantity and allowed units.

    Parameters
    ----------
    length : str
    """
    return _check_measurement(
        length,
        ["nanometer"],
        )

def check_temperature(temperature):
    """
    Checks that a temperature has a correct quantity and allowed units.

    Parameters
    ----------
    temperature : str
    """
    return _check_measurement(
        temperature,
        ["celsius"],
        )

def check_matter(matter):
    """
    Checks that a matter has a correct quantity and allowed units.

    Parameters
    ----------
    matter : str
    """
    return _check_measurement(
        matter,
        ["nanomole", "micromole"],
        )

def check_flowrate(flowrate):
    """
    Checks that a flowrate has a correct quantity and allowed units.

    Parameters
    ----------
    flowrate : str
    """
    return _check_measurement(
        flowrate,
        ["microliter/second"],
        )
