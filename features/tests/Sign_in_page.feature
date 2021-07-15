# Created by yordi at 7/6/2021
  Feature: Test sign_in page

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon Site
 When Click Amazon Orders link
 Then Verify Sign In page is opened