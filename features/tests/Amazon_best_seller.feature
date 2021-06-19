# Created by yordi at 6/18/2021
Feature: Amazon Best Seller Page
  # Enter feature description here

  Scenario: Verify Amazon Best Seller Page
    Given Open Amazon Best Seller Page
    Then Verify Best Seller Link
    Then Verify New Release Link
    Then Verify Movers & Shakers
    Then Verify Most Wished For
    Then Verify Gift Areas