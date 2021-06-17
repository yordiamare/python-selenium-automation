# Created by yordi at 6/8/2021
Feature: Test Amazon Cart Empty

  Scenario: User Verifies Amazon Cart is Empty
    Given Open Amazon url
    When Click on cart
    Then Verify Your Amazon Cart is empty