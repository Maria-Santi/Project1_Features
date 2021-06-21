from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class ManagerDashboard:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def manager_login_email(self):
        element: WebElement = self.driver.find_element_by_id("managerEmail")
        return element

    def manager_login_pass(self):
        element: WebElement = self.driver.find_element_by_id("managerPass")
        return element

    def manager_login_button(self):
        element: WebElement = self.driver.find_element_by_id("manLogin")
        return element

    def get_requests(self):
        element = self.driver.find_element_by_id("tableCaption").text
        return element

    def get_requests_dropdown(self):
        element = self.driver.find_element_by_id("dropdownMenuRequests")
        return element

    def resolve_request_button(self):
        self.driver.execute_script("return document.body.innerHTML")
        element = self.driver.find_element_by_id("dropdownMenu")
        return element

    def view_stats_button(self):
        element = self.driver.find_element_by_id("statsBtn")
        return element

    def manager_logout(self):
        element = self.driver.find_element_by_id("logoutBtn")
        return element
