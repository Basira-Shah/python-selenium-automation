# Created by ahmadshah at 5/6/22
Feature: Tests for Amazon search

  Scenario Outline: Verify that user can search for product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result for <search_result> are shown
    Examples:
    |search_word  |search_result  |
    |coffee       |"coffee"       |
    |spoons       |"spoons"       |
    |dress        |"dress"        |

 # Scenario: Verify that user can search for spoons
 #   Given Open Amazon page
 #   When Search for spoons
 #   Then Verify search result for "spoons" are shown


  #Scenario: Verify that user can search for dress
  #  Given Open Amazon page
  # When Search for dress
  #  Then Verify search result for "dress" are shown



  # Feature for HW 4
  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Tritan Farn to Table Pitcher
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 items(s)


  Scenario: Verify that user can search for cancel order
    Given Open Amazon help page
    When Search for Cancel order in help customer page
    Then Verify search result for Cancel Items or Orders are shown in the help customer page


  Scenario: Verify that your amazon cart is empty
    Given Open Amazon page
    When click on the cart icon
    Then Verify your Amazon cart is empty


  Scenario: User sees ham menu btn on the main page
    Given Open Amazon page
    Then Verify hamburger menu btn present


  Scenario: User sees correct amount of footer links
    Given Open Amazon page
    Then Verify there are 38 footer links
  # HW 5
  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for coffee
    Then Verify that every product has a name and an image

  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present

  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by <dept_alias>
    And Search for <search_query>
    Then Verify <selected_dept> department is selected
    Examples:
     |dept_alias     |search_query    |selected_dept     |
     |stripbooks     |Faust           |books             |
     |audible        |Alice in        |audible           |

  # HW 8
  Scenario: User can select and search computers in a department
    Given Open Amazon page
    When Select computers department
    And Search for macbook
    Then Verify computers departments is selected