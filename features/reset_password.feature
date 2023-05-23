Feature: Zonia reset password feature

  Background:
    Given login: I am on login page
    When login: I click on Ti-ai uitat parola? link
    Then forgot_password: I am redirected to forgot password page "https://www.zonia.ro/customer/account/forgotpassword/"


  @reset_password1
  Scenario: validate the successful password reset message
    When forgot_password: I fill in the e-mail address field with a valid e-mail "marius.george.stefan@gmail.com"
    When forgot_password: I click on Send password button
    #Then forgot_password: I get the success message "Dacă există un cont având adresa marius.george.stefan@gmail.com vei primi un email pentru resetarea parolei. Nu uita să îţi verifici şi căsuţa de SPAM."
    # deoarece mesajul de eroare contine diacritice (primesc eroarea: 'charmap' codec can't encode character '\u0103' in position 9262: character maps to <undefined>)
    Then login: I get a success message and I am redirected back to the login page "https://www.zonia.ro/customer/account/login/"

  @reset_password2
  Scenario: validate the error password reset message
    When forgot_password: I fill in the e-mail address field with an invalid e-mail "alabala@portocala"
    When forgot_password: I click on Send password button
    Then forgot_password: I get the error message "Invalid email address."


    # ultimul pas de la ambele scenarii uneori pica atunci cand incerc de pe acelasi IP sa resetez parola de prea multe ori
    # trebuie sa revin in 24 h; msg site (test manual): You have exceeded requests to times per hour from 1 IP.


