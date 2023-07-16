# test_app.py
import unittest
import streamlit as st
from StreamlitClient import StreamlitClient


class TestApp(unittest.TestCase):
    def setUp(self):
        # Create a Streamlit client instance
        self.client = StreamlitClient('app.py')

    def test_prediction(self):
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

        # Set the inputs for the test
        self.client.set_input(test_inputs)

        # Simulate clicking the 'Predict' button
        self.client.submit_form('Predict')

        # Get the result of the prediction
        prediction_result = self.client.get_element_text('You can sell your car for')

        # Ensure the result is as expected
        expected_result = 'You can sell your car for 5.00 lakhs'
        self.assertEqual(prediction_result, expected_result)

    def tearDown(self):
        # Close the Streamlit app after each test
        self.client.close()


if __name__ == '__main__':

