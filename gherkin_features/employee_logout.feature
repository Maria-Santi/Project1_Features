Feature: An Employee can logout

    Scenario: Employee logs out
      Given The Employee is on the Employee Dashboard Page
      When The Employee clicks on the Logout button
      Then The Employee should be logged out and redirected to the Reimbursement System Homepage
