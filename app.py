import streamlit as st

st.title("🧮 Simple Unit Converter")

# Conversion type selection
conversion_type = st.selectbox("Select conversion type:", ["Length", "Temperature", "Weight"])

# ===== LENGTH CONVERSION =====
if conversion_type == "Length":
    st.subheader("Length Converter")
    units = {
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Centimeters": 0.01,
        "Feet": 0.3048,
    }

    from_unit = st.selectbox("From:", units.keys(), key="length_from")
    to_unit = st.selectbox("To:", units.keys(), key="length_to")
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f", key="length_value")

    result = value * units[from_unit] / units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# ===== TEMPERATURE CONVERSION =====
elif conversion_type == "Temperature":
    st.subheader("Temperature Converter")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_from")
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"], key="temp_to")
    value = st.number_input("Enter temperature:", format="%.2f", key="temp_value")

    def convert_temp(val, from_u, to_u):
        if from_u == to_u:
            return val
        if from_u == "Celsius":
            return (val * 9/5 + 32) if to_u == "Fahrenheit" else (val + 273.15)
        elif from_u == "Fahrenheit":
            return (val - 32) * 5/9 if to_u == "Celsius" else (val - 32) * 5/9 + 273.15
        elif from_u == "Kelvin":
            return val - 273.15 if to_u == "Celsius" else (val - 273.15) * 9/5 + 32

    result = convert_temp(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# ===== WEIGHT CONVERSION =====
elif conversion_type == "Weight":
    st.subheader("Weight Converter")
    units = {
        "Kilograms": 1.0,
        "Grams": 0.001,
        "Pounds": 0.453592,
    }

    from_unit = st.selectbox("From:", units.keys(), key="weight_from")
    to_unit = st.selectbox("To:", units.keys(), key="weight_to")
    value = st.number_input("Enter weight:", min_value=0.0, format="%.2f", key="weight_value")

    result = value * units[from_unit] / units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
