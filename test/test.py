from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv  # Import CSV module to read the file
from selenium import webdriver




# Function to read test cases from CSV
def read_test_cases(filename):
    test_cases = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_cases.append(row)
    return test_cases

# Your existing Selenium setup
submit_xpath = "//button[text()='Submit']"
# driver_path = "test/chromedriver"
# print(driver_path)
# service = Service(executable_path=driver_path)
# driver = webdriver.Chrome(service=service)

# Function to fill and submit the form for a single test case
def submit_form(name, email):
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/submit/")

    name_input = driver.find_element(By.NAME, 'name')
    email_input = driver.find_element(By.NAME, 'email')

    name_input.send_keys(name)
    email_input.send_keys(email)

    submit_button = driver.find_element(By.XPATH, submit_xpath)
    submit_button.click()

# Main logic to iterate over test cases
test_cases = read_test_cases('test_cases.csv')  # Make sure to have test_cases.csv in your working directory
for case in test_cases:
    submit_form(case['name'], case['email'])

# Cleanup
driver.quit()
