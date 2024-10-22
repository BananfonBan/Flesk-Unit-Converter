from flask import Flask, request, render_template
from converter import (UnitsWeightType,
                       UnitsLengthType,
                       UnitsTemperatureType,
                       convert_weight,
                       convert_length,
                       convert_temperature)

app = Flask(__name__)

# TODO
# - История запросов. Можно реализовать через Cookie или Сессии
# - Сделать авторматические тесты
# - Настроить Makefile
# - Добавить валидащию значений для температур (Не могут быть ниже абсолютного нуля)
# - Дабавить валидацию веса и длины (Не могут быть меньше 0)


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
    errors = validate_value(value=input_value)

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
    errors = validate_value(value=input_value)

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
    errors = validate_value(value=input_value)

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
        errors['empty_input'] = 'Value can not be empty'
    try:
        float(value)
    except ValueError:
        errors['not_valid_input'] = 'Value must be a number'
    return errors


if __name__ == 'main':
    app.run(debug=True)
