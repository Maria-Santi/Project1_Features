from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from poms.employee_dashboard import EmployeeDashboard
from poms.manager_dashboard import ManagerDashboard


def before_all(context):
    driver: WebDriver = webdriver.Chrome('C:\\Users\\07mar\\Desktop\\drivers\\chromedriver.exe')

    employee_dashboard = EmployeeDashboard(driver)
    manager_dashboard = ManagerDashboard(driver)

    context.driver = driver
    driver.implicitly_wait(10)

    context.employee_dashboard = employee_dashboard
    context.manager_dashboard = manager_dashboard


def after_all(context: Context):
    context.driver.quit()
