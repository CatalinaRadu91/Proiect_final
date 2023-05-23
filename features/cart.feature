Feature: Zonia cart feature

  Background:
    Given home: I am a user on zonia.ro home page
    When home: I search after "Rochie Imperial Rosie"
    When products: I close cookies banner
    When products: I click on product name "Rochie Imperial Rosie"
    When products: I select size " XL " for the product and I add it to basket
    When products: I click on Cosul meu button

  @cart1
  Scenario: Test cart total sum functionality
    Then cart: I verify that total price is correct "449"


  @cart2
  Scenario: Test cart remove product functionality
    When cart: I click x sterge produs button
    Then cart: I verify empty cart message is displayed




