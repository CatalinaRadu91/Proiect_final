#Feature: Zonia login feature
#
#  Background:
#    Given login: I am on login page
#
#  @validcreds
#  Scenario: login successfully with valid credentials
#    When login: I enter a valid email "catalina.radu91@gmail.com" and a valid password "Par0l@XDX"
#    When login: I click Intra in cont button
#    Then account: I am redirected to my account page "https://www.zonia.ro/customer/account/edit/"
#
#
#  @invalidcreds
#  Scenario Outline: login with invalid password
#    When login: I insert email "<email>" and password "<password>"
#    When login: I click Intra in cont button
#    Then login: I get the error message "Login sau parola invalida"
#    Examples:
#      | email                     | password     |  |
#      | catalina.radu91@gmail.com | testpassword |  |
#      | catalina.radu@gmail.com   | Par0l@XDX    |  |
#      | catalina.radu@gmail.com   | testpassword |  |
#
#
#    # gabi? 1. e corect? 2. am vazut ca syntaxa gherkin foloseste si "and"; in steps de ce nu-l pot folosi?
#  @emptypassword
#  Scenario: log in with empty password
#    When login: I insert email "<email>" and I do not fill in the password field
#    When login: I click Intra in cont button
#    Then login: I get the error message "Camp obligatoriu"
#    And login: url has not changed




