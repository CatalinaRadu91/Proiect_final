from behave import *


@given('login: I am on login page')
def step_impl(context):
    context.login_page.navigate_to_page()


@when('login: I enter a valid email "{email}" and a valid password "{password}"')
def step_impl(context, email, password):
    context.login_page.insert_username(email)
    context.login_page.insert_password(password)


@when('login: I click Intra in cont button')
def step_impl(context):
    context.login_page.click_intra_in_cont()


@when('login: I insert email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.login_page.insert_username(email)
    context.login_page.insert_password(password)


@then('login: I get the error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_error_message(error_message)


@when('login: user enters {email} and {password}')
def step_impl(context, email, password):
    if password == 'empty': password = ""
    if email == 'empty': email = ""
    context.login_page.insert_username(email)
    context.login_page.insert_password(password)


@then('login: I get the error message for empty field "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_error_message_for_empty_field(error_message)


@then('login: url has not changed')
def step_impl(context):
    context.login_page.navigate_to_page()


@when('login: I click on Ti-ai uitat parola? link')
def step_impl(context):
    context.login_page.click_forgot_pass_link()


@then('login: I get a success message and I am redirected back to the login page "{expected_login_page_link}"')
def step_impl(context, expected_login_page_link):
    context.login_page.verify_login_page(expected_login_page_link)
