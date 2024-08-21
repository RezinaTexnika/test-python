from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pytest

class RegistrationForm:
    def __init__(self, driver):
        self.driver = driver

    # locators
    first_name_input = (By.CSS_SELECTOR, "#firstName")
    last_name_input = (By.CSS_SELECTOR, "#lastName")
    email_input = (By.CSS_SELECTOR, "#userEmail")
    gender_radio_buttons = (By.CSS_SELECTOR, "#genterWrapper input[type='radio']")
    mobile_input = (By.CSS_SELECTOR, "#userNumber")
    date_of_birth_input = (By.CSS_SELECTOR, "#dateOfBirthInput")
    subjects_input = (By.CSS_SELECTOR, "#subjectsInput")
    picture_input = (By.CSS_SELECTOR, "#uploadPicture")
    current_address_input = (By.CSS_SELECTOR, "#currentAddress")
    state_dropdown = (By.CSS_SELECTOR, "#react-select-3-input")
    city_dropdown = (By.CSS_SELECTOR, "#react-select-4-input")
    submit_button = (By.CSS_SELECTOR, "#submit")

    # Actions
    def fill_first_name(self, name):
        self.driver.find_element(*self.first_name_input).send_keys(name)

    def fill_last_name(self, name):
        self.driver.find_element(*self.last_name_input).send_keys(name)

    def fill_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def select_gender(self, gender):
        gender_options = self.driver.find_elements(*self.gender_radio_buttons)
        for option in gender_options:
            if option.get_attribute('value') == gender:
                option.click()
                break

    def fill_mobile(self, mobile):
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def fill_date_of_birth(self, date):
        self.driver.find_element(*self.date_of_birth_input).send_keys(date)
        self.driver.find_element(*self.date_of_birth_input).send_keys(Keys.ENTER)

    def fill_subjects(self, subjects):
        self.driver.find_element(*self.subjects_input).send_keys(subjects)
        self.driver.find_element(*self.subjects_input).send_keys(Keys.ENTER)

    def upload_picture(self, file_path):
        self.driver.find_element(*self.picture_input).send_keys(file_path)

    def fill_current_address(self, address):
        self.driver.find_element(*self.current_address_input).send_keys(address)

    def select_state(self, state):
        self.driver.find_element(*self.state_dropdown).send_keys(state)
        self.driver.find_element(*self.state_dropdown).send_keys(Keys.ENTER)

    def select_city(self, city):
        self.driver.find_element(*self.city_dropdown).send_keys(city)
        self.driver.find_element(*self.city_dropdown).send_keys(Keys.ENTER)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    form = RegistrationForm(driver)

    form.fill_first_name("John")
    form.fill_last_name("Doe")
    form.fill_email("john.doe@example.com")
    form.select_gender("Male")
    form.fill_mobile("1234567890")
    form.fill_date_of_birth("1990-01-01")
    form.fill_subjects("Maths")
    form.upload_picture("path/to/picture.jpg")
    form.fill_current_address("123 Main Street")
    form.select_state("Haryana")
    form.select_city("Karnal")
    form.submit_form()

    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#example-modal-sizes-title-lg"))
    )
    assert success_message.text == "Thanks for submitting the form"