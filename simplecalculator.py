import streamlit as st
import math

# Set the title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Selectbox for the operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation based on the operation selected
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is {result}")
        else:
            st.write("Error: Division by zero is not allowed.")

# Run the app
if __name__ == "__main__":
    st.write("Simple Calculator App")