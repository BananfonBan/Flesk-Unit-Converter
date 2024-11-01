from flask_wtf import FlaskForm
from wtforms import ValidationError, Field
from .converter import UnitsTemperatureType


def value_is_number(form: FlaskForm,
                    field: Field,
                    message: str = 'Value must be a number'):
    try:
        float(str(field.data))
    except ValueError:
        raise ValidationError(message)


def value_is_positive(message: str = None):
    if not message:
        message = 'Value must be a positive'

    def _positive(form: FlaskForm,
                  field: Field):
        if field.errors:
            return None
        value = float(str(field.data))
        if value < 0:
            raise ValidationError(message)

    return _positive


def valid_temperature_in_kelvin(value):
    if value < 0:
        raise ValidationError('The temperature value in Kelvin cannot be lower 0')


def valid_temperature_in_celsius(value):
    if value < -273.15:
        raise ValidationError('The temperature value in Celsius cannot be lower -273.15')


def valid_temperature_in_fahrenheit(value):
    if value < -459.67:
        raise ValidationError('The temperature value in Fahrenheit cannot be lower -459.67') # noqa E501


def valid_temperature(form: FlaskForm,
                      field: Field):
    if field.errors:
        return None
    measure = form.input_measure.data
    value = float(str(field.data))
    temp_validators = {
        UnitsTemperatureType.CELSIUS: valid_temperature_in_celsius,
        UnitsTemperatureType.FAHRENHEIT: valid_temperature_in_fahrenheit,
        UnitsTemperatureType.KELVIN: valid_temperature_in_kelvin,
    }
    temp_validators[measure](value)
