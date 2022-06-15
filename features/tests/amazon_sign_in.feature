# Created by ahmadshah at 5/21/22
Feature: Amazon Sign in tests

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign In page is opened