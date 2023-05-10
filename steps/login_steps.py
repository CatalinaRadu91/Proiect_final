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


@when('login: I insert email "<email>" and I do not fill in the password field')
def step_impl(context, email):
    context.login_page.insert_username(email)


# @then('login: I get the error message "Camp obligatoriu"')
# def step_impl(context, error_message):
#     context.login_page.check_error_message_for_empty_field(error_message)


# aici in feature, este cu "and", aici pot sa-l pun cu then?
@then('login: url has not changed')
def step_impl(context):
    context.login_page.navigate_to_page()
