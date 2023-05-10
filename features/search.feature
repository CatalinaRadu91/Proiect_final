#Feature: Zonia search feature
#
#  Background:
#    Given home: I am a user on zonia.ro home page
#
#  @search
#  Scenario Outline: Test search functionality
#    When home: I search after <query>
#    Then products: I verify that results contain search query <query>
#
#    Examples:
#      | query    |
#      | rochie   |
#      | ovya     |
#      | salopeta |
