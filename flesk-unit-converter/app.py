from flask import Flask, request, render_template
from .converter import (convert_weight,
                        convert_length,
                        convert_temperature)
from .forms import WeightConverterForm, LengthConverterForm, TemperatureConverterForm
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template('base.html')


@app.route('/weight', methods=['GET', 'POST'])
def weight_converter():
    form = WeightConverterForm()
    if request.method == 'GET':
        return render_template('weight.html', form=form)
    if form.validate_on_submit():
        result = convert_weight(
            input_value=float(form.value.data),
            input_measure=form.input_measure.data,
            output_measure=form.output_measure.data,
            rounding=form.rounding.data
        )
        return render_template('weight.html', form=form, result=result)
    return render_template('weight.html', form=form), 422


@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    form = LengthConverterForm()
    if request.method == 'GET':
        return render_template('length.html', form=form)
    if form.validate_on_submit():
        result = convert_length(
            input_value=float(form.value.data),
            input_measure=form.input_measure.data,
            output_measure=form.output_measure.data,
            rounding=form.rounding.data
        )
        return render_template('length.html', form=form, result=result)
    return render_template('length.html', form=form), 422


@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    form = TemperatureConverterForm()
    if request.method == 'GET':
        render_template('temperature.html', form=form)
    if form.validate_on_submit():
        result = convert_temperature(
            input_value=float(form.value.data),
            input_measure=form.input_measure.data,
            output_measure=form.output_measure.data,
            rounding=form.rounding.data
        )
        return render_template('temperature.html', form=form, result=result)
    return render_template('temperature.html', form=form), 422


if __name__ == 'main':
    app.run(debug=True)
