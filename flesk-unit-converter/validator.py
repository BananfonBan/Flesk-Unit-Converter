from .converter import UnitsTemperatureType


def validate_value(value):
    errors = {}
    if not value:
        errors['empty_input'] = 'Value cannot be empty'
    try:
        float(value)
    except ValueError:
        errors['not_valid_input'] = 'Value must be a number'
    return errors


def validate_weight(value):
    errors = {}
    if value < 0:
        errors['negative_weight'] = 'Weight cannot be negative'
    return errors


def validate_length(value):
    errors = {}
    if value < 0:
        errors['negative_length'] = 'Length cannot be negative'
    return errors


def valid_temperature(value, measure):
    errors = {}
    if measure == UnitsTemperatureType.KELVIN and not valid_temperature_in_kelvin(value): # noqa E501
        errors['kelvin_lower_absolute_zero'] = 'The temperature value in Kelvin cannot be lower 0' # noqa E501
    if measure == UnitsTemperatureType.CELSIUS and not valid_temperature_in_celsius(value): # noqa E501
        errors['celsius_lower_absolute_zero'] = 'The temperature value in Celsius cannot be lower -273.15' # noqa E501
    if measure == UnitsTemperatureType.FAHRENHEIT and not valid_temperature_in_fahrenheit(value): # noqa E501
        errors['fahrenehit_lower_absolute_zero'] = 'The temperature value in Fahrenheit cannot be lower -473.15' # noqa E501
    return errors


def valid_temperature_in_kelvin(value):
    if value < 0:
        return False
    return True


def valid_temperature_in_celsius(value):
    if value < -273.15:
        return False
    return True


def valid_temperature_in_fahrenheit(value):
    if value < -459.67:
        return False
    return True
