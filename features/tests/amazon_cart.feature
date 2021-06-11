# Created by yordi at 6/8/2021
Feature: Feature: Test Amazon Cart

  Scenario: User sees empty shopping cart
    Given Open Amazon page
    When click on cart icon
    Then "Your Amazon Cart is empty" message is displaced

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for Coffee mug
    And click on the first product
    And click on Add to cart button
    Then Verify cart has 1 item