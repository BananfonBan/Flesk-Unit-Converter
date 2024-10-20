from enum import Enum


class UnitsWeightType(Enum):
    MILLIGRAM = 'Milligram'
    GRAM = 'Gram'
    KILOGRAM = 'Kilogram'
    OUNCE = 'Ounce'
    POUND = 'Pound'


def convert_weight(input_value: float, input_measure: UnitsWeightType, output_measure: UnitsWeightType) -> float:  # noqa E501
    weight_units = {
        "Milligram": 0.000001,
        "Gram": 0.001,
        "Kilogram": 1,
        "Ounce": 0.02835,
        "Pound": 0.453592
    }
    value_in_kilogram = input_value * weight_units[input_measure]
    converted_value = value_in_kilogram / weight_units[output_measure]
    return round(converted_value, 3)


def convert_length(input_value: float, input_measure: str, output_measure: str) -> float:  # noqa 501
    length_units = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }
    value_in_meters = input_value * length_units[input_measure]
    converted_value = value_in_meters / length_units[output_measure]
    return round(converted_value, 3)


def convert_temperature(input_value: float, input_measure: str, uotput_measure: str) -> float: # noqa 501
    convert_to_kevin = {
        "Celsius": celsius_to_kelvin(input_value),
        "Fahrenheit": fahrenheit_to_kelvin(input_value),
        "Kelvin": input_value
    }
    temperature_in_kelvin = convert_to_kevin[input_measure]
    convert_kelvin_to = {
        "Celsius": kelvin_to_celsius(temperature_in_kelvin),
        "Fahrenheit": kelvin_to_fahrenheit(temperature_in_kelvin),
        "Kelvin": temperature_in_kelvin
    }
    converted_value = convert_kelvin_to[uotput_measure]
    return round(converted_value, 3)


def kelvin_to_celsius(value):
    return value - 273.15


def kelvin_to_fahrenheit(value):
    return (value * 9) / 5 - 459.67


def celsius_to_kelvin(value):
    return value + 273.15


def fahrenheit_to_kelvin(value):
    return (value + 459.67) * 5 / 9
