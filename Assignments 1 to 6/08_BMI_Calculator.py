import streamlit as st

# Title
st.title("🏋️ BMI Calculator")

# Input sliders with better min values
height = st.slider("Enter your height (cm)", min_value=50, max_value=300, value=170)
weight = st.slider("Enter your weight (kg)", min_value=10, max_value=300, value=70)

# Button to calculate BMI
if st.button("Calculate BMI"):
    if height == 0:  # Prevent division by zero
        st.error("⚠️ Height cannot be zero! Please enter a valid height.")
    elif weight == 0:
        st.error("⚠️ Weight cannot be zero! Please enter a valid weight.")
    else:
        bmi = weight / ((height / 100) ** 2)
        st.success(f"📊 Your BMI is: **{bmi:.2f}**")

        # Interpret BMI with color-coded messages
        if bmi < 18.5:
            st.warning("🟡 You are **Underweight**. Consider a balanced diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("🟢 You are **Normal**. Keep maintaining a healthy lifestyle!")
        elif 25 <= bmi < 29.9:
            st.warning("🟠 You are **Overweight**. Consider regular exercise.")
        else:
            st.error("🔴 You are **Obese**. Consult a healthcare professional.")

        # Display BMI Interpretation Chart
        st.markdown("""
        ### BMI Categories:
        - **Underweight**: BMI < 18.5 🟡
        - **Normal**: 18.5 – 24.9 🟢
        - **Overweight**: 25 – 29.9 🟠
        - **Obese**: BMI ≥ 30 🔴
        """)

