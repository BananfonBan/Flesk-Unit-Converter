from flask import Flask, request, render_template
from .converter import (UnitsWeightType,
                        UnitsLengthType,
                        UnitsTemperatureType,
                        convert_weight,
                        convert_length,
                        convert_temperature)

app = Flask(__name__)

# TODO
# - Make automatic tests
# - Set up commands for Makefile


@app.route("/")
def home():
    return render_template('base.html')


@app.get('/weight')
def get_weight_converter():
    return render_template(
        'weight.html',
        UnitsWeightType=UnitsWeightType
    )


@app.post('/weight')
def post_weight_converter():
    request_data = request.form.to_dict()
    input_value = request_data['value']
    input_measure = request_data['from_unit']
    output_measure = request_data['to_unit']
    rounding = request.form.get('rounding', type=int)
    errors = {}
    errors.update(validate_value(value=input_value))
    if not errors:
        errors.update(validate_weight(value=float(input_value)))

    response_dict = {
        'UnitsWeightType': UnitsWeightType,
        'input_value': input_value,
        'input_measure': input_measure,
        'output_measure': output_measure,
        'rounding': rounding
    }

    if errors:
        return render_template(
            'weight.html',
            **response_dict,
            errors=errors
        ), 422

    result = convert_weight(
        input_value=float(input_value),
        input_measure=input_measure,
        output_measure=output_measure,
        rounding=rounding)

    return render_template(
        'weight.html',
        **response_dict,
        result=result
    )


@app.get('/length')
def get_length_converter():
    return render_template(
        'length.html',
        UnitsLengthType=UnitsLengthType
    )


@app.post('/length')
def post_length_converter():
    request_data = request.form.to_dict()
    input_value = request_data['value']
    input_measure = request_data['from_unit']
    output_measure = request_data['to_unit']
    rounding = request.form.get('rounding', type=int)
    errors = {}
    errors.update(validate_value(value=input_value))
    if not errors:
        errors.update(validate_length(value=float(input_value)))

    response_dict = {
        'UnitsLengthType': UnitsLengthType,
        'input_value': input_value,
        'input_measure': input_measure,
        'output_measure': output_measure,
        'rounding': rounding
    }

    if errors:
        return render_template(
            'length.html',
            **response_dict,
            errors=errors
        ), 422

    result = convert_length(
        input_value=float(input_value),
        input_measure=input_measure,
        output_measure=output_measure,
        rounding=rounding)

    return render_template(
        'length.html',
        **response_dict,
        result=result
    )


@app.get('/temperature')
def get_temperature_converter():
    return render_template(
        'temperature.html',
        UnitsTemperatureType=UnitsTemperatureType
    )


@app.post('/temperature')
def post_temperature_converter():
    request_data = request.form.to_dict()
    input_value = request_data['value']
    input_measure = request_data['from_unit']
    output_measure = request_data['to_unit']
    rounding = request.form.get('rounding', type=int)
    errors = {}
    errors.update(validate_value(value=input_value))
    if not errors:
        errors.update(valid_temperature(value=float(input_value), measure=input_measure)) # noqa E501

    response_dict = {
        'UnitsTemperatureType': UnitsTemperatureType,
        'input_value': input_value,
        'input_measure': input_measure,
        'output_measure': output_measure,
        'rounding': rounding
    }

    if errors:
        return render_template(
            'temperature.html',
            **response_dict,
            errors=errors
        ), 422

    result = convert_temperature(
        input_value=float(input_value),
        input_measure=input_measure,
        output_measure=output_measure,
        rounding=rounding)

    return render_template(
        'temperature.html',
        **response_dict,
        result=result
    )


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


if __name__ == 'main':
    app.run(debug=True)
