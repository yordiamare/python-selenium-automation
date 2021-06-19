# Created by yordi at 6/18/2021
Feature: Amazon add product into cart

  Scenario: Verify Open Amazon
    Given Open Amazon
    When Search Water Bottle On Amazon
    When Click On Search Button
    When Select Water Bottle
    When Click Add Cart
    When Click The Shopping Icon
    Then Verify The Subtotal Item