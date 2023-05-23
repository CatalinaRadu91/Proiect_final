#Feature: Zonia search feature
#
#  Background:
#    Given home: I am a user on zonia.ro home page
#    When home: I accept site notifications
#
#  @search
#  Scenario Outline: Test search functionality
#    When home: I search after <query> and I press Enter
#    Then products: I verify that results contain search query <query>
#
#    Examples:
#      | query    |
#      | rochie   |
#      | ovya     |
#      | salopeta |

