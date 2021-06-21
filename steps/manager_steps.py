import time

from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given(u'The Manager is on the Reimbursement System Home Page')
def step_impl(context):
    context.driver.get('file:///C:/Users/07mar/Desktop/ReimbursementSystem/Project1_FrontEnd/homepage.html')
    context.driver.maximize_window()


@when(u'The Manager enters their Email {email}')
def step_impl(context, email: str):
    context.manager_dashboard.manager_login_email().send_keys(email)


@when(u'The Manager enters their Password {passw}')
def step_impl(context, passw: str):
    context.manager_dashboard.manager_login_pass().send_keys(passw)


@when(u'The Manager clicks the Login Button')
def step_impl(context):
    context.manager_dashboard.manager_login_button().click()


@then(u'The Manager should be logged in and on the Manager Dashboard Page')
def step_impl(context):
    time.sleep(1)
    title = context.driver.title
    assert title == 'Manager Dashboard'


@given(u'The Manager is on the Manager Dashboard Page')
def step_impl(context):
    title = context.driver.title
    assert title == 'Manager Dashboard'


@when(u'The Manager clicks {choice} on the Choose: dropdown button in the Pending Requests table')
def step_impl(context, choice: str):
    dropdown = context.manager_dashboard.resolve_request_button()
    dropdown.click()
    dropdown.parent.find_element_by_id(choice).click()


@when(u'The Manager sees a prompt box that says {prompt_box}')
def step_impl(context, prompt_box: str):
    time.sleep(1)
    alert = context.driver.switch_to.alert
    assert alert.text == prompt_box


@when(u'The Manager writes {message} into the prompt box')
def step_impl(context, message: str):
    alert = context.driver.switch_to.alert
    alert.send_keys(message)
    alert.accept()


@then(u'The Manager should see an Alert Box that says {alert_box}')
def step_impl(context, alert_box: str):
    time.sleep(1)
    alert = context.driver.switch_to.alert
    assert alert.text == alert_box
    alert.accept()


@when(u'The Manager clicks {sort} in the dropdown Sort By: button')
def step_impl(context, sort: str):
    dropdown = context.employee_dashboard.get_requests_dropdown()
    dropdown.click()
    dropdown.parent.find_element_by_id(sort).click()


@then(u'The Manager should see all their sorted requests in a table')
def step_impl(context):
    element = context.employee_dashboard.get_requests()
    assert element == 'Requests Table'


@when(u'The Manager clicks on the View All Employee Statistics button')
def step_impl(context):
    context.manager_dashboard.view_stats_button().click()


@then(u'The Manager should be on the Employee Statistics Page')
def step_impl(context):
    title = context.driver.title
    assert title == 'Employee Statistics'


@given(u'The Manager is on the Employee Statistics Page')
def step_impl(context):
    title = context.driver.title
    assert title == 'Employee Statistics'


@when(u'The Manager clicks on the Logout button')
def step_impl(context):
    context.manager_dashboard.manager_logout().click()


@then(u'The Manager should be logged out and redirected to the Reimbursement System Page Homepage')
def step_impl(context):
    title = context.driver.title
    assert title == 'Reimbursement System Home'
