Feature: An Employee Logs in to see their past and pending reimbursement requests and submit requests

  Background: The Employee is Logged In
    Given The Employee is on the Reimbursement System Home Page
    When The Employee enters their Email hermionegranger@hogwarts.edu
    When The Employee enters their Password hermionewizardyworld
    When The Employee clicks the Login Button
    Then The Employee should be logged in and on the Employee Dashboard Page

    Scenario Outline: Employee views all Requests
      Given The Employee is on the Employee Dashboard Page
      When The Employee clicks <sort> in the dropdown Sort By: button
      Then The Employee should see all their sorted requests in a table

      Examples: Employee Sorts Requests Table
        | sort |
        | Pending |
        | Past |
        | All |

    Scenario Outline: Employee submits a Reimbursement Request
      Given The Employee is on the Employee Dashboard Page
      When The Employee enters a request <reason> and <amount>
      When The Employee clicks the Submit Request button
      Then The Employee should see an Alert box that says <alert_box>

      Examples: Request Submission
        | reason | amount | alert_box |
        | Character Arch | 1000 | Your request was successfully submitted! |
