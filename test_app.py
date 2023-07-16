# test_app.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def browser():
    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_prediction(browser):
    # Open the Streamlit app in the browser
    browser.get('http://localhost:8501')  # Replace with the URL of your Streamlit app

    # Find and interact with input elements
    input1 = browser.find_element_by_name('What is the current Ex-Showroom price of the car')
    input1.send_keys('10.0')

    input2 = browser.find_element_by_name('What is the distance completed by the car in Miles?')
    input2.send_keys('5000')

    # Add more interactions for other input elements as needed...

    # Click the 'Predict' button
    predict_button = browser.find_element_by_name('Predict')
    predict_button.click()

    # Wait for the result to load
    result_element = browser.find_element_by_name('You can sell your car for')
    result = result_element.text

    # Ensure the result is as expected
    expected_result = 'You can sell your car for 5.00 lakhs'
    assert result == expected_result
