from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class EmployeeDashboard:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def employee_login_email(self):
        element: WebElement = self.driver.find_element_by_id("employeeEmail")
        return element

    def employee_login_pass(self):
        element: WebElement = self.driver.find_element_by_id("employeePass")
        return element

    def employee_login_button(self):
        element: WebElement = self.driver.find_element_by_id("empLogin")
        return element

    def get_requests_dropdown(self):
        element = self.driver.find_element_by_id("dropdownMenuRequests")
        return element

    def get_requests(self):
        element = self.driver.find_element_by_id("tableCaption").text
        return element

    def submit_request_reason(self):
        element = self.driver.find_element_by_id("requestReasonInput")
        return element

    def submit_request_amount(self):
        element = self.driver.find_element_by_id("requestAmountInput")
        return element

    def submit_request_button(self):
        element = self.driver.find_element_by_id("submitRequestBtn")
        return element

    def employee_logout_button(self):
        element = self.driver.find_element_by_id("logoutBtn")
        return element
