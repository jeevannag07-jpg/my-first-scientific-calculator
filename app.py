import streamlit as st
from calculator import Calculator

calc = Calculator()

st.title("🧮 Scientific Calculator")

mode = st.radio("Choose mode", ["Basic", "Scientific"])

if mode == "Basic":
    a = st.number_input("First number", value=0.0)
    op = st.selectbox("Operator", ["+", "-", "*", "/"])
    b = st.number_input("Second number", value=0.0)

    if st.button("Calculate"):
        try:
            if op == "+": result = calc.add(a, b)
            elif op == "-": result = calc.subtract(a, b)
            elif op == "*": result = calc.multiply(a, b)
            elif op == "/": result = calc.divide(a, b)
            st.success(f"Result: {result}")
        except ValueError as e:
            st.error(str(e))

else:  # Scientific mode
    op = st.selectbox("Operation", ["√ Square Root", "x^y Power", "! Factorial", "sin", "cos", "log"])
    a = st.number_input("Enter number", value=0.0)
    b = None
    if op == "x^y Power":
        b = st.number_input("Enter power", value=2.0)

    if st.button("Calculate"):
        try:
            if op == "√ Square Root": result = calc.square_root(a)
            elif op == "x^y Power": result = calc.power(a, b)
            elif op == "! Factorial": result = calc.factorial(a)
            elif op == "sin": result = calc.sine(a)
            elif op == "cos": result = calc.cosine(a)
            elif op == "log": result = calc.logarithm(a)
            st.success(f"Result: {result}")
        except ValueError as e:
            st.error(str(e))