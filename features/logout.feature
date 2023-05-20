Feature: Zonia logout feature

  Background:
    Given login: I am on login page
    When login: I enter a valid email "catalina.radu91@gmail.com" and a valid password "Par0l@XDX"
    When login: I click Intra in cont button
    Then account: I am redirected to my account page "https://www.zonia.ro/customer/account/edit/"

  @logout
  Scenario: logout successfully
    When home: I accept site notifications
    When account: I click Contul meu button
    When account: I click Logout button
    Then home: I am redirected to home page "https://www.zonia.ro/"
