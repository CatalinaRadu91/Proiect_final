from behave import *


@then('cart: I verify that total price is correct "419"')
def step_impl(context):
    context.cart_page.verify_total_price("419")


@when('cart: I click x sterge produs button')
def step_impl(context):
    context.cart_page.click_remove_btn()


@then('cart: I verify empty cart message is displayed')
def step_impl(context):
    context.cart_page.verify_empty_cart_msg()
