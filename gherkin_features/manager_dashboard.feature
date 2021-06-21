Feature: A Manager can view all reimbursement requests past and pending

  Background: The Manager is Logged In
    Given The Manager is on the Reimbursement System Home Page
    When The Manager enters their Email jkrowling@hogwarts.edu
    When The Manager enters their Password jkwizardyworld
    When The Manager clicks the Login Button
    Then The Manager should be logged in and on the Manager Dashboard Page

   Scenario Outline: Manager views all Requests
     Given The Manager is on the Manager Dashboard Page
      When The Manager clicks <sort> in the dropdown Sort By: button
      Then The Manager should see all their sorted requests in a table

     Examples: Manager Sorts Requests Table
        | sort |
        | Pending |
        | Past |
        | All |


    Scenario Outline: Resolve Requests
      Given The Manager is on the Manager Dashboard Page
      When The Manager clicks <choice> on the Choose: dropdown button in the Pending Requests table
      When The Manager sees a prompt box that says <prompt_box>
      When The Manager writes <message> into the prompt box
      Then The Manager should see an Alert Box that says <alert_box>
      Examples:
        | choice | prompt_box | message | alert_box |
        | Approve | Would you like to send a message to the employee? | Approved | The request was resolved |
        | Deny | Would you like to send a message to the employee? | It was for character development | The request was resolved |


  Scenario: Navigate to Statistics Page
      Given The Manager is on the Manager Dashboard Page
      When The Manager clicks on the View All Employee Statistics button
      Then The Manager should be on the Employee Statistics Page
