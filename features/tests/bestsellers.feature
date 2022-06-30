# Created by ahmadshah at 6/14/22
Feature: Tests for bestsellers functionality


  Scenario: All bestsellers links are present
   Given Open Amazon Bestsellers
    Then Verify there are 5 links


  Scenario: Bestsellers links can be opened
    Given Open Amazon Bestsellers
    Then User can click through top links and verify correct page open






