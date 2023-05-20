from behave import *


@then('forgot_password: I am redirected to forgot password page "{expected_forgot_pass_link}"')
def step_impl(context, expected_forgot_pass_link):
    context.forgot_password_page.verify_forgot_password_page(expected_forgot_pass_link)


@when('forgot_password: I fill in the e-mail address field with a valid e-mail "{email}"')
def step_impl(context, email):
    context.forgot_password_page.insert_email_address(email)


@when('forgot_password: I click on Send password button')
def step_impl(context):
    context.forgot_password_page.click_send_password()


@then('forgot_password: I get the success message "{success_msg}"')
def step_impl(context, success_msg):
    context.forgot_password_page.check_success_msg(success_msg)


@when('forgot_password: I fill in the e-mail address field with an invalid e-mail "{email}"')
def step_impl(context, email):
    context.forgot_password_page.insert_email_address(email)


@then('forgot_password: I get the error message "{error_msg}"')
def step_impl(context, error_msg):
    context.forgot_password_page.check_error_msg(error_msg)
