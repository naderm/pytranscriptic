
def _check_measurement(measurement, allowed_units):
    quantity, unit = measurement.split(":", 1)
    return unit in allowed_units and \
      quantity.isdigit()

def check_volume(volume):
    return _check_measurement(
        volume,
        ["nanoliter", "microliter", "milliliter"],
        )

def check_duration(duration):
    return _check_measurement(
        duration,
        ["millisecond", "second", "minute", "hour"],
        )

def check_speed(speed):
    return _check_measurement(
        speed,
        ["rpm"],
        )

def check_length(length):
    return _check_measurement(
        length,
        ["nanometer"],
        )

def check_temperature(temperature):
    return _check_measurement(
        temperature,
        ["celcius"],
        )

def check_matter(matter):
    return _check_measurement(
        matter,
        ["nanomole", "micromole"],
        )

def check_flowrate(flowrate):
    return _check_measurement(
        flowrate,
        ["microliter/second"],
        )
