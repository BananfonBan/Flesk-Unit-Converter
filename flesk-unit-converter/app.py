from flask import Flask, request, render_template
from .converter import (UnitsWeightType,
                        UnitsLengthType,
                        UnitsTemperatureType,
                        convert_weight,
                        convert_length,
                        convert_temperature)
from .validator import (validate_value,
                        validate_weight,
                        valid_temperature,
                        validate_length)


app = Flask(__name__)

# TODO
# - Make automatic tests


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


if __name__ == 'main':
    app.run(debug=True)
