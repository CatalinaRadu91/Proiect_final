from behave import *


@then('account: I am redirected to my account page "{expected_account_link}"')
def step_impl(context, expected_account_link):
    context.account_page.verify_account_page(expected_account_link)
