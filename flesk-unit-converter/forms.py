from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional
from .converter import UnitsWeightType, UnitsLengthType, UnitsTemperatureType
from .validator import value_is_number, value_is_positive, valid_temperature


class WeightConverterForm(FlaskForm):
    value = StringField(label='Value',
                        validators=[DataRequired(),
                                    value_is_number,
                                    value_is_positive(message='Weight cannot be negative')]) # noqa E501
    input_measure = SelectField(label='From',
                                choices=[weight.value for weight in UnitsWeightType])
    output_measure = SelectField(label='To',
                                 choices=[weight.value for weight in UnitsWeightType])
    rounding = IntegerField(label='Rounding', validators=[Optional()])
    submit = SubmitField(label='Convert')


class LengthConverterForm(FlaskForm):
    value = StringField(label='Value',
                        validators=[DataRequired(),
                                    value_is_number,
                                    value_is_positive(message='Length cannot be negative')]) # noqa E501
    input_measure = SelectField(label='From',
                                choices=[length.value for length in UnitsLengthType])
    output_measure = SelectField(label='To',
                                 choices=[length.value for length in UnitsLengthType])
    rounding = IntegerField(label='Rounding', validators=[Optional()])
    submit = SubmitField(label='Convert')


class TemperatureConverterForm(FlaskForm):
    input_measure = SelectField(label='From',
                                choices=[temperature.value for temperature in UnitsTemperatureType]) # noqa E501
    output_measure = SelectField(label='To',
                                 choices=[temperature.value for temperature in UnitsTemperatureType]) # noqa E501
    value = StringField(label='Value',
                        validators=[DataRequired(),
                                    value_is_number,
                                    valid_temperature])
    rounding = IntegerField(label='Rounding', validators=[Optional()])
    submit = SubmitField(label='Convert')
