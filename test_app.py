# test_app.py
import streamlit as st
import car_price_predictor  # Assuming your Streamlit app script is named app.py

# Import the pytest_streamlit fixture
from pytest_streamlit import streamlit_tester

def test_prediction():
    # Define test inputs
    test_inputs = {
        'What is the current Ex-Showroom price of the car': 10.0,
        'What is the distance completed by the car in Miles?': 5000,
        'What is the Fuel type of the car?': 'Petrol',
        'Are you a Dealer or Individual?': 'Dealer',
        'What is the Transmission Type?': 'Manual',
        'Number of Owners the car previously had?': 1,
        'In which year car was purchased?': 2018
    }

    # Simulate the Streamlit app's behavior using Pytest-Streamlit
    with streamlit_tester(runner=app):
        # Set the inputs for the test
        for key, value in test_inputs.items():
            st.text_input(key, value)

        # Simulate clicking the 'Predict' button
        st.button('Predict')

        # Get the result of the prediction
        prediction_result = st.text('You can sell your car for')

        # Ensure the result is as expected
        expected_result = 'You can sell your car for 5.00 lakhs'
        assert prediction_result == expected_result
