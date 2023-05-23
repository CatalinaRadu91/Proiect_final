#Feature: Zonia menu feature
#
#  Background:
#    Given home: I am a user on zonia.ro home page
#    When home: I accept site notifications
#
#  @tab
#  Scenario Outline: validate that when you access different tabs in the menu, you are redirected to the corresponding page
#    When home: I click on <tab_name>
#    Then <page_name>: I verify that the url is "https://www.zonia.ro/<url_path>"
#
#    Examples:
#      | page_name     | tab_name      | url_path           |
#      | Noua Colectie | Noua Colectie | noua-colectie.html |
#      | BestSeller    | BestSeller    | bestseller.html    |
#      | Oferte        | Oferte        | oferte.html        |


