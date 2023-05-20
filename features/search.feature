Feature: Zonia search feature

  Background:
    Given home: I am a user on zonia.ro home page

  @search
  Scenario Outline: Test search functionality
    When home: I accept site notifications
    When home: I search after <query> and I press Enter
    Then products: I verify that results contain search query <query>

    Examples:
      | query    |
      | rochie   |
      | ovya     |
      | salopeta |


    # pentru rochie trece scenariul
    # pentru ovy si salopeta sa blocheaza la pasul de acceptare a notificarii :( din cauza ca acea notificare nu este afisata de fiecare data?
    # ce pot sa fac sa le treaca pe toate 3?