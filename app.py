from flask import Flask, request, render_template
from converter import UnitsWeightType, convert_weight

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
    errors = validate_weight(value=input_value)

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


def validate_weight(value):
    errors = {}
    if not value:
        errors['weight'] = ('Value can not be empty')
    return errors


if __name__ == 'main':
    app.run(debug=True)
