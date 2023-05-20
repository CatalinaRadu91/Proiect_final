from behave import *


@then('account: I am redirected to my account page "{expected_account_link}"')
def step_impl(context, expected_account_link):
    context.account_page.verify_account_page(expected_account_link)


@when('account: I click Contul meu button')
def step_impl(context):
    context.account_page.click_contul_meu_btn()


@when('account: I click Logout button')
def step_impl(context):
    context.account_page.click_logout_btn()
