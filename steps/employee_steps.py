import time

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The Employee is on the Reimbursement System Home Page')
def step_impl(context):
    context.driver.get('file:///C:/Users/07mar/Desktop/ReimbursementSystem/Project1_FrontEnd/homepage.html')
    context.driver.maximize_window()


@when(u'The Employee enters their Email {email}')
def step_impl(context, email: str):
    context.employee_dashboard.employee_login_email().send_keys(email)


@when(u'The Employee enters their Password {passw}')
def step_impl(context, passw: str):
    context.employee_dashboard.employee_login_pass().send_keys(passw)


@when(u'The Employee clicks the Login Button')
def step_impl(context):
    context.employee_dashboard.employee_login_button().click()


@then(u'The Employee should be logged in and on the Employee Dashboard Page')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == 'Employee Dashboard'


@given(u'The Employee is on the Employee Dashboard Page')
def step_impl(context):
    title = context.driver.title
    assert title == 'Employee Dashboard'


@when(u'The Employee clicks {sort} in the dropdown Sort By: button')
def step_impl(context, sort: str):
    dropdown = context.employee_dashboard.get_requests_dropdown()
    dropdown.click()
    dropdown.parent.find_element_by_id(sort).click()


@then(u'The Employee should see all their sorted requests in a table')
def step_impl(context):
    element = context.employee_dashboard.get_requests()
    assert element == 'Requests Table'


@when(u'The Employee enters a request {reason} and {amount}')
def step_impl(context, reason: str, amount: int):
    context.employee_dashboard.submit_request_reason().send_keys(reason)
    context.employee_dashboard.submit_request_amount().send_keys(amount)


@when(u'The Employee clicks the Submit Request button')
def step_impl(context):
    context.employee_dashboard.submit_request_button().click()


@then(u'The Employee should see an Alert box that says {alert_box}')
def step_impl(context, alert_box: str):
    time.sleep(1)
    alert = context.driver.switch_to.alert
    assert alert.text == alert_box
    alert.accept()


@when(u'The Employee clicks on the Logout button')
def step_impl(context):
    context.employee_dashboard.employee_logout_button().click()


@then(u'The Employee should be logged out and redirected to the Reimbursement System Homepage')
def step_impl(context):
    title = context.driver.title
    assert title == 'Reimbursement System Home'
