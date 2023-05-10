Feature: Zonia cart feature

  Background:
    Given home: I am a user on zonia.ro home page


  @cart @cart1
  Scenario: Test cart total sum functionality
    When home: I search after "Rochie Madeira Rosie"
    When products: I click on product name "Rochie Madeira Rosie"
    When products: I select size for the product and I add it to basket
#    When products: I click on Cosul meu button
#    Then cart: I verify that total price is correct "419"


#  @cart @cart2
#  Scenario: Test cart remove product functionality
#    When cart: I click x (sterge produs) button
#    Then cart: I verify empty cart message is displayed

