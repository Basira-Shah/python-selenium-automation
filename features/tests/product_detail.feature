# Created by ahmadshah at 5/27/22
Feature: Tests for product page

  Scenario: User can select colors
    Given Open Amazon product B07MNHBRCJ page
    Then Verify user can click through colors

  # HW 5
  Scenario: User can select different colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click different colors

  Scenario: User can see product options
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user can see women image option
