from flask import Flask, request, render_template
from converter import (UnitsWeightType,
                       UnitsLengthType,
                       convert_weight,
                       convert_length)

app = Flask(__name__)


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
    errors = validate(value=input_value)

    if errors:
        return render_template(
            'weight.html',
            UnitsWeightType=UnitsWeightType,
            input_value=input_value,
            input_measure=input_measure,
            output_measure=output_measure,
            errors=errors
        )

    result = convert_weight(
        input_value=float(input_value),
        input_measure=input_measure,
        output_measure=output_measure)

    return render_template(
        'weight.html',
        UnitsWeightType=UnitsWeightType,
        input_value=input_value,
        input_measure=input_measure,
        output_measure=output_measure,
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
    errors = validate(value=input_value)

    if errors:
        return render_template(
            'length.html',
            UnitsWeightType=UnitsLengthType,
            input_value=input_value,
            input_measure=input_measure,
            output_measure=output_measure,
            errors=errors
        )

    result = convert_length(
        input_value=float(input_value),
        input_measure=input_measure,
        output_measure=output_measure)

    return render_template(
        'length.html',
        UnitsLengthType=UnitsLengthType,
        input_value=input_value,
        input_measure=input_measure,
        output_measure=output_measure,
        result=result
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        password = request.form['password']
        print(password)
        # проверка логина и пароля
        return 'Вы вошли в систему!'
    else:
        return render_template('login.html')


@app.route("/length")
def length():
    return render_template("length.html")


def validate(value):
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
