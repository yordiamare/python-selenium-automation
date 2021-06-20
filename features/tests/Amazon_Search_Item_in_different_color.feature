# Created by yordi at 6/19/2021
Feature: Search item in different color
  # Enter feature description here

  Scenario: User look for an item in different color
      Given Open Amazon Product Page
      When Search Product On The Search Space
      When User click Search Button
      When Click The Needed Product
      Then Verify User Can Click Through Colors