# Created by ahmadshah at 6/14/22
Feature: Tests for bestsellers functionality


  Scenario: Bestsellers links can be opened
   Given Open Amazon Bestsellers
    Then Verify there are 5 links in the Bestsellers
