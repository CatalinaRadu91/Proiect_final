#Feature: Zonia login feature
#
#  Background:
#    Given login: I am on login page
#
#  @valid_creds
#  Scenario: login successfully with valid credentials
#    When login: I enter a valid email "catalina.radu91@gmail.com" and a valid password "Par0l@XDX"
#    When login: I click Intra in cont button
#    Then account: I am redirected to my account page "https://www.zonia.ro/customer/account/edit/"
#
#
#  @invalid_creds
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
#  @empty_creds
#  Scenario Outline: login with empty creds
#    When login: user enters <email> and <password>
#    When login: I click Intra in cont button
#    Then login: I get the error message for empty field "Camp obligatoriu"
#    Then login: url has not changed
#
#    Examples:
#      | email         | password  |
#      | xyz@yahoo.com | empty     |
#      | empty         | parola123 |


