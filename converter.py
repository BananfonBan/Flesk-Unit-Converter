from enum import Enum


class UnitsWeightType(str, Enum):
    MILLIGRAM = 'Milligram'
    GRAM = 'Gram'
    KILOGRAM = 'Kilogram'
    OUNCE = 'Ounce'
    POUND = 'Pound'


class UnitsLengthType(str, Enum):
    MILLIMETER = "Millimeter"
    CENTIMETER = "Centimeter"
    METER = "Meter"
    KILOMETER = "Kilometer"
    INCH = "Inch"
    FOOT = "Foot"
    YARD = "Yard"
    MILE = "Mile"


class UnitsTemperatureType(str, Enum):
    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"
    KELVIN = "Kelvin"


def convert_weight(
        input_value: float,
        input_measure: UnitsWeightType,
        output_measure: UnitsWeightType
        ) -> float:

    weight_units = {
        UnitsWeightType.MILLIGRAM: 0.000001,
        UnitsWeightType.GRAM: 0.001,
        UnitsWeightType.KILOGRAM: 1,
        UnitsWeightType.OUNCE: 0.02835,
        UnitsWeightType.POUND: 0.453592
    }
    value_in_kilogram = input_value * weight_units[input_measure]
    converted_value = value_in_kilogram / weight_units[output_measure]
    return round(converted_value, 3)


def convert_length(
        input_value: float,
        input_measure: UnitsLengthType,
        output_measure: UnitsLengthType
        ) -> float:

    length_units = {
        UnitsLengthType.MILLIMETER: 0.001,
        UnitsLengthType.CENTIMETER: 0.01,
        UnitsLengthType.METER: 1,
        UnitsLengthType.KILOMETER: 1000,
        UnitsLengthType.INCH: 0.0254,
        UnitsLengthType.FOOT: 0.3048,
        UnitsLengthType.YARD: 0.9144,
        UnitsLengthType.MILE: 1609.34
    }
    value_in_meters = input_value * length_units[input_measure]
    converted_value = value_in_meters / length_units[output_measure]
    return round(converted_value, 3)


def convert_temperature(
        input_value: float,
        input_measure: UnitsTemperatureType,
        output_measure: UnitsTemperatureType
        ) -> float:

    convert_to_kevin = {
        UnitsTemperatureType.CELSIUS: celsius_to_kelvin(input_value),
        UnitsTemperatureType.FAHRENHEIT: fahrenheit_to_kelvin(input_value),
        UnitsTemperatureType.KELVIN: input_value
    }
    temperature_in_kelvin = convert_to_kevin[input_measure]
    convert_kelvin_to = {
        UnitsTemperatureType.CELSIUS: kelvin_to_celsius(temperature_in_kelvin),
        UnitsTemperatureType.FAHRENHEIT: kelvin_to_fahrenheit(temperature_in_kelvin), # noqa E501
        UnitsTemperatureType.KELVIN: temperature_in_kelvin
    }
    converted_value = convert_kelvin_to[output_measure]
    return round(converted_value, 3)


def kelvin_to_celsius(value):
    return value - 273.15


def kelvin_to_fahrenheit(value):
    return (value * 9) / 5 - 459.67


def celsius_to_kelvin(value):
    return value + 273.15


def fahrenheit_to_kelvin(value):
    return (value + 459.67) * 5 / 9
