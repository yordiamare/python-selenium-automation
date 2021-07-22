# Created by yordi at 7/18/2021
Feature: Language selection tests


  Scenario: User can see Spanish language option
    Given Open Amazon Help page
    When Move mouse over flag icon
    Then Spanish language selection is visible
