Feature: Zonia menu feature

  Background:
    Given home: I am a user on zonia.ro home page

  @tab
  Scenario Outline: Click on item tab
    When home: I accept site notifications
    When home: I click on <tab_name>
    Then <page_name>: I verify that the url is "https://www.zonia.ro/<url_path>"

    Examples:
      | page_name     | tab_name      | url_path           |
      | Noua Colectie | Noua Colectie | noua-colectie.html |
      | BestSeller    | BestSeller    | bestseller.html    |
      | Oferte        | Oferte        | oferte.html        |


    # primul test trece, urmatoarele 2 nu deoarece se blocheaza la site notification :( din cauza ca acea notificare nu este afisata de fiecare data?
    # ce pot sa fac sa le treaca pe toate 3?