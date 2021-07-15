# Created by yordi at 5/27/2021
Feature: Test Amazon search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Table in search field
    And Click on Amazon search icon
    #Then Verify search_worked

