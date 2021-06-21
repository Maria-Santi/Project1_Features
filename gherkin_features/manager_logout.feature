Feature: A Manager can logout

  Background:
    Given The Manager is on the Employee Statistics Page

    Scenario: Manager logs out
      When The Manager clicks on the Logout button
      Then The Manager should be logged out and redirected to the Reimbursement System Page Homepage
