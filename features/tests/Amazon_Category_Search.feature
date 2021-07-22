# Created by yordi at 7/19/2021
Feature: Amazon_Drop_down_Search
  # Enter feature description here

  Scenario: User can select and search in a department
    Given Open Amazon Search
    When Select books department
    And Search for Faust
	Then Verify books department is selected